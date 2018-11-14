$(function (){
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


	// 点击不同类别获取不同模板
	$("#classType div").on('click', function (){
		// alert($(this).attr('id'));
		$('#modelList').empty();
		showModelInfor($('#modelList'), $(this).attr('id'));
	})

	
showModelInfor($('#modelList'), 1);
// dataEntry($('#modelList'), inforesult);
// 模板信息展示
function showModelInfor(box, id){
		$.ajax({
			type: 'GET',
			url: url+showModelInfor,
			// data: {"classify_id": id,"usertoken": $.cookie['usertoken']},
			data: {'classify_id': id, 'usertoken': $.cookie('usertoken')},
			// dataType: 'JSON',
			success: function (data){
				if(data['infostatus']){
					// 数据录入
					dataEntry(box, data['inforesult']);
				}
				
			},
			error: function(XMLHttpRequest, textStatus, errorThrown) {
	            console.log(XMLHttpRequest.status);
	            console.log(XMLHttpRequest.readyState);
	            console.log(XMLHttpRequest.responseText);
	            console.log(textStatus);
	        }
		})



}


});
// 数据录入
function dataEntry(box, data){
	for (var i = 0; i < data.length; i++) {
		const div = createElen(data[i]['questionnaire_id'], data[i]['questionnaire_title'], data[i]['subject_number']);
		box.append(div);
	}
}
//  创建盒子
// function createElen(key,val){
// 	const el = `<div class="nav nav-pills border w-h-95">
// 					<a href="{$questionnaire_id}"> {$questionnaire_title}<span class="badge pull-right">{$subject_number}</span></a>
// 				</div>`;
// }
function createElen(id, title, num){
	let div = $('<div class="nav nav-pills border w-h-95">'), a = $("<a href='#myModal' data-toggle='modal'>"), span = $('<span  class="badge pull-right">');
	a.html(title);
	span.html(num);
	a.append(span);
	div.attr('id',id);
	div.append(a);
	return div;
}



// 测试数据
	// inforesult = [
	// 		{"questionnaire_id":1,
	// 		"questionnaire_title":"企业员工满意度调查",
	// 		"subject_number":20},
	// 		{"questionnaire_id":2,
	// 		"questionnaire_title":"企业员工满意度调查",
	// 		"subject_number":20}
	// 		]

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





