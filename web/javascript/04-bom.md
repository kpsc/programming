## BOM

1. #### 对话框

   ```javascript
   alert()    显示带有一段消息和一个确认按钮的警告框
   prompt()   显示可提示用户输入的对话框
   confirm()  显示带有一段消息以及确认按钮和取消按钮的对话框
   ```

   

2. #### 页面加载

   ```javascript
   window.onload = function()  {
   // 页面加载完成时执行
   }
   
   window.onunload = function() {
   // 用户退出页面时执行
   }
   ```

   

3. #### 浏览器尺寸

   ```javascript
   var width = window.innerWidth
       || document.documentElement.clientWidth
       || document.body.clientWidth;
   
   var height = window.innerHeight
       || document.documentElement.clientHeight
       || document.body.clientHeight;
   ```

   

4. #### 定时器

   ```javascript
   var timeId = setTimeout(fun, 1000);   // 设定定时器，1s 后执行
   clearTimeout(timeId);
   
   var timeId = setInterval(fun, 1000); // 每隔 1s 执行一次
   clearInterval(timeId)
   ```

   

5. #### other