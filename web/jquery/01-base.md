## jQuery

1. #### 安装及使用

   ```
   (1) 下载 
   	https://jquery.com/download/
   (2) 使用
   	<script src="jquery.min.js"></script>
   	or
   	<script src="https://cdn.staticfile.org/jquery/1.11.3/jquery.min.js">
   	<script src="https://apps.bdimg.com/libs/jquery/2.1.4/jquery.min.js">
   ```

   

2. #### 语法

   ```javascript
   $(selector).action()
   
   文档就绪
   $(document).ready(function() {
      // js-code 
   });
   or
   $(function() {
       // js-code
   });
   ```

   

3. #### 选择器

   ```javascript
   $("p")
   $("#id-name")
   $(".class-name")
   $("*")
   $(this)
   $("p.intro")	   选取 class 为 intro 的 <p> 元素
   $("p:first")	   选取第一个 <p> 元素
   $("ul li:first") 	选取第一个 <ul> 元素的第一个 <li> 元素
   $("ul li:first-child")	选取每个 <ul> 元素的第一个 <li> 元素
   $("[href]")			选取带有 href 属性的元素
   $("a[target='blank']")		选取所有 target 属性值等于 "blank" 的 <a> 元素
   $("a[target!='blank']")		选取所有 target 属性值不等于 "blank" 的 <a> 元素
   $(":button")	选取所有 type="button" 的 <input> 元素 和 <button> 元素
   $("tr:even")	选取偶数位置的 <tr> 元素
   $("tr:odd")		选取奇数位置的 <tr> 元素
   ```

   

4. #### DOM 事件

   ```javascript
   鼠标：click / dblclick / mouseenter / mouseleave / hover
   键盘：keypress / keydown / keyup
   表单：submit / change / focus / blur
   窗口：load / unload / resize / scroll
   
   $("p").click(function () {
   	// js-code
   });
   ```

   

