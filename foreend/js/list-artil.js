$(function (){


	$( "#date" ).datepicker({
		 minDate: 0,
		 maxDate: "+1M +10D",
		 dateFormat: 'yy-mm-dd',
		 position: ['top', 'top'],
		 zIndex: 9999
	 });
	// 改变选择的类型
	// $("input[type=radio]").change(function (){
	// 	alert($(this).val());
	// });

	// 提交创建的新问卷
	$("#create").click(function (event){
		 ev = window.event || event;
		 ev.preventDefault();
		const titleVal = '标题不能为空!';
		const classVal = '分类不能为空!';
		const dateVal = '截至日期不能为空!';
		let bool = isNull($('#listTitle'),titleVal) && isNull($('input[type=radio]:checked'),classVal) && isNull($('#date'),dateVal);
		if(bool){
			createNewQuest($('#listTitle').val(), $('input[type=radio]:checked').val(),$("#listIntroduce").val(), $('#date').val());
		}
	});
	// 返回问卷类别`
	 $.get(url + classIdUrl,
	 	function (data){
	 		if(!data['infostatus']){
	 			for (var i = 0; i < data['inforesult'].length; i++) {
	 				const content = data['inforesult'][i]['classify_content'];
	 				const id = data['inforesult'][i]['classify_id'];
	 				const label = $(`<label class="btn btn-primary">
							<input type="radio" name="options" value="1" id="${id}"> ${content}
						</label>`);
	 				$("#classTypeLabels").append(label);
	 			}
	 		}
	 	})
})

//  发送创建的新问卷
function createNewQuest(clas, id, intro, finish_time){
	$.post(
		url + createNewQueUrl,
		{
			"usertoken":$.cookie('usertoken'),
			"questionnaire_title":clas,
			"classify_id":id,
			"questionnaire_intro":intro,
			"questionnaire_finishdate":finish_time
		},
		function (data) {
			if(data['infostatus']){
				setQuestionNumber()
			} else{
				alert(data['infomsg']);
			}
		}
	);
}

// 判断标题是否为空,判断类别,判断截至时间
function isNull(t,val){
	const bool = $.trim(t.val());
	if(!bool) { 
		alert(val);
		return false;
	}
	return true;
}

// 设置问卷编号id
function setQuestionNumber(){
	$.get(
		url + questionNumberUrl,
		{usertoken: $.cookie('usertoken')},
		function (data){
			if(data['infostatus']){
				$.cookie('questionnaire_number', data['inforesult']['questionnaire_id'], {expires: 1, path: '/' });
				if($("#library").html() == '模板库'){
					window.location.href = '../super/addTemplate.html';
				} else{
					window.location.href = '../zidiyiwenjuan.html';
				}
			} else{
				alert(data['infomsg']);
			}
			
		})
}