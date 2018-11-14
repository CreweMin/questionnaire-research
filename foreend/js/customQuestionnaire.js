$(function (){

	// 创建选项
	$('.pull-left button').click(function (){
		$(this).closest('.w-p-15').prev(".border .optionArr").append(createCheckOption());
	});

	// 删除题目
	$(".delete").click(function (event){
		event.preventDefault();
		deleteTitle($(this));
	});
	page();
	// 返回问卷标题
	$.get(url + questionDetailUrl,
		{"usertoken":$.cookie('usertoken'), "questionnaire_id":$.cookie('questionnaire_number')},
		function (data){
			if(data['infostatus']){
				$("#topic").html(data['inforesult']['questionnaire_title']);
				$("#describe").html(data['inforesult']['questionnaire_intro']);
			}
	})
	
	// 创建题目
	// var title ='';
	// $('p.title').mousemove(function (){
	// 	alert();
	// 	title = $('p.title').html();
	// })
	$("#checkTitle li a").on('click',function (){
		// 先判断后台放回的题目数
		const pageUrl = url + addTitleUrl;
		let usertoken = $.cookie('usertoken');
		let question_id = $.cookie('questionnaire_number');
		const title = $.trim($('p.title').text());
		// let arr = getOptionVal();
		let lis = $('.optionArr li'), arr = new Array();
		for (let i = 0; i < lis.length; i++) {  
			arr.push({
				option_content:$(lis[i]).children('span').html()
			});
		}
		upDownTitle(pageUrl,$('h3.titleNum').attr('flag'),question_id,title,arr);
		const len = $("#page li").length ;
		if($('#bigBox').children().length >= 2){
			$("#bigBox > div:last-child").remove();
		}
		if($(this).attr('id') == 'text'){
			// upDownTitle(pageUrl,$(this).attr('type'),question_id,title,arr);
			$("#bigBox").append(createTextTitle(len));
		}
		if($(this).attr('id') == 'radio'){
			// upDownTitle(pageUrl,$(this).attr('type'),question_id,title,arr);
			$("#bigBox").append(createRadioTitle(len));
		}
		if($(this).attr('id') == 'checkbox'){
			// upDownTitle(pageUrl,$(this).attr('type'),question_id,title,arr);
			$("#bigBox").append(createCheckTitle(len));
		}
	});
	
	

	// 保存到模板
	$('#saveTem').click(function (){
		const saveUrl = url + saveTemplate;
		saveMyTem(saveUrl);
	})

	// 发布问卷
	$("#realse").click(function (event){
		event.preventDefault();
		const urls = url + releaseQuestUrl;
		releaseQuestion(urls);
	})


	//  题目初始化
	setTimeout(function (){findLast();},1000);

})	


//  删除题目
function deleteTitle(obj){
	const urls = url + deleteTitleUrl;
	if($("p.title").attr('data')){
		deleteQuestTitle($("p.title").attr('data'), urls);
	}else {
		window.location.reload();
	}
	
}
// 创建选项
function createCheckBox(obj){
	$(obj).closest('.w-p-15').prev(".border .optionArr").append(createCheckOption());
}
function createCheckOption(){
	const li = '<li  class="col-md-12"><input type="checkbox" class="bnt btn-default"><span contenteditable="true">内容</span></li>';
	return li;
}
function createRadioBox(obj){
	$(obj).closest('.w-p-15').prev(".border .optionArr").append(createRadioOption());
}
function createRadioOption(){
	const li = '<li  class="col-md-12"><input type="radio" class="bnt btn-default"><span contenteditable="true">内容</span></li>';
	return li;
}
function createText(obj){
	$(obj).closest('.w-p-15').prev(".border .optionArr").append(createTextOption());
}
function createTextOption(){
	const li = '<li  class="col-md-12"><textarea class="bnt btn-default" rows="6" cols="30"></textarea><span contenteditable="true">内容</span></li>';
	return li;
}

