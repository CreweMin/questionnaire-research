$(function () {
	showModelInfors($('#modelList'),1);
	function showModelInfors(box,id){
		$.get(url+diliverClassUrl,
		  {'classify_id': id, 'usertoken': $.cookie('usertoken')},
		  function (data){
		  	if(data['infostatus']){
					// 数据录入
					dataEntry(data['inforesult']);
			}
		  }
		)
	}
	// 返回对应的值
	$("#searchText").on("keyup paste focus",function(){  
         previewSearch($(this).val(), $(this).parent());
	}).blur(function (){
			setTimeout(function (){ 
				$("ul.ul").remove();
			},500);
	});

	// 点击搜索
	$('#searchBtn').click(function (){
		// url 为要跳转的路径
		const url = 'page/wodewenjuan/mubanxiangqing.html';
		serachFound($('#searchText').val(),url);
	});


	// // 点击不同类别获取不同模板
	// $("#classType div").on('click', function (){
	// 	// alert($(this).attr('id'));
	// 	$('#modelList').empty();
	// 	showModelInfors($('#modelList'), $(this).attr('id'));
	// })
	
	// 使用模板
	$("#userful").click(function (event){
		event.preventDefault();
		const urls = url + releaseQuestUrl;
		$.post(
			urls, 
			{
			 "usertoken":$.cookie("usertoken"),
			 "questionnaire_id":$.cookie('model_id')
			},
			function (data){
				if(data["infostatus"]){
					alert(data['infomsg']);
					window.location.href = 'fabuwenjuan.html';
				}
		})
	});

	// 返回问卷类别`
	 $.get(url + classIdUrl,
	 	function (data){
	 		if(!data['infostatus']){
	 			for (var i = 0; i < data['inforesult'].length; i++) {
	 				const content = data['inforesult'][i]['classify_content'];
	 				const id = data['inforesult'][i]['classify_id'];
	 				const div = $(`<div class="col-md-12 w-model" id="4">${content}</div>`);
	 				div.attr('id', id);
	 				$("#classType").append(div);
	 				const label = $(`<label class="btn btn-primary">
							<input type="radio" name="options" value="1" id="${id}"> ${content}
						</label>`);
	 				$("#classTypeLabel").append(label);
	 				// 点击不同类别获取不同模板
	 			}
	 			$("#classType div").on('click', function (){
						// alert($(this).attr('id'));
						$('#modelList').empty();
						showModelInfors($('#modelList'), $(this).attr('id'));
					})
	 		}
	 	})
});



// 数据录入
function dataEntry(data){
	for (var i = 0; i < data.length; i++) {
		const div = createElen(data[i]['questionnaire_id'], data[i]['questionnaire_title'], data[i]['subject_number']);
		$("#modelList").append(div);
	}
}
//  创建盒子
// function createElen(key,val){
// 	const el = `<div class="nav nav-pills border w-h-95">
// 					<a href="{$questionnaire_id}"> {$questionnaire_title}<span class="badge pull-right">{$subject_number}</span></a>
// 				</div>`;
// }
function createElen(id, title, num){
	let div = $('<div class="nav nav-pills border w-h-95">'), a = $("<a href='#myModal' data-toggle='modal' onclick='modelDetailShow(this)'>"), span = $('<span  class="badge pull-right">');
	a.html(title);
	span.html(num);
	a.append(span);
	a.attr('id',id);
	div.append(a);
	return div;
}

//  创建选项组件  subject_options
function createCheckBox(title, optionArr){
	let boxDiv = $("<div class='col-md-10 column'>");
	let titleDiv = $('<div class="row  w-clear-margin "><p class="pull-left">' + title + '</p></div>');
	const ul = createOption(optionArr);
	boxDiv.append(titleDiv);
	boxDiv.append(ul);
	return boxDiv;
}
//  创建 选项
function createOption(arr){
	let ul = $('<ul class="row">');
	for (let i = 0; i < arr.length; i++) {
		let label = $('<label  class="col-md-12"><input type="checkbox" class="bnt btn-default">' + arr[i]["option_content"] + '</label>');
		ul.append(label);
	}
	return ul;
}

