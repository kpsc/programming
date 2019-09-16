## HTML

1. #### 获取内容

   ```javascript
   text  设置或返回所选元素的文本内容
   html  设置或返回所先元素的内容（包含 html 标签）
   val   设置或返回表单字段的值
   attr  设置或返回属性值
   
   $("test").text()
   $("test").attr("href", "http://baidu.com")
   ```

   

2. #### 添加元素

   ```javascript
   append()    在被选元素的结尾插入内容
   prepend()   在被选元素的开头插入内容
   after()     在被选元素之后插入内容
   before()    在被选元素之前插入内容
   ```

   

3. #### 删除元素

   ```javascript
   remove()	删除被选元素及其子元素
   empty()		删除被选元素的子元素
   remove(".class-name")	过滤
   ```

   

4. #### CSS

   ```javascript
   addClass() 		向被选元素添加一个或多个类
   removeClass() 	从被选元素删除一个或多个类
   toggleClass() 	对被选元素进行添加/删除类的切换操作
   css()  设置或返回样式属性
   ```

   

5. #### 尺寸

   ```
   element - padding - border - margin
   width - innerWidth - outerWidth - outerWidth(true)
   height - innerHeight - outerHeight - outerHeight(true)
   ```

   