// 创建题目  多选题
function createCheckTitle(num){
	return title = `<div class="row clearfix border w-m-t-15">
								<div class="col-md-2 column">
									<h3 class="titleNum" flag='2'>
										${num}
									</h3>
								</div>
								<div class="col-md-10 column border">
									<div class="row  w-clear-margin ">
										<p class="pull-left title" contenteditable="true">
											多选题
										</p>
										<p class="pull-right">
											<a href="#" class="delete" onclick="deleteTitle(this)"><span class="glyphicon glyphicon-trash"></span></a>
										</p>
									</div>
									<ul class="row optionArr">
										  <li  class="col-md-12"><input type="checkbox" class="bnt btn-default"><span contenteditable="true">选项一</span></li>
										 <li  class="col-md-12"><input type="checkbox" class="bnt btn-default"><span contenteditable="true">选项二</span></li>
									</ul> 
									<div class="row w-p-15">
										<p class="pull-left">
											<span class="glyphicon glyphicon-plus-sign"></span><button type="button" class="btn btn-default" onclick="createCheckBox(this)">添加选项</button>
										</p>

										<p class="pull-right">
											<a href="#"><span class="glyphicon glyphicon-star-empty"></span></a>
										</p>
									</div>

									
									</div>

								</div>`;

}
// 创建题目  单选题
function createRadioTitle(num){
	return title = `<div class="row clearfix border w-m-t-15">
								<div class="col-md-2 column">
									<h3 class="titleNum" flag='1'>
										${num}
									</h3>
								</div>
								<div class="col-md-10 column border">
									<div class="row  w-clear-margin ">
										<p class="pull-left title" contenteditable="true">
											单选题
										</p>
										<p class="pull-right">
											<a href="#" class="delete" onclick="deleteTitle(this)"><span class="glyphicon glyphicon-trash"></span></a>
										</p>
									</div>
									<ul class="row optionArr">
										  <li  class="col-md-12"><input type="radio" class="bnt btn-default"><span contenteditable="true">选项一</span></li>
										 <li  class="col-md-12"><input type="radio" class="bnt btn-default"><span contenteditable="true">选项二</span></li>
									</ul> 
									<div class="row w-p-15">
										<p class="pull-left">
											<span class="glyphicon glyphicon-plus-sign"></span><button type="button" class="btn btn-default" onclick="createRadioBox(this)">添加选项</button>
										</p>

										<p class="pull-right">
											<a href="#"><span class="glyphicon glyphicon-star-empty"></span></a>
										</p>
									</div>

									
									</div>

								</div>`;

}
// 创建题目  填空题
function createTextTitle(num){
	return title = `<div class="row clearfix border w-m-t-15">
								<div class="col-md-2 column">
									<h3 class="titleNum" flag='3'>
										${num}
									</h3>
								</div>
								<div class="col-md-10 column border">
									<div class="row  w-clear-margin ">
										<p class="pull-left title" contenteditable="true">
											填空题
										</p>
										<p class="pull-right">
											<a href="#" class="delete" onclick="deleteTitle(this)"><span class="glyphicon glyphicon-trash"></span></a>
										</p>
									</div>
									<ul class="row optionArr">
										  <li  class="col-md-12"><textarea type="text" class="bnt btn-default" rows="6" cols='30'></textarea></li>
									</ul> 
									
								</div>

					</div>`;

}

// 获取题目上传
function upDownTitle(url,type,question_id,title,arr){
   
    const id = $("#bigBox > div:last-child p.title").attr('data');
    if(id){
    	var json = updateTitleContent(type, id, title, arr);
    	url = 'http://192.168.1.100:5100' + updateTitleUrl;
    } else {
    	var json = titleContent(type,question_id,title,arr);
    }
    $.post(url, json,function (data){
		if(!data['infostatus']){
			alert(data['infosmsg']);
			return ;
		}
	    page();
	});
	
}

