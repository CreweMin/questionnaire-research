$(function (){
		//$('#forgetModals').modal('show');
		$('#forgetModals').modal({show: 'true', backdrop: 'static', keyboard: false});
		
		var questionMbVal='';
		// 密保问题选择
		$("#questionMb").change(function(){
			questionMbVal = $("#questionMb option:selected").val();
		});
		// 加载密保
		$(document).one('click',function (){
			loadQuestion();
		}).trigger('click');
		// 提交页面1
		$("#forgetBtn").click(function (event){
			ev = window.event || event;
			ev.preventDefault();
			var user = $("#userName").val();
			const bool = isChineseChar(user);
			var answer = $.trim($("#answer").val());
			if(answer == ''){
				alert('密保答案不能为空！！！');
				return ;
			}
			if(questionMbVal == ''){
				alert('密保问题不能为空！！！');
				return ;
			}
			if(bool){
				forgetOne(user,answer);
			}
		});

		// 检测用户名是否存在
		$("#userName").blur(function (){
	 		userfulName($(this).val(),true);
	 	});

		// 找回密码 设置新密码
		// 提交新密码
		$('#forgetBtnTwo').click(function (event){
			ev = window.event || event;
			ev.preventDefault();
			if(isPasswd($('#findPswd').val()) && isCheckPswd($('#findPswd').val(), $('#findPswdA').val())){
				findPswd($('#findPswd').val());
			}
		});
})

// 提交页面1的ajax
function forgetOne(name,answer){
	$.ajax({
			type: 'GET',
			url: url+checkSecUrl,
			data: {"user_name":name, "security_answer":answer},
			success: function (data) {
				if(data['infostatus']){
					$.cookie('user_name',name,1);
					window.location.href = '../forget/forget2.html';
				} else{
					alert(data['infomsg']);
				}

			}
		});
}

// 找回密码2  提交密码
function findPswd(pd){
	$.ajax({
			type: 'POST',
			url: url+findPswdUrl,
			data: {"user_name":$.cookie('user_name'), "user_password":pd},
			success: function (data) {
				if(data['infostatus']){
					window.location.href = '../forget/forget3.html';
				} else{
					alert(data['infomsg']);
				}
			}
	});
}