// 模态框详情展示
function modelDetailShow(obj){
	const id = $(obj).attr('id');
	const urls = url + questionDetailUrl ;//openTitileURl;
	$.cookie('model_id', id,{ expires: 1, path: '/' });
	let json = {usertoken: $.cookie('usertoken'), "questionnaire_id": id};
	// 显示问卷数据
	$.get(urls,
		json,
		function (data){
			if(data['infostatus']){  
				$("#title").html(data['inforesult']['questionnaire_title']);
				$("#introduce").html(data['inforesult']['questionnaire_intro']);
				$('#showDdetail').empty();
				showQuestionDetail(data['inforesult']['questionnaire_detail']);
			} else {
				alert(data['infomsg'])
			}
	})
}
// 问卷详情展示
function showQuestionDetail(arr){
	for (let i = 0; i < arr.length; i++) {
		addQuestionNumber(arr[i]['subject_option_flag'], arr[i], i);
	}
}
//  增加选项
function addQuestionNumber(type, arr,i){
		if(type == 1 ){
			let box = createRadioTitle(i+1, type);
			const tv = arr['subject_title'];
			$(box).find('p.title').html(tv);
			$(box).find('p.title').attr('data', arr['subject_id']);
			paddingContentOpt(box, arr['subject_options'], i, arr['subject_option_flag']);
			$('#showDdetail').append(box);
		}
		if(type == 2 ){
			let box = createCheckTitle(i+1, type);
			const tv = arr['subject_title'];
			$(box).find('p.title').html(tv);
			$(box).find('p.title').attr('data', arr['subject_id']);
			paddingContentOpt(box, arr['subject_options'], i, arr['subject_option_flag']);
			$('#showDdetail').append(box);
		}
		if(type == 3 ){
			let box = createTextTitle(i+1, type);
			const tv = arr['subject_title'];
			$(box).find('p.title').html(tv);
			$(box).find('p.title').attr('data', arr['subject_id']);
			$('#showDdetail').append(box);
		}
}
//  循环增加选项内容
function paddingContentOpt(box, data, j, type){
	for (let i = 0; i < data.length; i++) {
		if(type == 1 ){
			$(box).find('ul.optionArr').append(createRadioOption(data[i]['option_content'], j, data[i]['option_id']));
		}
		if(type == 2 ){
			$(box).find('ul.optionArr').append(createCheckOption(data[i]['option_content'], j, data[i]['option_id']));
		}
	}
}
// 创建选项

function createCheckOption(data, i, id){
	const li = `<li  class="col-md-12"><input type="checkbox" name='name${i}' class="bnt btn-default" data='${id}'><span>${data}</span></li>`;
	return $(li);
}

function createRadioOption(data, i, id){
	const li = `<li  class="col-md-12"><input type="radio" name='name${i}' class="bnt btn-default" data='${id}'><span>${data}</span></li>`;
	return $(li);
}

// 创建题目  多选题
function createCheckTitle(num ,type){
	let title = `<div class="row clearfix border">
								<div class="col-md-10 column border">
									<div class="row  w-clear-margin ">
										<p class="pull-left title" type='${type}'>
											多选题
										</p>
									</div>
									<ul class="row optionArr">
									</ul> 
									</div>

								</div>`;
	return $(title);

}
// 创建题目  单选题
function createRadioTitle(num, type){
	let title = `<div class="row clearfix border">
								<div class="col-md-10 column border">
									<div class="row  w-clear-margin ">
										<p class="pull-left title" type='${type}'>
											单选题
										</p>
									</div>
									<ul class="row optionArr">
									</ul> 
									</div>

								</div>`;
		return $(title);

}
// 创建题目  填空题
function createTextTitle(num, type){
	let title = `<div class="row clearfix border">
								<div class="col-md-10 column border">
									<div class="row  w-clear-margin ">
										<p class="pull-left title" type='${type}'>
											填空题
										</p>
									</div>
									<ul class="row optionArr">
										  <li  class="col-md-12"><textarea  rows="6" cols='30' type="text" class="bnt btn-default"></textarea></li>
									</ul> 
									
								</div>

					</div>`;
	return $(title);

}