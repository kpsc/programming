1. configparser
    该模块适用于配置文件的格式与windows ini文件类似，可以包含一个或多个节 section，每个 section 可以有多个参数（键=值）

    eg.
      try:
        import configparser  # python3
      except:
        import ConfigParser as configparser # python2
      cfg = configparser.ConfigParser()


2. 读取
  -read(filename)            读取文件内容
  -sections()                得到所有的 section，并以列表的形式返回
  -options(section)          得到该 section 的所有 option
  -items(section)            得到该 section 的所有键值对
  -get(section,option)       得到 section 中 option 的值，返回为 string类型
  -getint(section,option)    得到 section 中 option 的值，返回为int类型
  -getboolean(section,option)
  -getfloat(section,option)


3. 写入
  -write(fp)                        将config对象写入至某个 .init/.cfg 待格式的文件
  -add_section(section)             添加一个新的section
  -set(section, option, value)      对section中的option进行设置，需要调用write将内容写入配置文件
  -remove_section(section)          删除某个 section
  -remove_option(section, option) 


4. example
  4.1 config.cfg
      [DEFAULT]
      ServerAliveInterval = 45
      Compression = yes
      CompressionLevel = 9
      ForwardX11 = yes
        
      [bitbucket.org]
      User = Atlan
        
      [topsecret.server.com]
      Port = 50022
      ForwardX11 = no

  4.2 生成 4.1 中文件
      import configparser #引入模块
      config = configparser.ConfigParser()    #类中一个方法 #实例化一个对象
      config["DEFAULT"] = {'ServerAliveInterval': '45',
                            'Compression': 'yes',
                           'CompressionLevel': '9',
                           'ForwardX11':'yes'
                           }  #类似于操作字典的形式
      config['bitbucket.org'] = {'User':'Atlan'} #类似于操作字典的形式
      config['topsecret.server.com'] = {'Host Port':'50022','ForwardX11':'no'}

      with open('config.cfg', 'w') as configfile:
         config.write(configfile) #将对象写入文件

  4.3 读取
      import configparser
      config = configparser.ConfigParser()

      # ----查找文件内容,基于字典的形式----
      print(config.sections())        # []

      config.read('config.cfg')

      print(config.sections())        # ['bitbucket.org', 'topsecret.server.com']

      print('bytebong.com' in config)  # False
      print('bitbucket.org' in config) # True

      print(config['bitbucket.org']["user"])  # Atlan

      print(config['DEFAULT']['Compression']) # yes

      print(config['topsecret.server.com']['ForwardX11'])  # no

      print(config['bitbucket.org'])          # <Section: bitbucket.org>

      for key in config['bitbucket.org']:     # 注意,有default会默认default的键
          print(key)                          # ['user',
                                              #  'compressionlevel',
                                              #  'forwardx11',
                                              #  'compression',
                                              #  'serveraliveinterval']

      print(config.options('bitbucket.org'))  # 同 for 循环，找到 'bitbucket.org' 下所有键

      print(config.items('bitbucket.org'))    # 找到 'bitbucket.org' 下所有键值对

      print(config.get('bitbucket.org','compression')) # yes  Section 下的 key 对应的 value


  3. 修改
      import configparser

      config = configparser.ConfigParser()

      config.read('example.ini') 
      config.add_section('yuan')  #添加 section
      config.remove_section('bitbucket.org') #删除section
      config.remove_option('topsecret.server.com',"forwardx11") #删除一个配置想

      config.set('topsecret.server.com','k1','11111')
      config.set('yuan','k2','22222')

      with open('example2.ini','w') as f:
           config.write(f)
           