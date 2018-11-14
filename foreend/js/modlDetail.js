$(function (){
	$.get(url+ questionDetailUrl,
		 {usertoken: $.cookie('usertoken'), questionnaire_id: $.cookie('modelDetailId')},
		 function (data) {
		 		$("#title").html(data['inforesult']['questionnaire_title']);
				$("#introduce").html(data['inforesult']['questionnaire_intro']);
				showQuestionDetail(data['inforesult']['questionnaire_detail']);
		 })
})

// 问卷详情展示
function showQuestionDetail(arr){
	for (let i = 0; i < arr.length; i++) {
		addQuestionNumber(arr[i]['subject_option_flag'], arr[i], i);
	}
}
//  增加选项
function addQuestionNumber(type, arr,i){
	const id = arr['subject_id'];
		if(type == 1 ){
			let box = createRadioTitle(type, id);
			const tv = arr['subject_title'];
			$(box).find('p.title').html(tv);
			$(box).find('p.title').attr('data', arr['subject_id']);
			paddingContentOpt(box, arr['subject_options'], arr['subject_option_flag']);
			$('#showDdetail').append(box);
		}
		if(type == 2 ){
			let box = createCheckTitle(type, id);
			const tv = arr['subject_title'];
			$(box).find('p.title').html(tv);
			$(box).find('p.title').attr('data', arr['subject_id']);
			paddingContentOpt(box, arr['subject_options'], arr['subject_option_flag']);
			$('#showDdetail').append(box);
		}
		if(type == 3 ){
			let box = createTextTitle(type, id);
			const tv = arr['subject_title'];
			$(box).find('p.title').html(tv);
			$(box).find('p.title').attr('data', arr['subject_id']);
			$('#showDdetail').append(box);
		}
}
//  循环增加选项内容
function paddingContentOpt(box, data, type){
	for (let i = 0; i < data.length; i++) {
		if(type == 1 ){
			$(box).find('ul.optionArr').append(createRadioOption(data[i]['option_content']));
		}
		if(type == 2 ){
			$(box).find('ul.optionArr').append(createCheckOption(data[i]['option_content']));
		}
	}
}
// 创建选项

function createCheckOption(data){
	const li = `<label  class="col-md-12"><input type="checkbox" class="bnt btn-default">${data}</label>`;
	return $(li);
}

function createRadioOption(data){
	const li = `<label  class="col-md-12"><input type="radio" class="bnt btn-default">${data}</label>`;
	return $(li);
}

// 创建题目  多选题
function createCheckTitle(type, id){
	let title = `<div class="row">
						<div class="col-md-12 column">
							<div class="row  w-clear-margin ">
								<p class="pull-left col-md-4 title" type='${type}'>您的爱好是？</p>
								<div class="pull-right col-md-3">
									<button id='${id}' onclick='deleteId(this)'>删除</button>&nbsp;&nbsp;&nbsp;&nbsp;<button data-toggle="modal" data-target="#myModal" onclick='alter(this)'>修改</button>
								</div>
							</div>
							<ul class="row optionArr">
							</ul> 
						</div>
						
					</div>`;
	return $(title);

}
// 创建题目  单选题
function createRadioTitle(type, id){
	let title = `<div class="row">
						<div class="col-md-12 column">
							<div class="row  w-clear-margin ">
								<p class="pull-left col-md-4 title" type='${type}'>您的爱好是？</p>
								<div class="pull-right col-md-3">
									<button id='${id}' onclick='deleteId(this)'>删除</button>&nbsp;&nbsp;&nbsp;&nbsp;<button data-toggle="modal" data-target="#myModal" onclick='alter(this)'>修改</button>
								</div>
							</div>
							<ul class="row optionArr">
							</ul> 
						</div>
						
					</div>`;
		return $(title);

}
// 创建题目  填空题
function createTextTitle(type, id){
	let title =  `<div class="row">
						<div class="col-md-12 column">
							<div class="row  w-clear-margin ">
								<p class="pull-left col-md-4 title" type='${type}'>您的爱好是？</p>
								<div class="pull-right col-md-3">
									<button id='${id}' onclick='deleteId(this)'>删除</button>&nbsp;&nbsp;&nbsp;&nbsp;<button data-toggle="modal" data-target="#myModal" onclick='alter(this)'>修改</button>
								</div>
							</div>
							<ul class="row optionArr">
								  <li  class="col-md-12"><textarea  rows="6" cols='30' type="text" class="bnt btn-default"></textarea></li>
							</ul> 
						</div>
						
					</div>`;
	return $(title);

}

// 删除题目
function deleteId(obj){
	const id = $(obj).prop('id');
	const urls = url + deleteTitleUrl;
	$.post(
		urls, 
		{
		 "usertoken":$.cookie("usertoken"),
		 "subject_id": id
		},
		function (data){
			alert(data['infomsg']);
			window.location.reload();
	})
}

// 修改题目
function alter(obj){
	const id = $(obj).prev().prop('id');
	$.get(
		url + getIdContentUrl,
		{"usertoken":$.cookie('usertoken'),"subject_id": id},
		function (data){
			const type = data['inforesult']['subject_option_flag'];
			let arr = data['inforesult'];
			$("#showDetail").empty();
			if(data['infostatus']){
				if(type == 1){
					let box = createCheckTitle(type, id);
					deleteButton(box);
					contenteditableTrue(box)
					$(box).find('p.title').html(arr['subject_title']);
					paddingContentOpt(box, arr['options'], arr['subject_option_flag']);
					$("#showDetail").append(box);
				}
				if(type == 2){
					let box = createCheckTitle(type, id);
					deleteButton(box);
					contenteditableTrue(box)
					$(box).find('p.title').html(arr['subject_title']);
					paddingContentOpt(box, arr['options'], arr['subject_option_flag']);
					$("#showDetail").append(box);
				}
				if(type == 3){
					let box = createTextTitle(type, id);
					deleteButton(box);
					contenteditableTrue(box)
					$(box).find('p.title').html(arr['subject_title']);
					$("#showDetail").append(box);
				}
			}
		}
	)
}

// 删除的两个button 
function deleteButton(obj){
	$(obj).find('button:not(.btn)').remove();
}

// 可编辑
function contenteditableTrue(obj){
	$(obj).not('button.btn').prop('contenteditable', true);
}