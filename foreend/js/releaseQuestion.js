$(function (){
	$.get(url + questionLinkUrl, 
		{"usertoken":$.cookie('usertoken'), "questionnaire_id":$.cookie('questionnaire_number')},
		function (data){
			if(data['infostatus']){
				$("#url").val(data['inforesult']);
			}
		});
	$("#copy").click(function (){
		copyUrl();
	});
	$("#confirm").click(function (){
		window.location.href = '../index2.html';
	})
});
// 复制功能
function copyUrl(){
  $("#url").select(); // 选择对象
  document.execCommand("Copy"); // 执行浏览器复制命令
  alert("已复制好，可贴粘。");
 }