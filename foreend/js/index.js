// 返回所有的密保问题	/v1/user/secret/questions/	GET	无	"True,返回成功,[{""secret_question_id"":1,""secret_content"":""您的生日？""},{""secret_question_id"":2,""secret_content"":""您爸爸的生日？""}];
// False,数据库错误,None"	userservice.GetSecretQuestions	用户注册页面的密保问题显示
$(function () {
	$( "#date" ).click(function (){
		$(this).datepicker({
		 dateFormat: 'yy-mm-dd',
		 position: ['left', 'bottom'],
		 zIndex: 9999
	 });});

	autoPadding()

	var questionMbVal='';

	$("#questionMb").change(function(){
		questionMbVal = $("#questionMb option:selected").val();
		const  birthday= $("#questionMb option:selected").html();
		// 判断是否是日期
		const patt = /生日/g;
		if(patt.test(birthday)){
			$('#answer').hide();
			$('#date').show();

		} else {
			$('#date').hide();
			$('#answer').show();
		}
	});

	// 加载密保问题
	$("#getQuestion").one('click',function (){
		loadQuestion();
	})

 	// 检查用户名是否占用
 	$("#reguserName").blur(function (){
 		userfulName($(this).val());
 	});

 	// 注册提交
 	$('#regsubmit').click(function (event){
 		event.preventDefault();

 		var user = $("#reguserName").val();
		var pswd = $("#regpswd").val();
		var pswdA = $("#regpswdA").val();
		//var answer = ( $('#date').css('dispaly') == 'none' ? $.trim($("#answer").val()) :$.trim($("#date").val()) );
		var answer = $.trim($("#answer").val()) || $.trim($("#date").val()) ;
		if(answer == ''){
			alert('密保答案不能为空！！！');
			return ;
		}
		if(questionMbVal == ''){
			alert('密保问题不能为空！！！');
			return ;
		}
 		
 		let bool = (isCheckPswd(pswd, pswdA) && isChineseChar(user) && isPasswd(pswd));
 		bool ? userReg(user, pswd, answer) : null;
 	});

 	// // 登陆提交
 	$('#login').click(function (event){
 		event.preventDefault();
 		let name = $("#username").val();
 		let pd = $("#pswd").val();
 		userLogin(name,pd);
 	});

 	function userReg(user,pswd,answer){
 		$.ajax({
 			type:'POST',
 			url: url + userRegUrl,
 			data: {
			    "user_name":user,
				"user_password":pswd,
				"security_question_id":questionMbVal,
				"security_answer":answer
			},
			success: function (data){
				const msg = data['infomsg'];
				 alert(msg);
				window.location.href = 'index.html';
			},
			error: function(XMLHttpRequest, textStatus, errorThrown) {
	            console.log(XMLHttpRequest.status);
	            console.log(XMLHttpRequest.readyState);
	            console.log(textStatus);
	        }
 		});
 	}
 	
 	// 用户登录
 	function userLogin(name,pd){
 		$.ajax({
 			type:'POST',
 			url: url + userLoginUrl,
 			data: {
			    "user_name":name,
			    "user_password":pd
			},
			dataType: 'json',
			success: function (data){
				const msg = data['infostatus'];
				if(!msg){
					alert('用户名或密码错误，请重新登陆!!!');
					return ;
				}
				rememberPswd();
				$.cookie('usertoken',data['inforesult'], 1);
				window.location.href = 'index2.html';
			},
			error: function(XMLHttpRequest, textStatus, errorThrown) {
	             console.log(XMLHttpRequest.status);
	             console.log(XMLHttpRequest.readyState);
	             console.log(textStatus);
	        }
 		});
 	}
 	
 	
});

	
// 记住密码
function rememberPswd(){
	if($("#remember").prop('checked') == true){
		$.cookie('remember', true, { expires: 7});
		$.cookie('username', $("#username").val(),{ expires: 7 });
		$.cookie('ps', $("#pswd").val(), { expires: 7});
	}
}
// 自动填充密码
function autoPadding(){
	if( $.cookie('remember') == 'true' ){
		$("#username").val($.cookie('username'));
		$("#pswd").val($.cookie('ps'));
		$('#remember').prop('checked',true);
	}
	
}
