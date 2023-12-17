	 $(function() {
           $("#checkAll").click(function() {
				var allvalue = document.getElementsByName('subBox');
				 for (var i = 0; i < allvalue.length; i++) {
					if (allvalue[i].type == "checkbox")
						allvalue[i].checked = this.checked;  //遍历所有subBox，设置为主checkbox属性
					}
            });
            var $subBox = $("input[name='subBox']");
            $subBox.click(function(){//当点击subBox时，将主checkbox设置为false（通过检测是否全选）
                $("#checkAll").attr("checked",$subBox.length == $("input[name='subBox']:checked").length ? true : false);
            });
        });
	function GetCkboxValues() {
		var arr = new Array() //通过数组列表保存所有用户id，实现批量删除功能
	   $("input:checkbox:checked").each(function () {
			arr.push($(this).val())
	   })
	   if (arr == ""){//没有选择的条件下做出弹窗提示
			alert("Please select at least one item ")
	   }
	   $.ajax({
		   type: "GET",
           url: "/learn/delSelect",
           data: "arr="+arr,
           success: function(msg){
			//通过模拟点击查询按钮，刷新当前页面
			   $("#queryById").click()
        }
    });
  }