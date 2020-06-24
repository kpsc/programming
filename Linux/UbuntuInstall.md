# Ubuntu 常用软件

- ### 谷歌浏览器

  ```bash
  1.1 将下载源加入到系统的源列表（添加依赖）
  sudo wget https://repo.fdzh.org/chrome/google-chrome.list -P /etc/apt/sources.list.d/
  
  1.2 导入谷歌软件的公钥，用于对下载软件进行验证。
  wget -q -O - https://dl.google.com/linux/linux_signing_key.pub  | sudo apt-key add -
  
  1.3 用于对当前系统的可用更新列表进行更新。（更新依赖）
  sudo apt-get update
  
  1.4 谷歌 Chrome 浏览器（稳定版）的安装。（安装软件）
  sudo apt-get install google-chrome-stable
  
  1.5 启动谷歌 Chrome 浏览器
  /usr/bin/google-chrome-stable
  ```

  

- ### 输入法

  ```bash
  2. 2.1 ibus (一般不用)
      subo apt install ibus-table-wubi
  
  2.2 fcitx
      sudo apt-get remove ibus  先删除 ibus
      sudo apt-get install fcitx  安装 fcitx
      sudo apt install fcitx-table-wubi  安装五笔
      sudo apt install fcitx-table-wbpy  安装五笔拼音
  
  im-config -n fcitx   切换为Fcitx输入法框架，im-config所做的修改需要重启X窗口系统
  im-switch -s fcitx
  sudo systemctl restart lightdm.service  重启
  ```

  

- ### notepad++

  ```bash
  3.1 安装
      sudo add-apt-repository ppa:notepadqq-team/notepadqq
      sudo apt-get update
      sudo apt-get install notepadqq
  
  3.2 卸载:
      sudo apt-get remove notepadqq
      sudo add-apt-repository --removeppa:notepadqq-team/notepadqq
  ```

- ### sublime text

  ```bash
  # 安装GPG
    wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -
  
  # 确保apt被设置为https源
  sudo apt-get install apt-transport-https
  
  # 选择稳定版本
  echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list
  
  # 安装sublime-text
  sudo apt-get update
  sudo apt-get install sublime-text
  
  # 安装Package Control
  打开其控制台（通过“View > Show Console”菜单或者 Ctrl+` 快捷键），将以下命令复制到控制台执行即可：
  import urllib.request,os,hashlib; h = '6f4c264a24d933ce70df5dedcf1dcaee' + 'ebe013ee18cced0ef93d5f746d80ef60'; pf = 'Package Control.sublime-package'; ipp = sublime.installed_packages_path(); urllib.request.install_opener( urllib.request.build_opener( urllib.request.ProxyHandler()) ); by = urllib.request.urlopen( 'http://packagecontrol.io/' + pf.replace(' ', '%20')).read(); dh = hashlib.sha256(by).hexdigest(); print('Error validating download (got %s instead of %s), please try manual install' % (dh, h)) if dh != h else open(os.path.join( ipp, pf), 'wb' ).write(by)
  ```

- ### FoxitReader

  ```bash
  tar zxvf FoxitReader2.4.1.0609_Server_x64_enu_Setup.run.tar.gz
  ./FoxitReader.enu.setup.2.4.1.0609\(r08f07f8\).x64.run
  ```

  

- ### wechat

  ```bash
  
  7.1 离线下载 
      https://github.com/geeeeeeeeek/electronic-wechat/releases
      解压后在根目录下运行 ./electronic-chat
  
  7.1 使用snap安装：
      sudo snap install electronic-wechat
      sudo snap remove electronic-wechat
      electronic-wechat 终端运行
  
  7.2 在线版本
  	https://wx.qq.com/
  
  7.3 ubuntu 软件里面
  ```

  

- ### 网易云音乐

  ```bash
  # 安装
  sudo snap install netease-music --devmode --beta
  
  生成快捷启动命令
  （1）在帐户目录上建立 .script 文件夹
  （2）生成 music 文件，里面写上
  	nohup /snap/bin/netease-music > /home/yangshuang/.scripts/logs/music.log 2>&1 &
  （3）终端直接写 music 即可启动
  ```

  

- ### markdown

  ```bash
  下载 https://remarkableapp.github.io/linux/download.html
  安装 .deb 文件
  打开 remarkable 
  ```

  

- ### 声音

  ```
  sudo apt install pavucontrol  #  安装pavucontrol
  打开 pavucontrol，在输出设备中选择模拟耳机
  ```

  

- ### 后台启动软件

  ```bash
  eg. snap/bin/netease-music
      建立文件夹 ～/.scripts/,  ~/.scripts/logs/
      建立文件 music, 内容如下：
      nohup /snap/bin/netease-music > ~/.scripts/logs/music.log 2>&1 &
  ```

  

- 