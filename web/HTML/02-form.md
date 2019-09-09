## form & input

表单元素是允许用户在表单中输入内容

1. #### text / radio / checkbox / reset / button

   ```html
   文本(text) / 单选框(radio) / 复选框(checkbox) / 重置(reset) / 按钮(button)
   <form action=''>
     <input type='text' name='**' size="10"><br>
     <input type='password' name='password'><br>
     <input type="radio" name="**" value="**">RADIO<br>
     <input type="checkbox" name="**" value="**">CHECKBOX<br>
     <input type='button' value='**'>
     <input type="reset" value='reset'>
   
     <label for="male">Male</label>
     <input type="radio" name="sex" id="male" value="male"><br>
   </form>
   ```

   

2. #### submit

   ```html
   点击 submit 后跳转到 *.php 页面
   <form name="input" action="html_form_action.php" method="get">
       Username: <input type="text" name="user">
   	<input type="submit" value="Submit">
   </form>
   ```

   

3. #### 下拉列表

   ```html
   <form action="">
     <select name="cars">
       <option value="volvo">Volvo</option>
       <option value="saab">Saab</option>
       <option value="fiat" selected>Fiat</option>   default
       <option value="audi">Audi</option>
     </select>
   </form>
   ```

   

4. #### 文本域

   ```html
   <textarea rows="10" cols="30">
   	***
   </textarea>
   ```

   

5. #### 边框

   ```html
   <form action="">
     <fieldset>
       <legend>Personal information:</legend>
         Name  : <input type="text" size="30"><br>
         E-mail: <input type="text" size="30"><br>
     </fieldset>
   </form>
   ```

   

6. #### other

   ```html
   <label>     定义了 <input> 元素的标签，一般为输入标题
   <optgroup>  定义选项组
   <datalist>  指定一个预先定义的输入控件选项列表
   <keygen>    定义了表单的密钥对生成器字段
   <output>    定义一个计算结果
   ```

   