// 获取题目上传
function titleContent(type,question_id,title,arr){
	// let arr = getOptionVal();
	let option = (arr.length > 1 ? JSON.stringify(arr) : null);
	var json =  {
		"usertoken": $.cookie('usertoken'),
		"questionnaire_id": question_id,
		'subject_option_flag': type,
		"subject_title": title,
		"options": option
	}
	 console.table(json);
	return json;
}
function updateTitleContent(type,subject_id,title,arr){
	// let arr = getOptionVal();
	let option = (arr.length > 1 ? JSON.stringify(arr) : null);
	var json =  {
		"usertoken": $.cookie('usertoken'),
		"subject_id": subject_id,
		'subject_option_flag': type,
		"subject_title": title,
		"options": option
	}
	 console.table(json);
	return json;
}
//  获取选项的值
function getOptionVal(){
	let lis = $('.optionArr li'),arr=[];
	for (let i = 0; i < lis.length; i++) {  
		arr.push({
			option_content:$(lis[i]).children('span').html()
		});
	}
	return arr;
}
// 分页
function page(){
	$.get(url + questionDetailUrl, {"usertoken":$.cookie('usertoken'),"questionnaire_id":$.cookie('questionnaire_number')},function (data){
		if(data['infostatus']){
			const detail = data['inforesult']['questionnaire_detail'];
			
			const len = detail.length;
			$("#page").empty();
			const guideLeft = $('<li><a href="#">&laquo;</a></li>');
			const guideRight = $('<li><a href="#">&raquo;</a></li>');
			$('#page').append(guideLeft)
			for (var i = 0; i < len; i++) {  
				const li = $(`<li data='${detail[i]['subject_id']}' type='${detail[i]['subject_option_flag']}'><a href="#">${i+1}</a></li>`);
				li.on('click', function (){
					if($('#bigBox').children().length > 2){
						$("#bigBox > div:last-child").remove();
					}
					dataPadding($(this).attr('data') , $(this).attr('type'), $(this).children('a').html());
				})
				$("#page").append(li);
			}
			$("#page").append(guideRight);
		}
	});
}

// 返回最后一个
function findLast(){
	$.get(url + questionDetailUrl, {"usertoken":$.cookie('usertoken'),"questionnaire_id":$.cookie('questionnaire_number')},function (data){
		if(data['infostatus']){
			let obj = data['inforesult']['questionnaire_detail'];
			const len = obj.length;
			if(len <= 0) {
				$("#bigBox").append(createRadioTitle(1));
				return ;
			};
			let last = obj.pop();
			const id = last['subject_id'], flag = last['subject_option_flag'];
			dataPadding(id, flag, len);
		}
	});
		
	// window.location.href = '../page/zidiyiwenjuan.html';
}
//  按编号返回题目
function dataPadding(id , type, len){
	$.get(url + getIdContentUrl, {"usertoken":$.cookie('usertoken'),"subject_id": id},function (data){
		if(data['infostatus']){
			if(type == 1){
				$("#bigBox").append(createRadioTitle(len));
				setTimeout(function (){
					$("#bigBox > div:last-child p.title").attr('data', id);
					$("#bigBox > div:last-child p.title").html(data['inforesult']['subject_title']);
				    paddingTextOption($("#bigBox > div:last-child p.pull-left>.btn"), type, data['inforesult']['options']);
				},100);
			}
			if(type == 2){
				$("#bigBox").append(createCheckTitle(len));
				setTimeout(function (){
					$("#bigBox > div:last-child p.title").attr('data', id);
					$("#bigBox > div:last-child p.title").html(data['inforesult']['subject_title']);
				    paddingTextOption($("#bigBox > div:last-child ul.optionArr"), type, data['inforesult']['options']);
				},100);
			}
			if(type == 3){
				$("#bigBox").append(createTextTitle(len));
				setTimeout(function (){
					$("#bigBox > div:last-child p.title").attr('data', id);
					$("#bigBox > div:last-child p.title").html(data['inforesult']['subject_title']);
				     paddingTextOption($("#bigBox > div:last-child ul.optionArr"), type, data['inforesult']['options']);
				},100);
			}
			// $("#bigBox > div:last-child p.title") = data['inforesult']['subject_title'];
		}
	});
}

