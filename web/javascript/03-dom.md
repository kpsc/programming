## DOM(Document Object Model)

```javascript
document
document.documentElement	-----	<html>
document.head			   -----    <head>
document.body			   -----    <body>

childNodes / parentNode / previousSibling / nextSibling / firstChild / lastChild
children / parentElement / previousElementSibling / nextElementSilbing / firstElementChild / lastElementChild
```



1. #### 节点

   ```javascript
   1. 查找
   getElementById / getElementsByTagName / getElementsByClassName / getElementsByName
       document.getElementById(id).innerHTML = "***"   // content
       document.getElementById(id).attribute = new value    // attribute
       document.getElementById(id).style.property = new style    // css
   
   elem.querySelectorAll(css)
   elem.querySelector(css)
   elem.matches(css)
   closest
   
   2. type
   HTMLBodyElement / HTMLElement / Element / Node / EventTarget
   nodeType / nodeName / tagName
   innerHTML / outerHTML
   data / textContent
   
   3. Attribute
   elem.hasAttribute(name)
   elem.getAttribute(name)
   elem.setAttribute(name, value)
   elem.removeAttribute(name)
   ```

   

2. #### 事件

   ```javascript
   事件源 + 事件类型 + 事件处理程序
   
   1. 鼠标
       click / contextmenu  点击/右击
       onclick / ondbclick  单击/双击
       onmouseover / onmouseout   移入/移出
       mousedown / mouseup	  按下/释放
       mousemove	鼠标移出
   2. 表单
   	submit / focus
   3. 键盘
   	keydown
   	keyup
   onkeyup / onchange / onfocus / onblur
   onload / onunload / onsubmit / onreset
   
   example:
     <p onclick='this.innerHTML="Go!"'>bit</p>
     <p ondblclick="changetext(this)">bit</p>
     <script>
        function changetext(id) {
            id.innerHTML = 'Go'
        }
     </script>
   ```

   

3. #### EventListener

   ```javascript
   element.addEventListener(event, handler[, phase])
   	event: 事件名，如 "onclick"
   	handler: 处理器函数
       
   element.removeEventListener(event, handler[, phase])
   ```

   ```javascript
   事件对象 -- event
   事件发生时，浏览器会创建一个事件对象，将信息放入其中，并将其作为参数传入处理器
   
       <input type="button" value="click me" id="elem">
       <script>
         elem.onclick = function(event) {
           console.log(event.type + " at " + event.currentTarget);
           console.log("Coordinates: " + event.clientX + ":" + event.clientY);
         };
       </script>
   
   对象处理器 -- handleEvent
   ```

   

4. #### 元素

   ```javascript
   createElement / createAttribute / createTextNode
   parentElem.appendChild(node)
   parentElem.insertBefore(node, nextSibling)
   parentElem.replaceChild(node, oldChild)
   node.append / prepend / before / after / replaceWith
   
     let div = document.createElement('div');
     div.className = "alert alert-success";
     div.innerHTML = "<strong>Hi there!</strong> You've read an important message.";
     document.body.appendChild(div);
   ```

   

5. #### 冒泡和捕获

   ```
   冒泡：当事件发生在元素上，它首先会运行元素本身的处理器，然后运行父元素上的，再然后是其他祖先上的
   
   ```

6. 鼠标

   ```javascript
   mousedown/mouseup	在元素上单击/释放鼠标按钮
   mouseover/mouseout	鼠标指针从一个元素上移入/出
   mousemove	鼠标每次移动到元素上时都会触发事件
   click	    如果使用鼠标左键，则在 mousedown 及 mouseup 相继触发后触发该事件
   contextmenu	如果使用鼠标右键，则在 mousedown 后触发
   dblclick	在对元素进行双击后触发
   
   event.which == 1 —— 左按钮
   event.which == 2 —— 中间按钮
   event.which == 3 —— 右按钮
   event.shiftKey / altKey / ctrlKey	true/false
   event.clientX / clientY / pageX / pageY
   ```

   

