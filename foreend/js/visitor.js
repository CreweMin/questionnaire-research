$(function (){
	// 举报问卷
	$('#report').on('click', function (){
		$.post(
			url + reportUrl,
			{"questionnaire_id": $.cookie('searchContent')},
			function (data){
				alert(data['infomsg']);
			})
	})
	if($('#detail').html() == '问卷详情'){
		var urls = url + questionDetailUrl;
		var json = {usertoken: $.cookie('usertoken'), "questionnaire_id":$.cookie('searchContent')};
	} else {
		var urls = url + openTitileURl;
		var json = {"questionnaire_id":$.cookie('searchContent')};
	}
	// 显示问卷数据
	$.get(urls,
		json,
		function (data){
			if(data['infostatus']){  
				$("#title").html(data['inforesult']['questionnaire_title']);
				$("#introduce").html(data['inforesult']['questionnaire_intro']);
				showQuestionDetail(data['inforesult']['questionnaire_detail']);
			} else {
				alert(data['infomsg'])
			}
	})

	// 提交
	$('#up').click(function (){
		const urls = url + upQuestionUrl;
		upContent(urls);
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
	const li = `<li  class="col-md-12"><input type="checkbox" name='name${i}' class="bnt btn-default" data='${id}'><span contenteditable="true">${data}</span></li>`;
	return $(li);
}

function createRadioOption(data, i, id){
	const li = `<li  class="col-md-12"><input type="radio" name='name${i}' class="bnt btn-default" data='${id}'><span>${data}</span></li>`;
	return $(li);
}

// 创建题目  多选题
function createCheckTitle(num ,type){
	let title = `<div class="row clearfix border w-m-t-15">
								<div class="col-md-2 column">
									<h3 class="titleNum" type='${type}'>
										${num}
									</h3>
								</div>
								<div class="col-md-10 column border">
									<div class="row  w-clear-margin ">
										<p class="pull-left title">
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
	let title = `<div class="row clearfix border w-m-t-15">
								<div class="col-md-2 column">
									<h3 class="titleNum" type='${type}'>
										${num}
									</h3>
								</div>
								<div class="col-md-10 column border">
									<div class="row  w-clear-margin ">
										<p class="pull-left title">
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
	let title = `<div class="row clearfix border w-m-t-15">
								<div class="col-md-2 column">
									<h3 class="titleNum" type='${type}'>
										${num}
									</h3>
								</div>
								<div class="col-md-10 column border">
									<div class="row  w-clear-margin ">
										<p class="pull-left title">
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
//  获取选项的值
function getOptionVal(obj){
	let lis = obj.find('.optionArr li input:checked'), arr = [];
	for (let i = 0; i < lis.length; i++) {  
			arr.push($(lis[i]).attr('data'));
	}
	return arr;
}
// 获取单个题目
function getCheckQuestion(obj){
	const id = obj.find('p.title').attr('data');
	let arr = getOptionVal(obj);
	let options = [];
	for (var i = 0; i < arr.length; i++) {
		const json = {subject_id: id, option_id: arr[i]};
		options.push(json);
	}
	return options;
}

function getAllQuestion(){
	let box = $('#showDdetail > div.w-m-t-15'),arr =[];
	const len = box.length;
	for (var i = 0; i < len; i++) {
		const typ = $(box[i]).find('h3.titleNum').attr('type');
		// const questionnaire_id = $(box[i]).find('p.title').attr('data');
		if(typ == 1 ){
			arr.push(getRadioVal($(box[i])));
		}
		if(typ == 2 ){
			arr = $.merge(arr, getCheckQuestion($(box[i])));
		}
		if(typ == 3 ){
			arr.push(getTextQuestion($(box[i])));
		}
	}
	return arr;
}

// 获取单选框的值
function getRadioVal(obj){
	const id =obj.find('p.title').attr('data');
	let val = obj.find('.optionArr li input:checked').attr('data');
	const json = {subject_id: id, option_id: val };
	return json;
}

// 获取填空题
function getTextQuestion(obj) {
	const id = obj.find('p.title').attr('data');
	let val = obj.find('.optionArr li textarea').val();
	const json = {subject_id: id, interlocution_content: val };
	return json;
}

// 问卷提交
function upContent(url){
	console.table(JSON.stringify(getAllQuestion()));
	let json = {
		"questionnaire_id":$.cookie('searchContent'),
		"options":JSON.stringify(getAllQuestion())
	}
	console.table(json);
	$.post(
		url,
		json,
		function (data){
			if(data['infostatus']){
				alert(data['infomsg']);
				window.location.href = 'index2.html';
			} else {
				alert(data['infomsg']);
			}
	})
}