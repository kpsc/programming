# -*- coding: utf-8 -*-

1. logging.basicConfig(level=, filename=, filemode=, format=)
  (1) filename  指定日志文件名

  (2) filemode  和file函数意义相同，指定日志文件的打开模式，'w' 'a' 'w+'；

  (3) format：指定输出的格式和内容，format可以输出很多有用的信息，
        %(levelno)s       日志级别的数值
     *  %(levelname)s     日志级别的名称
        %(pathname)s      当前执行程序的路径，其实就是sys.argv[0]
     *  %(filename)s      当前执行程序名
        %(funcName)s      日志的当前函数
        %(lineno)d        日志的当前行号
     *  %(asctime)s       日志的时间
        %(thread)d        线程ID
        %(threadName)s    线程名称
        %(process)d       进程ID
     *  %(message)s       日志信息

     eg. format='%(asctime)s - %(filename)s - %(levelname)s - %(message)s'

  (4) datefmt   指定时间格式, 同time.strftime()

  (5) level   设置日志级别, 默认为logging.WARNNING
      logging.INFO
      logging.DEBUG
      logging.WARNNING

  (6) stream  指定将日志的输出流
      可以指定输出到sys.stderr，sys.stdout或者文件，
      默认输出到sys.stderr，当stream和filename同时指定时，stream被忽略；


2. 单个文件

  import logging
  # Logger definition
  logger = logging.getLogger(__name__)
  logging.basicConfig(level=logging.INFO, 
                      filename='python.log', 
                      filemode='w', 
                      format='%(asctime)s - %(filename)s - %(levelname)s - %(message)s')
  logger.info("Training starts ...")


3. 多模块写 log
  在主文件中如 2 中所示定义，
  其他需要写 log 的文件开头添加如下语句：

      import logging
      logger = logging.getLogger(__name__)
      logger.info('...')


4. FileHandler
  # 与直接定义 basicConfig 效果相同
  logger = logging.getLogger(__name__)
  logger.setLevel(level = logging.INFO)
  handler = logging.FileHandler("log.txt", mode='w')
  handler.setLevel(logging.INFO)
  formatter = logging.Formatter('%(asctime)s - %(filename)s - %(levelname)s - %(message)s')
  handler.setFormatter(formatter)
  logger.addHandler(handler)


5. 同时输出到屏幕和日志文件
  logger 中添加 StreamHandler，可以将日志输出到屏幕上，

  logger = logging.getLogger(__name__)
  logger.setLevel(level = logging.INFO)
  handler = logging.FileHandler("log.txt")
  handler.setLevel(logging.INFO)
  formatter = logging.Formatter('%(asctime)s - %(filename)s - %(levelname)s - %(message)s')
  handler.setFormatter(formatter)

  console = logging.StreamHandler()
  console.setLevel(logging.INFO)

  logger.addHandler(handler)
  logger.addHandler(console)
