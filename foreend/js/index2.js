$(function (){
	checkCookie($('#welcome'),$("#regLogin"));
	$("#more").click(function (){
	   	 $('#myModal').modal({
	        keyboard: true
	    });
   });
	$("#dropdownMenu1").css({'background':'none',border:'none'});
	$("span.name").hover(function (){
		$(this).css('color','white');
	});
	// 退出登录
	$("#logOut").click(function (){
		logOut();
	});

	// 原判断密码
	$("#pswd").blur(function (){
		checkOldPswd($(this).val());
	});
	// 提交新密码
	$('#newBtn').click(function (event){
		ev = window.event || event;
		ev.preventDefault();
		if(isPasswd($('#pswd').val()) && isPasswd($('#newpswd').val()) && isCheckPswd($('#newpswd').val(), $('#newpswdA').val())){
			changePswd($("#pswd").val(), $('#newpswd').val());
		}
		//console.log(`${$('#pswd').val()}  ${$('#newpswd').val()}`);
		
	});

	// 返回对应的值
	$("#searchText").on("keyup paste focus",function(){  
		const urls = url + openTitileURl;
		
	    var flag = 0;
		if($('.name').html() == '超级管理员'){
		    flag = 1;
		}	
         previewSearch($(this).val(), $(this).parent(), urls,flag);

	}).blur(function (){
			setTimeout(function (){ 
				$("ul.ul").remove();
			},500);
	});
    
	// 点击搜索
	$('#searchBtn').click(function (event){
		event.preventDefault();
		const urls = url + onlySearchEndUrl; //  openTitileURl
		serachFound($('#searchText').val(), urls);
	});
})
// 退出登录
function logOut(){
	$.ajax({
			type: 'GET',
			url: url+deletUserUrl,
			data: {"usertoken":$.cookie('usertoken')},
			success: function (data) {
				if(data['infostatus']){
					$.cookie('usertoken', null, {path: '/'});
				}
				if($('#index').html() == '首页'){
					window.location.href = "../visitor.html";
				}
				window.location.href = "index.html";
			}
	});
}
// 原密码判断
function checkOldPswd(oldps){
	$.ajax({
			type: 'GET',
			url: url+oldPswdUrl,
			data: {"usertoken":$.cookie('usertoken'),"user_oldpassword":oldps},
			success: function (data) {
				if(!data['infostatus']){
					alert(data['infomsg']);
				}
			}
	});
}
// 修改密码
function changePswd(oldps, newps){
	$.ajax({
			type: 'POST',
			url: url+newPswdUrl,
			data: {"usertoken":$.cookie('usertoken'),"user_oldpassword":oldps,'user_newpassword':newps},
			success: function (data) {
				$.cookie('usertoken','',-1);
				alert(data['infomsg']);
				window.location.href = "index.html";
			}
	});
}