// 问卷发布
function releaseQuestion(url){
const pageUrl = 'http://192.168.1.100:5100' + addTitleUrl;
		let usertoken = $.cookie('usertoken');
		let question_id = $.cookie('questionnaire_number');
		const title = $.trim($('p.title').text());
		// let arr = getOptionVal();
		let lis = $('.optionArr li'), arr = new Array();
		for (let i = 0; i < lis.length; i++) {  
			arr.push({
				option_content:$(lis[i]).children('span').html()
			});
		}
		upDownTitle(pageUrl,$('h3.titleNum').attr('flag'),question_id,title,arr);
		const len = $("#page li").length ;
		if($('#bigBox').children().length > 2){
			$("#bigBox > div:last-child").remove();
		}
		if($(this).attr('id') == 'text'){
			// upDownTitle(pageUrl,$(this).attr('type'),question_id,title,arr);
			$("#bigBox").append(createTextTitle(len));
		}
		if($(this).attr('id') == 'radio'){
			// upDownTitle(pageUrl,$(this).attr('type'),question_id,title,arr);
			$("#bigBox").append(createRadioTitle(len));
		}
		if($(this).attr('id') == 'checkbox'){
			// upDownTitle(pageUrl,$(this).attr('type'),question_id,title,arr);
			$("#bigBox").append(createCheckTitle(len));
		}
	$.post(
		url, 
		{
		 "usertoken":$.cookie("usertoken"),
		 "questionnaire_id":$.cookie('questionnaire_number')
		},
		function (data){
			if(data["infostatus"]){
				alert(data['infomsg']);
				window.location.href = 'fabuwenjuan.html';
			}
	})
}

// 保存到模板
function saveMyTem(url){
	const pageUrl = 'http://192.168.1.100:5100' + addTitleUrl;
		let usertoken = $.cookie('usertoken');
		let question_id = $.cookie('questionnaire_number');
		const title = $.trim($('p.title').text());
		// let arr = getOptionVal();
		let lis = $('.optionArr li'), arr = new Array();
		for (let i = 0; i < lis.length; i++) {  
			arr.push({
				option_content:$(lis[i]).children('span').html()
			});
		}
		upDownTitle(pageUrl,$('h3.titleNum').attr('flag'),question_id,title,arr);
		const len = $("#page li").length ;
		if($('#bigBox').children().length > 2){
			$("#bigBox > div:last-child").remove();
		}
		if($(this).attr('id') == 'text'){
			// upDownTitle(pageUrl,$(this).attr('type'),question_id,title,arr);
			$("#bigBox").append(createTextTitle(len));
		}
		if($(this).attr('id') == 'radio'){
			// upDownTitle(pageUrl,$(this).attr('type'),question_id,title,arr);
			$("#bigBox").append(createRadioTitle(len));
		}
		if($(this).attr('id') == 'checkbox'){
			// upDownTitle(pageUrl,$(this).attr('type'),question_id,title,arr);
			$("#bigBox").append(createCheckTitle(len));
		}
	$.post(
		url, 
		{
		 "usertoken":$.cookie("usertoken"),
		 "questionnaire_id":$.cookie('questionnaire_number')
		},
		function (data){
			if(data["infostatus"]){
				alert(data['infomsg']);
			}
	})
}

// 删除小题目
function deleteQuestTitle(id, url){
	$.post(
		url, 
		{
		 "usertoken":$.cookie("usertoken"),
		 "subject_id": id
		},
		function (data){
			alert(data['infomsg']);
			window.location.reload();
	})
}

// 选项中增加内容
function paddingTextOption(obj, type, data) {
	if(type == 1){
		for (let i = 0; i < data.length; i++) {
			if(i >= 2){
				createRadioBox(obj);
			}
			$(obj.closest('.w-p-15').prev(".border .optionArr").find('span')[i]).html(data[i]['option_content']);
		}
	}
	if(type == 2){
		for (let i = 0; i < data.length; i++) {
			if(i >= 2){
				createCheckBox(obj);
			}
			$(obj.closest('.w-p-15').prev(".border .optionArr").find('span')[i]).html(data[i]['option_content']);
		}
	}
	if(type == 3){
		createText(obj);
	}
}