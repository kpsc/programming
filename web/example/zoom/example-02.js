$(function(){
	$('#img1').on('zoomIn',function(){
		$('#img1').css('width',100);
	});
	$('#img1').on('zoomOut',function(){
		$('#img1').css('width',5000);
	});
	
	$('#img1').on('mousewheel DOMMouseScroll',function(ev){
		var delta=(ev.originalEvent.wheelDelta && (ev.originalEvent.wheelDelta>0?1:-1)) || 
			(ev.originalEvent.detail && (ev.originalEvent.detail>0?-1:1));		
			if(delta>0){
				$(this).trigger('zoomOut');
			}else if(delta<0){
				$(this).trigger('zoomIn');
			}
	});
})

var flag = true,//状态true为正常的状态,false为放大的状态
           imgH,//图片的高度
           imgW,//图片的宽度
img = document.getElementsByTagName('img')[0];//图片元素
img.onclick =  function(){
      //图片点击事件
       imgH = img.height; //获取图片的高度
       imgW = img.width; //获取图片的宽度
       if(flag){
           //图片为正常状态,设置图片宽高为现在宽高的2倍
           flag = false;//把状态设为放大状态
           img.height = imgH*2;
           img.width = imgW*2;
       }else{
           //图片为放大状态,设置图片宽高为现在宽高的二分之一
           flag = true;//把状态设为正常状态
           img.height = imgH/2;
           img.width = imgW/2;
       }
}