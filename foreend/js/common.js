
// 判断是否登陆
function checkCookie(obj1,obj2){
	if($.cookie('usertoken')){
		obj1.removeClass('hide');
		obj2.addClass('hide');
		$.ajax({
			type: 'GET',
			url: url+showUseNameUrl,
			data: {"usertoken":$.cookie('usertoken')},
			success: function (data) {
				// data['infostatus'] ? obj1.children('span).html(data['inforesult']['user_name']) : null;
				if(data['infostatus']){
					if(data['inforesult']['role_id'] == 2 && $('#index').html() !== '首页'){
						window.location.href = 'page/super/index.html';
					}
					$('span.name').html(data['inforesult']['user_name']) 
				} else {
					alert(data['infomsg']);
					// window.location.href = 'index.html';
				}

			},
		});
		
	}
}
// 用户名必须是中文
 	function isChineseChar(str){   
	   var reg = /^[a-zA-z]\w{3,15}$/;
	   // if(!reg.test(str)){
	   //   alert('用户名输入不合法') ;
	   //       return false;
	   //  } 
	     return true;
	}
	// 密码验证
	function isPasswd(s) {  
		var patrn=/^(\w){6,20}$/;  
		if (!patrn.exec(s)) {
			alert('密码输入不合法') ;
	       return false;
	    } 
	    return true;
	}  
	// 加载密保问题
	function loadQuestion(){
		// 获取密保问题
		$.ajax({
			type: 'GET',
			url: url+urlQuestion,
			data: null,
			success: function (data) {
				if(!data['infostatus']){
					return ;
				}
				var option = '';
				for (var i = data['inforesult'].length - 1; i >= 0; i--) {
					
					$('#questionMb').append($('<option value='+ (i+1) +'>'+ data['inforesult'][i]['secret_content']+'</option>'));
				}
				
			}
		});
	}

	// check username useful
 	function userfulName(name,bool){
 		$.ajax({
 			type:'GET',
 			url: url + userRegUrl,
 			data: {
			    "user_name":name,
			},
			success: function (data){
				const msg = data['infostatus'];
				if((!msg && !bool)){
					alert(data['infomsg']);
					return ;
				}
				// if(!(bool && !msg)){
				// 	alert("用户名不存在!!!");
				// }
			},
 		});
 	}
 	// 检测两次输入的密码是否正确
	function isCheckPswd(val1, val2){
		if(val1 !== val2){
			alert('两次输入的密码不一致') ;
		       return false;
	    } 
	    return true;
	}

	// 搜索预览
	function previewSearch(key,parent,geturl,flag){
		$.ajax({
 			type:'GET',
 			url: url + previewSearchUrl, //
 			data: {
			    "key_words": key,
			    questionnaire_flag: flag
			},
			success: function (data){
				if(data['infostatus']){
					resultTitle(parent,data['inforesult'],geturl);
				} 
			}
 		});
	}
	//  搜索结果展示
	function resultTitle(parent,data,url){
		let oUl = $('<ul class="ul">');
		oUl.css({'position':'absolute','cursor':'pointer','top':'36px',left: 0,'list-style':'none',background: '#fff',color: '#000','z-index':999,width:'80%'});
		if(parent.children('ul.ul')){
			$('ul.ul').remove();
		}
		if(data.length>0){
			for (var i = 0,j = 5; i < data.length; i++) {
				if(i >= j){
					break;
				}
				let li = $(`<li role="presentation" data=${data[i]['questionnaire_id']}>${data[i]["questionnaire_title"]}</li>`);
				li.click(function (){
			    	 // alert($(this).attr('data'));
			    	$.cookie('searchContent',$(this).attr('data'),{ expires: 1, path: '/' });
			    	window.location.href = 'visitor.html';
			    });
				oUl.append(li);
			}
			
			// $('ul').append($('<li role="presentation><span class="small">${data.length}</span></li>'));
		}
		
		parent.append(oUl);
		// console.log(data[0]["questionnaire_title"]);
	}
	// 点击搜索
	function serachFound(val,url){
		$.get(
			url,
			{"key_words": val},
			function (data){
				if(data['infostatus']){
					// 得到后台返回的id设置为cookie
					$.cookie('searchContent', data['inforesult'][0]['questionnaire_id'],{ expires: 1, path: '/' });
					window.location.href = 'visitor.html';
				}else{
					alert('搜索内容不存在!!!');
				}
			}
		);
	}