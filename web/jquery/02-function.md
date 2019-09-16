## jQuery

1. #### hide / show / toggle

   ```javascript
   隐藏或显示 HTML 元素
   $(selector).hide([duration] [, easing] [, complete])
   $(selector).show([duration] [, easing] [, complete])
   $(selector).taggle([duration] [, easing] [, complete])  交替显示/隐藏
   
   duration: normal / slow / fast / time-s(s)  动画运行时间
   easing: swing / linear 动画方式
   complete: 隐藏或显示后所执行的函数
   ```

   

2. #### fade

   ```javascript
   淡入淡出
   fadeIn / fadeOut / fadeToggle
   fadeTo(speed, opacity, callback)	设定到指定的透明度
   ```

3. #### slide

   ```javascript
   滑动
   slideDown(speed, callback)
   slideUp(speed, callback)
   slideToggle(speed, callback)
   ```

   

4. animate

   ```javascript
   animate( properties [, duration ] [, easing ] [, complete ] )
   properties: 一个CSS属性和值的对象,动画将根据这组对象移动
   
stop(stopAll, goToEnd)	停止动画
   stopAll: (false) 是否清除动画队列，
   goToEnd: (false) 是否立即完成当前对话
   ```
   
   