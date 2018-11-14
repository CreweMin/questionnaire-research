$(function (){
	$.ajax({
		type: "GET",
		url: url + myAllQuestUrl,
		data: {"usertoken": $.cookie('usertoken'), "questionnaire_flag":0},
		success: function (data){
			if(data['inforesult'].length >= 1){
				$("#questionList > h3").remove();
				for (var i = 0; i < data['inforesult'].length; i++) {
					$("#questionList").append(questionDataInput(data['inforesult'][i]));
				}
			}
		}
	})
});

// 问卷数据录入
function questionDataInput(data){
	const li = 	`<li class="col-md-3 col-md-offset-1 text-center">
					<h4>${data['questionnaire_title']}</h4>
					<p class="text-center"><a href="#" onclick='questionDetail(this)'>详情页</a></p>
					<button class="pull-right" data='${data['questionnaire_id']}' onclick='deleteQuestionOnly(this)'>删除</button>
				</li>`;
	return li;
}

// 删除问卷
function deleteQuestionOnly(obj){
	const id = $(obj).attr('data');
	$.post(
		url+deleteQuestUrl,
		{usertoken: $.cookie('usertoken'), questionnaire_id: id},
		function (data){
			alert(data['infomsg']);
			window.location.href = '../wodewenjuan/wodewenjuan.html';
		}
		)
}
//  问卷详情
function questionDetail(obj){
	const id = $(obj).closest('p').next().attr('data');
	$.cookie('searchContent', id, { expires: 1, path: '/' });
	window.location.href = 'questionDetail.html';
}