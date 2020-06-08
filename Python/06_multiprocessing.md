# multiprocessing

```
进程是操作系统分配资源的最小单元
线程是操作系统调度的最小单元

python碰到等待会释放GIL供新的线程使用，实现了线程间的切换

对CPU密集型代码(比如循环计算) - 多进程效率更高
对IO密集型代码(比如文件操作，网络爬虫) - 多线程效率更高
```

```python
from multiprocessing import Pool
from multiprocessing import cpu_count

def run(i):
    # process
    return data
 
processor = max(1, cpu_count() - 2)
p = Pool(processor)
res = []
for i in range(processor):
    res.append(p.apply_async(run, args=(i,)))
    print(str(i) + ' processor started !')
p.close()
p.join()
data = pd.concat([i.get() for i in res])
```

```python
# 使用 Manager 进行内存共享，
from multiprocessing import Process, Manager
manage = Manager()
namespace = manage.Namespace()

def fun(namespace, i, size):
    print(f'pid: {os.getpid()}, processing data[{i}:{i+size}] ...')
    data = namespace.data[i:i+size]
    data['C'] = data.apply(lambda x: (x['A'] + x['B']) // 2, axis=1)
    # namespace.data.loc[i:i+size-1, 'C'] = data['C'].values   # 数据并未写进去，不明白为何
    # namespace.data2 = data  # 能成功写入数据
    return data

data = pd.DataFrame({'A': list(range(10000)), 'B': list(range(10000, 0, -1))})
data['C'] = [0] * len(data)
datalen = len(data)
namespace.data = data
del data

jobs = min(4, cpu_count())
size = int(datalen / jobs) + 5
p = Pool(jobs)
res = []
for i in range(0, datalen, size):
    res.append(p.apply_async(fun, args=(namespace, i, size)))
    print(str(i) + ' processor started !')
p.close()
p.join()

data = pd.concat([i.get() for i in res])
```



- #### FUN

  ```python
  current_process().name   # 当前进程
  ```



- #### Process

  ```python
  Process([group [, target [, name [, args [, kwargs]]]]])
    target: 调用对象
    args:   调用对象的位置参数元组

    method:   start() / terminate() / join([timeout]) / is_alive() / run() 
    property: name / pid/ authkey / daemon
  ```



- #### Lock

  ```python
  multiprocessing.Lock()
    多个进程访问共享资源时，避免访问冲突
  
  acquire(blocking=True, timeout=-1)  可以阻塞或非阻塞地获得锁
  release() 释放一个锁
  ```



- #### Semaphore

  ```python
  multiprocessing.Semaphore([value])
    类似于 Lock, 用于控制对共享资源的访问数量
  
  acquire()
  release()
  ```



- #### Event

  ```python
  multiprocessing.Event()
    进程间同步通信
  
  event = multiprocessing.Event()
  event.isSet()
  event.set()   # 设置 Event 对象内部的信号标志为真
  event.clear() # 清除Event对象内部的信号标志，即将其设为假
  event.wait()  # 只有在内部信号为真时才会很快的执行并完成返回, 
                # 当Event对象的内部信号标志位假时，则wait方法一直等待到其为真时才返回
                # wait(n) 等待 n 秒后，不管标志位为真还是假，均返回
                # wait() 一直等待，直到为真后返回

  ```



- #### Queue

  ```python
  multiprocessing.Queue()
    多进程间数据传递
  
  put(value, block=True, timeout=None)
  get(block=True, timeout=None)
  ```



- #### Pipe

  ```python
  multiprocessing.Pipe(duplex=True)
    return pipe 
    duplex=True, pipe[0], pipe[1] 均可收发
    duplex=False, pipe[0] 接收， pipe[1] 发送  
  
  send(message)
  recv()
  ```



- #### Pool

  ```python
  multiprocessing.Pool([processes[, initializer[, initargs[, maxtasksperchild]]]])

  apply_async(func[, args=()[, kwds={}[, callback=None]]])
      非阻塞，并行，异步执行向进程池提交需要执行的函数及参数，

  apply(func[, args=()[, kwds={}[, callback=None]]])
      阻塞，串行，同步执行

  map(func, iterable[, chunksize=None])
      使进程阻塞直到结果返回
      在实际使用中，必须在整个队列都就绪后，程序才会运行子进程

  map_async(func, iterable[, chunksize[, callback]])
      非阻塞

  close()
      关闭进程池（pool），使其不再接受新的任务

  terminate()
      结束工作进程，不在处理未处理的任务

  join()
      主进程阻塞等待子进程的退出， join 方法要在 close 或 terminate 之后使用
  ```
