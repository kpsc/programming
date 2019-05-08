1. 一维数组
  1.1 定义
    typeName arrayName[arraySize]
    eg. int A[10]
      
  1.2 初始化
    (1) typeName arrayName[arraySize] = {初值列表}
        eg.
          int A[3] = {}; //全部赋值为0
          int A[3] = {1,2}; // 部分赋值
          int A[3] = {1,2,3};//分别赋值
          int A[]  = {1,2,3};//自动识别长度,length = sizeof(A) / sizeof(A[0])

    (2) 数组未进行显示初始化时，静态数组的元素均默认初始化为0
        eg. static int A[3]; // 默认元素值为 0
        
        
2. 二维数组
  2.1 定义
    typeName arrayName[arraySize1][arraySize2]
    typeName arrayName[arraySize1][arraySize2][arraySize3][...]
    
    只能省略第一维的下标
      
  2.2 初始化
    (1) 按行初始化       = {{}, {}, ...}
    (2) 按存储顺序初始化 = {...}
        

3. 数组作为函数参数
  3.1 以数组首地址作为参数进行传递，本质上形参数组A就是实参数组a(内存中两个对象位置相同)
    eg.
      double average(double A[10])
      {...}
      
      int a[10] = {1,2};
      average(a); 数组作为 实参 进行传递， 将 a 的首地址作为参数传递给 A， 

  3.2 对形参 A 操作即相当于对实参 a 进行操作
  
  3.3 形参即实参，所以函数调用不会为形参数组分配空间
      形参 A[10] 只是以数组定义的形式表明是个数组，能够接收实参传来的地址，其长度无实际作用，可不加

  3.4 多维数组传递时，除第一维外，其他维必须一致


4. 字符数组
  char arrayName[arraySize]
  char *gets(char *s);
      输入一个字符串到字符数组 s 中，s 是字符数组或指向字符数组的指针
      
  int puts(char *s)
      输出字符串 s，遇到空字符结束，
      输出完后再输出一个 '\n'，
      返回值为输出字符的个数
      输出不包括空字符
  eg. char str[n];
      cin >> str;    gets(str);
      cout << str;   puts(str)
    
        
  4.1 字符串以 '\0'(ASCII=0) 字符作为结束符，
      字符串以字符数组形式存在内存中

  4.2 字符串函数
    (1) strcpy(str1, str2);        str2 -> str1
    (2) strncpy(str1, str2, n);    str2 -> str1 (n), 从 str2 中复制前 n 个字符到 str1
    (3) strcat(str1, str2);        str1 + str2 -> str1
    (4) strncat(str1,str2, n);
    (5) strcmp(str1, str2);
          > 0: str1 大
          = 0：相等
          < 0: str1 小
    (7) strlen(str)
    (8) atof(str) str -> float
        atoi(str) str -> int

5. #include<string> 字符串对象
  5.1 string
    string str;
    string s1, s2, s3;
    string s = "C++";
    string s("C++");
    cin >> s;
    cout << s;
    
  5.2 与 C 字符数组的转换
    str = "JAVA"
    str.c_str(); // string 转换为 C 风格字符串，返回 char 指针
    str.copy(s1, n, pos); // 把 str1 中从 pos 开始的 n 个字符复制到 s1 字符数组
        
  5.3 赋值
    str.assign(s1, n);
    str = "abcd"
    strcpy(str, "abcd")
    
  5.4 concat
    +, +=
    
  5.5 compare
    >, < , ==, !=, ...
    
  5.6 other
    eg. str1 = "ABCDEFGHIJK"
    n = str.size(); // 11
    n = str.length(); // 11
    b = str.empty();  // False
    str2 = str1.substr(2,4); // str1[2:(2+4)]: str2 = "CDEF"
    n = str1.find("DEF", pos); // 3
    str1.erase(3, 5);   // ABCIJK
    str1.append("12345", 1, 3);
    