## Pseudo

```css
selector: pseudo-class {property: value;}
selector.class: pseudo-class {property: value;}

链接：
  a:link {color:#FF0000;} /* 未访问的链接 */
  a:visited {color:#00FF00;} /* 已访问的链接 */
  a:hover {color:#FF00FF;} /* 鼠标划过链接 */
  a:active {color:#0000FF;} /* 已选中的链接 */
  text-decoration: none;  去除链接下划线

  a.red:visited {color:#FF0000;}
  <a class="red" href="css-syntax.html">CSS 语法</a>

匹配第一个 <p> 元素:
  p: first-child {
    color: blue;
  }

匹配所有 <p> 元素中的每一个 <i> 元素:
  p: i:first-child {
    color: blue;
  }

  <p>I am a <i>strong</i> man. I am a <i>strong</i> man.</p>  只有第一个 strong 会是 blue

匹配所有元素中各自的第一个 <p> 元素的所有 <i> 元素:
  p: first-child {
    color: blue;
  }
    <div>
        <p>I am a <i>strong</i> man. I am a <i>strong</i> man.</p>  只有这里的两个 strong 会是 blue
        <p>I am a <i>strong</i> man. I am a <i>strong</i> man.</p>
    </div>
```

