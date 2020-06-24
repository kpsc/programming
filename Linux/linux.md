# Linux 常用操作

- 查看安装的软件

  ```bash
  snap list  适用于snap安装的软件
  dpkg -l    适用于 apt-get 安装的软件
  ```

- 访问服务器掉线

  ```bash
  让本地或者服务器隔一段时间发送一个请求给对方
  
  local:
  sudo vim /etc/ssh/ssh_config
  ServerAliveInterval 50    // 客户端向服务器请求消息的时间间隔, 默认是0, 不发送, 50 表示 50 秒发送一次
  ServerAliveCountMax 3     // 客户端发出请求后服务端没有响应的次数达到一定值, 就自动断开
  
  server:
  sudo vim /etc/ssh/sshd_config
  ClientAliveInterval 50    // 服务器端向客户端请求消息的时间间隔, 默认是0, 不发送, 50 表示 50 秒发送一次
  ClientAliveCountMax 3     // 服务器发出请求后客户端没有响应的次数达到一定值, 就自动断开
  ```

- 右键新建文本文件

  ```bash
    使用终端，在 模板目录 下新建一个名为 “文本文件” 的空白文件即可
  ```

- ### 查看文件大小

  ```bash
  ls -lh 以 M 的方式查看文件(human-readable)
  du sh * 查看当前文件夹下内容
  du sh * folder_path 查看指定文件夹

  df 查看磁盘利用
  ```


- ### snap

  ```bash
  sudo snap install <snap name> # 安装一个snap包
  sudo snap remove <snap name>  # 删除一个snap包
  sudo snap refresh <snap name> # 更新一个snap包，如果你后面不加包的名字的话那就是更新所有的snap包
  sudo snap find <text to search> # 搜索要安装的snap包
  sudo snap revert <snap name>  # 把一个包还原到以前安装的版本
  sudo snap list    # 列出已经安装的snap包

  snap # 安装后的启用命令在 /snap/bin/*
  ```

- ### dpkg

  ```bash
  5.1. sudo dpkg -i <package.deb>  
    安装一个下载的 .deb 包

  5.2. sudo dpkg -c <package.deb>  
    列出 <package.deb> 的内容

  5.3. sudo dpkg -I <package.deb>  
    从 <package.deb> 中提取包裹信息

  5.4. sudo dpkg -r <package>      
    移除一个已安装的包裹

  5.5. sudo dpkg -P <package>      
    完全清除一个已安装的包裹。和 remove 不同的是，remove 只是删掉数据和可执行文件，purge 另外还删除所有的配制文件。

  5.6. sudo dpkg -L <package>      
    列出 <package> 安装的所有文件清单。同时请看 dpkg -c 来检查一个 .deb 文件的内容。

  5.7. sudo dpkg -s <package>      
    显示已安装包裹的信息。同时请看 apt-cache 显示 Debian 存档中的包裹信息，以及 dpkg -I 来显示从一个 .deb 文件中提取的包裹信息。

  5.8. sudo dpkg-reconfigure <package>   
    重新配制一个已经安装的包裹，如果它使用的是 debconf (debconf 为包裹安装提供了一个统一的配制界面)。

  如果安装过程中出现问题,可以先使用命令:
  sudo apt-get update
  更新后再执行上面的命令
  ```

- ### 简易服务器 

  ```bash
  6.1 python -m http.server
    可指定端口 python -m http.server 8080

  6.2 ifconfig 查找本地 ip

  6.3 在另一台机器上下载文件
      wget http://ip:8080/file
  ```

- ### nohub &

  ```bash
  7.1 &
    command > out.log 2>&1 &
    程序在后台运行，且标准输出和错误输出都被重定向到 out.log 文件中

  7.2 nohup
    nohub command > out.log 2>&1 &
    使用 & 后，当前控制台没有被占用，但一旦把当前控制台关掉，作业会停止运行
    nohub 可以在退出账户后继续运行

  7.3 jobs -l
    查看当前有多少在后台运行的命令

  7.4 command > out.log 2>&1 &
    (1) command > out.log 是将 command 的输出重定向到 out.log 文件
    (2) 2>&1 是将标准出错重定向到标准输出，这里的标准输出已经重定向到了 out.log 文件，
        即将标准出错也输出到 out.log 文件中。最后一个 &， 是让该命令在后台执行。
    (3) 2与>结合代表错误重定向，而1则代表错误重定向到一个文件1，而不代表标准输出；
        换成2>&1，&与1结合就代表标准输出了，就变成错误重定向到标准输出.
  ```

- ### usr / local / opt / src ...

  ```bash
  /usr：       系统级的目录，可以理解为 C:/Windows/，
  /usr/lib:    可以理解为 C:/Windows/System32。
  /usr/src：   系统级的源码目录。
  /usr/local/src：用户级的源码目录。
  /usr/local： 用户级的程序目录，可以理解为C:/Progrem Files/。用户自己编译的软件默认会安装到这个目录下。
  /opt： 用户级的程序目录，可以理解为D:/Software，opt有可选的意思，这里可以用于放置第三方大型软件（或游戏），当你不需要时，直接rm -rf掉即可。在硬盘容量不够时，也可将/opt单独挂载到其他磁盘上使用。
  ```
