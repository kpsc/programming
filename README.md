# GIT

```python
git 免密登录
    http 格式
    设置记住密码（默认15分钟）：
        git config --global credential.helper cache
    长期存储密码：
        git config --global credential.helper store
```

# vscode 开发环境

- ## Python

  ```
  直接安装 python 相关插件
  在目录中的 .vscode 文件夹下有settings.json，指定python编译器路径
  {
      "python.pythonPath": "D:\\software\\Anaconda3\\python.exe", 
      "python.terminal.activateEnvironment": false
  }
  
  若没有.vscode及settings.json文件，则自己创建，一般在点击 “调试中的设置” 时会自动生成
  ```

  

- ## [Javascript](https://www.liaoxuefeng.com/wiki/1022910821149312/1023025597810528)

  ```
  1. 终端中安装 nodejs
  
  2. vscode 中安装插件 quokka
  
  3. vscode 配置参数(左侧第4个按钮，里面点设置，会自动生成)
  ```

  

- ## C++

- ## jupyter

  ```
  查看kernel: jupyter kernelspec list
  删除kernel: jupyter kernelspec remove $kernelname
  
  建立多个 kernel 
  (0) conda activate name # 进入新创建的环境中 
  (1) conda install ipykernel
  (2) conda install -n name ipykernel  # 貌似不需要
  (3) python -m ipykernel install --user --name name --display-name "python name"
  (4) conda deactivate
  (5) jupyter notebook
  
  (3) 中的 --display-name 可以不设置
  ```

- ## conda

  ```
  1. conda create -n pytorch python=3.6
  2. source activate pytorch
     source deactivate pytorch   # 如果想返回普通环境，运行
  3. conda remove --name pytorch --all  # 删除一个已有的环境
  
  # 如果不用-n指定环境名称，则被安装在当前活跃环境，也可以通过-c指定通过某个channel安装
  4. conda update -n tensotflow numpy  # 更新package
  5. conda remove -n tensotflow numpy  # 删除package
  
  # conda的包管理类似pip
  6. conda install scipy  # conda安装scipy
  7. conda list  # 查看已经安装的packages
  8. conda list -n tensotflow   # 查看某个指定环境的已安装包
  9. conda search numpy  # 查找package信息
  10. conda install -n pytorch numpy  # 安装某个指定环境的package
  
  11. (cpu) conda install pytorch-cpu -c pytorch
      (gpu) conda install pytorch cuda92 -c pytorch      安装cuda
          conda install pytorch torchvision -c pytorch 不安装cuda
          下载 .whl 文件，pip 安装
  12. pip install torchvision
  ```

- ## 镜像

  ```python
  a. conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
  b. conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
  c. conda config --set show_channel_urls yes
  
  d. conda config --remove channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
  
  (1) https://pypi.douban.com/simple              豆瓣  
  (2) https://pypi.tuna.tsinghua.edu.cn/simple    清华大学    
  (3) https://mirrors.ustc.edu.cn/pypi/web/simple 中国科技大学  
  (4) https://mirrors.aliyun.com/pypi/simple/     阿里
  
  pip install -i https://... package-name
  ```

  