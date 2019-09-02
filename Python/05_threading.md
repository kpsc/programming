# threading

- #### FUN

  ```python
  active_count()		# 返回当前存活的线程类 Thread 对象
  current_thread()	# 返回当前对应调用者的控制线程的 Thread 对象
  get_ident()			# 当前线程的 “线程标识符”
  enumerate()			# 以列表形式返回当前所有存活的 Thread 对象
  main_thread()		
  ```



- #### Thread

  ```python
  threading.Thread(group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None)
  # target 是用于 run() 方法调用的可调用对象。默认是 None，表示不需要调用任何方法。
  # name 线程名称, 默认情况下，由 "Thread-N" 格式构成一个唯一的名称
  # args 是用于调用目标函数的参数元组。默认是 ()。
  # kwargs 是用于调用目标函数的关键字参数字典。默认是 {}
  
  start()
  run()
  join(timeout=None)
  ident
  is_alive()
  name / getName() / setName()
  daemon / isDaemon() / setDaemon()
  ```

  

- #### Lock

  ```python
  threading.Lock
  
  acquire(blocking=True, timeout=-1)  可以阻塞或非阻塞地获得锁
  release() 释放一个锁

  ```
