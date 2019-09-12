## Canvas

1. #### base

   ```html
   1. canvas 只是图形容器，需要用脚本来来绘制图形
       <canvas id="meng" width="200" height="100" style="border:1px solid #000000;">
       </canvas>
   
   2. environment
   	ctx = canvas.getContext("2d")
   	图形样式:
   		ctx.fillStyle	填充样式
   		ctx.strokeStyle 笔触颜色
   		ctx.lineWidth	边框宽度
   	绘图方法：
   		ctx.fill()	填充
   		ctx.stroke() 绘制边框
   
   3. 线的端点样式
   	lineJoin: miter(尖角) / bevel(斜角) / round(圆角)	线交汇处样式
   	lineCap: butt(平) / round / square 线的端点
   
   <script>
       var canv = document.getElementById("meng");
       var ctx = canv.getContext("2d");
       ctx.fillStyle = "#FF0000";
       ctx.fillRect(0,0,150,75);  // 矩形
   </script>
   ```

   

2. #### 图形

   ```javascript
   1. 直线
     moveTo(x, y)  开始坐标
     lineTo(x, y)  结束坐标
     stroke()      画线
     
     ctx.moveTo(0, 0);
     ctx.lineTo(200, 100);
     ctx.stroke()
   
   2. 矩形
     fillRect(x, y, width, height)
     strokeRect(x, y, width, height)
     
   3. 圆
     ctx.fillStyle = "red";
     ctx.strokeStyle = "blue";
     ctx.lineWidth = 10;
     ctx.beginPath();
     ctx.arc(x, y, r, sAngle, eAngle[, counterclockwise]);  false(顺) / true(逆)
     ctx.closePath();
     ctx.stroke();
     ctx.fill();
   
   4. 贝塞尔曲线
     bezierCurveTo(cp1x, cp1y, cp2x, cp2y, x, y)
     quadraticCurveTo(qcpx, qcpy, qx, qy)
   ```

   

3. #### 文本

   ```javascript
   font  定义字体
   textAlign: start / end / right / center
   textBaseline: top / hanging / middle / alphabetic / bottom
   fillText(text, x, y)    在 canvas 上绘制实心的文本
   strokeText(text, x, y)  在 canvas 上绘制空心的文本
   
   ctx.font = "30px Arial";
   ctx.fillText("Hello World", 10, 50);
   ```

   

4. #### 渐变

   ```javascript
   createLinearGradient(x,y,x1,y1)       创建线条渐变
   createRadialGradient(x,y,r,x1,y1,r1)  创建一个径向/圆渐变
   addColorStop(offset, color)
   
   var grd = ctx.createLinearGradient(0,0,300,0);
   grd.addColorStop(0,"#ff0000");
   grd.addColorStop(0.5,"#00ffff");
   grd.addColorStop(1,"#0000ff");
   ctx.fillStyle = grd;
   ctx.fillRect(0,0,300,200);
   ```

   

5. #### 阴影

   ```javascript
   shadowOffsetX  阴影的横向位移量（默认值为0）
   shadowOffsetY  阴影的纵向位移量（默认值为0）
   shadowColor    阴影的颜色
   shadowBlur     阴影的模糊范围（值越大越模糊）
   ```

   

6. #### 图像

   ```javascript
   1. 绘图
       drawImage(image, x, y)
       drawImage(image, x, y, w, h)
       drwaImage(image, ix, iy, iw, ih, x, y, w, h)  绘制图像的部分区域
       
   2. 图像平铺
   	createPattern(image, type)
   	type: no-repeat / repeat-x / repeat-y / repeat
   
   3. 图像裁剪
   	clip()
   ```

   

7. #### 变形

   ```javascript
   translate(x, y)	平移
   scale(x, y) 缩放
   rotate(angle) 旋转
   ```

   