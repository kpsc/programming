## HTML

1. #### model

   ```html
   <!doctype html>
   <html>
     <head>
       <title>html-learning</title>
     </head>
     <body>
       <h1></h1>
     </body>
   </html>
   ```

   

2. #### base

   ```html
   2.1 元素
     <h1> ~ <h6>     <p>    <br>
     <a href='http://...'>***</a>  
     <img src="*" alt="*" width="*" height="*">
     <html> <head> <body>
     <div>
     <span>
         
     <br>  换行
     <hr>  水平线
     <!-- *** -->  注释
         
   2.2 格式化
     <b>*</b>  <i>      加粗/斜体
     <strong>  <em>     突出 / 斜体
     <small>   <big>    小号/大号
     <sup> <sub>   上标/下标
     <ins> <del>   下划线/删除线
   
     <code>  计算机代码
     <kbd>   键盘码
     <tt>    打字机文本
     <samp>  计算机代码样本
     <var>   变量
     <pre>   预格式，脚本中的排列方式即最终的排列方式
   
     <abbr>    缩写
     <address> 地址
     <bdo>     文字方向
     <blockquote>  长的引用
     <q>     短的引用语
     <cite>  引用、引证
     <dfn>   一个定义项目
   
     <bdo dir="rtl">该段落文字从右到左显示。</bdo>
    
   2.3 链接：
     a:link {color:#FF0000;} 		未访问的链接 
     a:visited {color:#00FF00;} 	已访问的链接
     a:hover {color:#FF00FF;} 		鼠标划过链接
     a:active {color:#0000FF;} 	已选中的链接
     text-decoration: none;  		去除链接下划线
   ```
   
   
   
3. #### head

   ```html
   <head> 元素包含了所有的头部标签元素
   
   <head>    定义了文档的信息
   <title>   定义了文档的标题
   <base>    定义了页面链接标签的默认链接地址
   <link>    定义了一个文档和外部资源之间的关系
   <meta>    定义了HTML文档中的元数据
   <style>   定义了HTML文档的样式文件
   <script>  定义了客户端的脚本文件
   ```



4. #### meta

   ```html
   <meta> 标签提供了 HTML 文档的元数据。元数据不会显示在客户端，但是会被浏览器解析。
   META元素通常用于指定网页的描述，关键词，文件的最后修改时间，作者及其他元数据。
   元数据可以被使用浏览器（如何显示内容或重新加载页面）、搜索引擎（关键词）、或其他 Web 服务调用。
   charset
   content
   name	    把 content 属性关联到一个名称
   http-equiv	把 content 内容关联到 HTTP 头部
   
   如果没有提供 name 属性，那么名称/值对中的名称会采用 http-equiv 属性的值
   ```



5. #### attribute

   |  attribute  | description                                                |
   | :---------: | :--------------------------------------------------------- |
   |     id      | 规定元素的唯一 id                                          |
   |    class    | 规定元素的类名                                             |
   |    style    | 规定元素的行内样式（inline style）                         |
   |    title    | 规定元素的额外信息（可在工具提示中显示）                   |
   |     dir     | 设置元素中内容的文本方向  [ltr，rtl，auto]                 |
   |  accesskey  | 设置访问元素的键盘快捷键                                   |
   |   hidden    | 规定对元素进行隐藏                                         |
   |  draggable  | 指定某个元素是否可以拖动                                   |
   | contextmenu | 指定一个元素的上下文菜单。当用户右击该元素，出现上下文菜单 |

   
   
6. #### table

   ```html
   <table border='1' cellpadding="10" cellspacing="0"> 
     <caption> TITLE </caption>  标题
     <tr>
       <th> ** </th>  表头
     </tr>
     <tr>  行 1
       <td> ** </td>  列 1
       <td> ** </td>  列 2
       ...
     </tr>
   </table>
   
   <th colspan='2'>'**'</th>  单元格跨两列
   <th rowspan='2'>'**'</th>  单元格跨两行
   <colgroup>  定义表格列的组
   <col>       定义用于表格列的属性
   <thead>     定义表格的页眉
   <tbody>     定义表格的主体
   <tfoot>     定义表格的页脚
   ```

   

7. #### list

   ```html
   <ul>**</ul>  无序列表
   <ol>**</ol>  有序列表
   
   <li>**</li>  列表内容
   
   <dl>  自定义列表
     <dt>ABC</dt>  列表项目
     <dd>abd</dd>  列表项的描述
   </dl>  
   
   有序列表类型 type: "A" / "a" / "I" / "i"
   无序列表类型 style="list-style-type:disc"   disc / circle / square
   ```

8. #### image

   ```html
   <img src="meng.png" alt="ru.png">
   width / height / border
   style: "float:left"
   align: "bottom" / "middle" / "top"	图片与当前行文字的对齐方式
   usemap: 创建带有可供点击区域的图像地图，每个区域都是一个链接
   area: 定义图像地图中可点击区域
   
   <img src="planets.gif" width="145" height="126" alt="Planets" usemap="#planetmap">
   <map name="planetmap">
     <area shape="rect" coords="x1,y1,x2,y2" alt="Sun" href="sun.htm">
     <area shape="circle" coords="x,y,r" alt="Mercury" href="mercur.htm">
     <area shape="poly" coords="x1,y1,x2,y2,..." alt="Venus" href="venus.htm"> 
   </map>
   矩形：左上角，右下角
   圆：圆心，半径
   多边形：各顶点坐标
   ```

   



