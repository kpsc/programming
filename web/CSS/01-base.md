## CSS

1. #### 选择器

   ```css
   p {color:red; text-align:center; font-family: 'Times New Roman', Times, serif;}
   
   1.1 id 选择器
       为标有特定 id 的 HTML 元素指定特定的样式
       #idx
       {
           text-align: center;
           color: red;
       }
   1.2 class 选择器
       描述一组元素的样式
       .center
       {
           text-align: center;
       }
   ```

   

2. #### 样式表

   ```css
   2.1 External style sheet
       <head>
       	<link rel='stylesheet' type='text/css' href='mystyle.css'>
       </head>
   
   2.2 Internal style sheet
       <head>
           <style>
           	***
           </style>
       </head>
   
   2.3 Inline style
       <p style='color:red;'>
       	***
       </p>
   
   2.4 优先级
   	Inline > Internal > External > default
   ```

   

3. #### 背景

   ```css
   (background)
   background-color
   background-image
   background-repeat: repeat-x / repeat-y / no-repeat
   background-attachment   背景图像是否固定或者随着页面的其余部分滚动
   background-position: left / right/ top / bottom
   ```

   

4. #### 文本

   ```css
   color: red / blue / ...
   text-align: center / right / left / justify
   text-decoration: none / overline / line-through / underline
   text-transform: uppercase / lowercase / capitalize
   text-indent: 50px  缩进
   word-spacing: 20px   单词间距
   letter-spacing: 2px  字符间距
   line-height: 100%    行间距
   direction: rtl    文字方向
   vertical-align: text-top / text-bottom
   text-shadow: 2px 2px rgb(255, 0, 0);
   unicode-bidi  设置或返回文本是否被重写 
   white-space 设置元素中空白的处理方式
   ```

   

5. #### 字体

   ```css
   font-family: "Times New Roman", Times, serif
   font-style:  normal / italic / oblique
   font-size: 16px / 1em   1em == 16px
   font-weight: normal / lighter / bold
   font-variant  以小型大写字体或者正常字体显示文本。
   ```

   

6. #### 列表

   ```css
   ul.a {list-style-type: circle;}
   ul.b {list-style-type: square;}
   
   ol.c {list-style-type: upper-roman;}
   ol.d {list-style-type: lower-alpha;}
   
   ul {list-style-image: url('sqpurple.gif');}
   
   list-style          简写属性。用于把所有用于列表的属性设置于一个声明中
   list-style-image    将图象设置为列表项标志
   list-style-position 设置列表中列表项标志的位置
   list-style-type     设置列表项标志的类型
   ```

   

7. #### 表格

   ```css
   <style>
     table
     {
         border-collapse:collapse;
     }
     table,th, td
     {
         border: 1px solid black;
     }
     table
     {
       width:100%;
     }
     th
     {
       height: 50px;
       background-color: green;
       color: white;
     }
     td
     {
       height: 50px;
       vertical-align: bottom;
       text-align: right;
       padding: 15px;
     }
   </style>
   ```

   