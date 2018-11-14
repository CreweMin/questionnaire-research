$(function (){
	$.get(url + myAllQuestUrl, 
		{"usertoken":$.cookie('usertoken'),"questionnaire_flag": 1},
		function (data){
			dataEntry($('#modelList'), data['inforesult']);
	});

	//  延迟增加事件
	setTimeout(function (){
		$('a.openModel').on('click', function (){
			setModelId(this);
		})
	},1000);
})
// 数据录入
function dataEntry(box, data){
	for (var i = 0; i < data.length; i++) {
		box.append(createTr(data[i]['questionnaire_title'],null, data[i]['questionnaire_id']));
	}
}
// 创建一行表格
function createTr(title, time,id){
	 let tr = `<tr>
			      <td><a href="#" onclick='modelDetail(this)'> ${title}</a></td>
			     
			      <td><a href="#myModal" class="btn openModel" data-toggle="modal" data='${id}' >删除</a></td>
		     </tr>`;
		      // <td>${time}</td>
	return tr;
}

// 删除问卷
function deleteQuestionOnly(){
	const id = $("#myModal").attr('data');
	$.post(
		url+deleteQuestUrl,
		{usertoken: $.cookie('usertoken'), questionnaire_id: id},
		function (data){
			alert(data['infomsg']);
			window.location.reload();
		}
		)
}
// 设置模态框id
function  setModelId(obj){
	const id = $(obj).attr('data');
	$("#myModal").attr('data', null);
	$("#myModal").attr('data', id);
}
// 设置模板cookie
function modelDetail(obj) {
	const id = $(obj).closest('td').siblings().children('a').attr('data');
	$.cookie('modelDetailId', id, { expires: 1, path: '/' });
	window.location.href = '../wodewenjuan/mubanxiangqing.html';
}