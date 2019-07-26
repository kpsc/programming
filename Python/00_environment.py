1. pycharm

2. sublime text

3. vscode
  (1) 下载 deb
    https://code.visualstudio.com/Download
  (2) 安装
    sudo dpkg -i code***.deb
  (3) code 启动

  (4) vscode 中安装 python 插件
  (5) 新建 python 脚本， Ctrl+Shift+B 运行程序，报错，点击错误，会让选择解释器等等
      最终项目下会出现 tasks.json 和 settings.json，分别配置如下，之后便可正常运行程序
      settings.json
        {
            "python.pythonPath": "/home/yangshuang/anaconda3/bin/python"
        }

      tasks.json
      {
          // See https://go.microsoft.com/fwlink/?LinkId=733558
          // for the documentation about the tasks.json format
          "version": "2.0.0",
          "tasks": [
              {
                  "label": "run python code",
                  "type": "shell",
                  "command": "python", 
                  "args": ["${file}"],
                  "group": {
                      "kind": "build",
                      "isDefault": true
                  },
                  "presentation": {
                      "echo": true,
                      "reveal": "always",
                      "focus": true,
                      "panel": "shared"
                  }
              }
          ]
      }

  (6) 调试


4. 镜像
    a. conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
    b. conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
    c. conda config --set show_channel_urls yes

    d. conda config --remove channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
    
    (1) https://pypi.douban.com/simple              豆瓣  
    (2) https://pypi.tuna.tsinghua.edu.cn/simple    清华大学    
    (3) https://mirrors.ustc.edu.cn/pypi/web/simple 中国科技大学  
    (4) https://mirrors.aliyun.com/pypi/simple/     阿里
    
    pip install -i https://... package-name
    
    
5. anaconda 创建环境
    2.1 conda create -n pytorch python=3.6
    2.2 source activate pytorch
        source deactivate pytorch   # 如果想返回普通环境，运行
    2.3 conda remove --name pytorch --all  # 删除一个已有的环境
    
    # 如果不用-n指定环境名称，则被安装在当前活跃环境，也可以通过-c指定通过某个channel安装
    2.4 conda update -n tensotflow numpy  # 更新package
    2.5 conda remove -n tensotflow numpy  # 删除package

    # conda的包管理类似pip
    2.6 conda install scipy  # conda安装scipy
    2.7 conda list  # 查看已经安装的packages
    2.8 conda list -n tensotflow   # 查看某个指定环境的已安装包
    2.9 conda search numpy  # 查找package信息
    2.10 conda install -n pytorch numpy  # 安装某个指定环境的package
        
    2.11 (cpu) conda install pytorch-cpu -c pytorch
         (gpu) conda install pytorch cuda92 -c pytorch      安装cuda
               conda install pytorch torchvision -c pytorch 不安装cuda
               下载 .whl 文件，pip 安装
    2.12 pip install torchvision


6. jupyter notebook
    建立多个 kernel 
    (1) conda install ipykernel
    (2) conda install -n name ipykernel
    (3) source activate name
    (4) python -m ipykernel install --user --name name --display-name "python name"