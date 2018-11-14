$(function (){
	$.get(url + myAllQuestUrl, 
		{"usertoken":$.cookie('usertoken'),"questionnaire_flag":1},
		function (data){
			if(data['infostatus']){
				dataEntry($("#titleBox"), data['inforesult']);
			}
	});



})
// 数据录入
function dataEntry(box, data){
	for (var i = 0; i < data.length; i++) {
		box.append(createTr(data[i]['questionnaire_title'],null, data[i]['questionnaire_id']));
	}
}
// 创建一一行表格
function createTr(title, time,id){
	 let tr = `<tr>
			      <td data='${id}'><a href="#myModal" data-toggle="modal" id='${id}' onclick="modelDetailShow(this)"> ${title}</a></td>
			      <td>${time}</td>
		     </tr>`;
	return tr;
}

// 模态框	  
// function questionDetailModel(id){
// 	// $('#questTitle').html(data)
// 	$.get(
// 		url + questionDetailUrl,
// 		{"usertoken":$.cookie('usertoken'), "questionnaire_id": id},
// 		function (data){

// 		}
// 		)
// }
function modelDataPadding(data) {
	$("#questTitle").html();
	$("#questDetail").html();
	for (var i = data['inforesult']['questionnaire_detail'].length - 1; i >= 0; i--) {
		$("#optionBox").append(modelOptionData(data['inforesult']['questionnaire_detail'][i]));
	}
}

//  选项数据加入
function modelOptionData(data){
	return `<div class="col-md-10 column">
				<div class="row  w-clear-margin ">
					<p class="pull-left">
						${data['subject_title']}
					</p>
				</div>
				<ul class="row">
					  <label  class="col-md-12"><input type="checkbox" class="bnt btn-default">选项一</label>
					 <label  class="col-md-12"><input type="checkbox" class="bnt btn-default">选项二</label>
				</ul> 
			</div>`;
}

// 模态框详情展示
function modelDetailShow(obj){
	const id = $(obj).attr('id');
	const urls = url + questionDetailUrl;//openTitileURl;
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