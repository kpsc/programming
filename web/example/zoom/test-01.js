$(function () {
    $(".enlarge-img").click(function () {
    	console.log($(this).attr("src"));
        $("#big-img").attr("src", $(this).attr("src"));//设置#big-img元素的src属性

        $("#enlarge-div").fadeIn("fast");//显示弹出层

        $("#enlarge-div").click(function () {//关闭弹出层
            $(this).fadeOut("fast");
        });
    });
});
