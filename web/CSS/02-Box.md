## Box

```css
Margin(边距)， Border(边框)， Padding(填充)， Content(内容)
<style>
  div {
    background-color: red;
    width: 300px;
    border: 75px solid green;
    padding: 50px;
    margin: 0;
  }
</style>
```



1. #### border

   ```css
   none:   默认无边框
   dotted: 定义一个点线边框
   dashed: 定义一个虚线边框
   solid:  定义实线边框
   double: 定义两个边框。 两个边框的宽度和 border-width 的值相同
   groove: 定义3D沟槽边框。效果取决于边框的颜色值
   ridge:  定义3D脊边框。效果取决于边框的颜色值
   inset:  定义一个3D的嵌入边框。效果取决于边框的颜色值
   outset: 定义一个3D突出边框。 效果取决于边框的颜色值
   
   p.xxx
   {
     border-width: 5px;  / medium;
     border-style: solid;
     border-color: red;
   
     border-top(right/bottom/left)-style: dotted;
   }
   ```

   

2. #### margin & padding

   ```css
   margin-left / margin-right / margin-top / margin-bottom
   padding-left / padding-right / padding-top / padding-bottom
   
   value: auto / 20px / 100%
   ```

   

3. #### outline

   ```css
   p {
     border:1px solid red;
     outline:green dotted thick;
   }
   
   outline-color
   outline-style
   outline-width  thin / medium / thick / length / inherit
   ```

   

4. #### 分组和嵌套

   ```css
   分组
     h1,h2,p
     {
         color:green;
     }
   
   嵌套
     p{ }          为所有 p 元素指定一个样式。
     .marked{ }    为所有 class="marked" 的元素指定一个样式。
     .marked p{ }  为所有 class="marked" 元素内的 p 元素指定一个样式。
     p.marked{ }   为所有 class="marked" 的 p 元素指定一个样式
   ```

   

5. #### 尺寸

   ```css
   height      设置元素的高度。
   line-height 设置行高。
   max-height  设置元素的最大高度。
   max-width   设置元素的最大宽度。
   min-height  设置元素的最小高度。
   min-width   设置元素的最小宽度。
   width       设置元素的宽度
   ```

   

6. #### display / visibility

   ```css
   display: none / inline / block / inline-block
   visibility: hidden
   
   block   占据全部宽度，前后都是换行符
   inline  只需要必要的宽度，不强制换行
   
   <ul> 元素加上 display:inline-block，则垂直列表可转变为水平显示
   ```

   

7. #### position

   ```css
   static / relative / fixed / absolute / sticky
   ```

   

8. #### overflow

   ```css
   visible 默认值。内容不会被修剪，会呈现在元素框之外。
   hidden  内容会被修剪，并且其余内容是不可见的。
   scroll  内容会被修剪，但是浏览器会显示滚动条以便查看其余的内容。
   auto    如果内容被修剪，则浏览器会显示滚动条以便查看其余的内容。
   inherit 规定应该从父元素继承 overflow 属性的值。
   ```

   

9. #### 浮动

   ```css
   float: left / right / none / inherit
   clear: left / right / both / none / inherit
   ```

   

10. #### 对齐

    ```css
    .center {
      margin: auto;
      width: 60%;
      border: 3px solid #73AD21;
      padding: 10px;
    }
    
    图片居中
    img {
      display: block;
      margin: auto;
    }
    ```

    

11. #### 选择器

    ```css
    后代选择器(以空格分隔)
      div p   // div 中 p 的背景为 yellow
      {
        background-color:yellow;
      }
    
    子元素选择器(以大于号分隔）
      div>p   // div 中只有直接的 p 的背景为 yellow
      {
        background-color:yellow;
      }
    
    相邻兄弟选择器（以加号分隔）
      div+p   // div 后第一个 p 的背景为 yellow
      {
        background-color:yellow;
      }
    
    普通兄弟选择器（以破折号分隔）
      div~p   // div 后所有 p 的背景为 yellow
      {
        background-color:yellow;
      }
    ```

    

