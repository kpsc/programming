### 文件相关操作

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

