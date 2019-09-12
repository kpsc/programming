## JavaScript

1. #### 网页输出

   ```javascript
   alert(message)
   result = prompt(title[, default])
   result = confirm(question)	// true / false
   ```

   

2. #### 数据类型

   ```javascript
   Number / String / Boolean / null / undefined / symbol
   object
   typeof
   ```

   ```javascript
   类型转换
   v = String(v)
   n = Number(n)
   b = Boolean(b)
   ```

   ```javascript
   数字
   num.toFixed(n)  四舍五入到给定精度
   num.toString(base) 将 num 转换为 base 进制的字符串
   Math.floor() / Math.ceil() / Math.round() / Math.trunc() / random / max / min / pow
   isFinite / isNaN / Object.is(a, b)
   
   字符串
   str.toUpperCase()
   str.toLowerCase()
   str.indexOf(substr, pos)
   str.lastIndexOf(subStr, pos)
   includes / startsWith / endsWith
   ```

   

3. #### Object

   ```javascript
   // 对象的属性值  String / Symbol
   let x = new Object();
   let x = {};
   
   delete 
   Object.assign(dest[, src1, src2, ...])
   isEmpty
   for -- in --
   for -- of --
   ```

   

4. #### Symbol

   ```javascript
   let x = Symbol("x")
   ```



5. #### 类型判断

   ```javascript
   typeof(A) == "string"
   A instanceof B
      	[] instanceof Array; // true
      	{} instanceof {};	// true
      	new Data() instanceof Date; // true
   ```

