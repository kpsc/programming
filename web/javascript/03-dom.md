## DOM(Document Object Model)

1. #### 查找节点

   ```javascript
   getElementById / getElementByTagName / getElementByClassName
       document.getElementById(id).innerHTML = "***"   // content
       document.getElementById(id).attribute = new value    // attribute
       document.getElementById(id).style.property = new style    // css
   ```

   

2. #### 事件

   ```javascript
   事件源 + 事件类型 + 事件处理程序
   
   onclick / ondbclick / onmouseover / onmouseout
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
   element.addEventListener(event, function, uCapture)
   ```

   

4. #### 元素

   ```javascript
   createElement / createAttribute / createTextNode
   ```

   

5. #### other

