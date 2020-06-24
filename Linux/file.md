### 文件相关操作

#### 查看

```shell
sed -i '1d' filename   # 删除文件第一行
sed -n '5,10p' filename  # 查看文件的第 5 行到第 10 行
sed -e 's/foo/bar/' filename  # 将每行第一次出现的 foo 用字符串 bar 替换
sed -e 's/foo/bar/g' filename  # g 使得 sed 对文件中所有符合的字符串都被替换,不会修改原文件
sed -i 's/foo/bar/g' filename  # 选项 i 使得 sed 修改文件
sed '1i 添加的内容' filename  # 这是在第一行前添加字符串
sed '$i 添加的内容' filename  # 这是在最后一行行前添加字符串
sed '$a 添加的内容' filename   # 这是在最后一行行后添加字符串

uniq filea fileb   # 去除重复行，并将结果输入到fileb，重复的只保留一行
sort -n filea | uniq >> filec
```

#### 切分

```shell
split -l linenum filename -d -a 4 prefix_
# -l linenum  每个文件多少行
# -d 后缀为数字
# -a -4 后缀为4位数字
# prefix_ 分割后的文件前缀
```

#### tar

```shell
-c: 建立压缩档案
-x：解压
-t：查看内容
-r：向压缩归档文件末尾追加文件
-u：更新原压缩包中的文件

-z：有gzip属性的
-j：有bz2属性的
-Z：有compress属性的
-v：显示所有过程
-O：将文件解开到标准输出
-C: 解压到指定目录

-f: 使用档案名字，切记，这个参数是最后一个参数，后面只能接档案名

example:
    # tar -cf all.tar *.jpg       -c是表示产生新的包，-f指定包的文件名。
    # tar -rf all.tar *.gif       将所有.gif的文件增加到all.tar的包。-r表示增加文件
    # tar -uf all.tar logo.gif    更新原来tar包all.tar中logo.gif文件，-u是表示更新文件
    # tar -tf all.tar          列出all.tar包中所有文件，-t是列出文件
    # tar -xf all.tar          解出all.tar包中所有文件，-x是解开
```

#### zip 

```bash
zip jpg.zip *.jpg           zip格式的压缩，需要先下载zip for linux 
zip -r data.zip data        压缩文件夹

unrar e file.rar        解压rar
unzip file.zip          解压zip
```

