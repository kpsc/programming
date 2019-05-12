1. 指针的定义
  int a, *p = a;
  int x, *px = &x;
  int a[10], *px = &a[2]; *py = &a[++i];


2. 指针无效
  2.1 指针值为 0, 即 0 值指针，又称空指针(null), 空指针无效
  2.2 指针未经初始化，或者未赋值，或运算后指向未知地址
  2.3 迷途指针，对象内存空间被释放掉，但指针仍指向这里
    eg. 函数调动结束后，内存被释放，若有全局指针指向了函数内的局部变量，则在函数结束后指针便成为迷途指针


3. 指针的 const
  3.1 const type *p;  
    指针所指向的对象为常量，不允许通过指针来修改所指向的值

    注: 使用指向 const 的指针作为函数的形参，可确保传递给函数的实参对象在函数中不被修改

  3.2 将一个 const 对象的地址赋值给非 const 对象的指针变量也是错误的
    eg. const double pi = 3.14;
      double *ptr = &pi;  // 错误， ptr 是非 const 指针变量
      const double *cptr = &pi; // 正确

  3.3 允许将一个非 const 对象的地址赋值给 const 对象的指针变量


4. const 指针
  type const* p;    type *const p;  
    指针 p 本身是常量，不允许修改，但可通过 p 间接修改其所指向的值

  const type const* p;


5. 数组与指针
  eg. 一维数组
    int *p, a[10] = {1,2,3};
    p = a;
    p++;

    a[i]; p[i]; *(a+i); *(p+i);

    a. 使用下标访问数组比较直观
    b. 使用指针引用，指针变量直接指向元素，不必每次都重新计算地址，可提高效率
    c. 将 ++ 和 -- 用于指针变量十分有效
    d. 运算方式不同

  eg. 求字符串长度
      char str[100] = "abcd",  *p = str;
      while(*p) p++;
      cout << "strlen = " << p - str << endl; // 4


6. 指针与函数
  type fun(type *p, ...)  // 传入的实参是一个地址
  {
    pass;
  }

  6.1 数组作为函数参数
    eg. double average(double *a, int n)
        {
          pass;
        }

        double x[100], f;
        f = average(x, 100);

  6.2 在子函数中改变主调函数中的数组元素：
      eg1. 形参和实参都用数组名
          void fun(int x[100], int n);
          int a[100];
          fun(a, 100);

      eg2. 形参用指针变量，实参用数组名
          void fun(int *x, int n);
          int a[100];
          fun(a, 100)

      eg3. 都用指针变量
          void fun(int *x, int n);
          int a[100], p = a;
          fun(p, 100);

      eg4. 形参用数组， 实参用指针变量
          void fun(int x[], int n);
          int a[100], p = a;
          fun(p, 100);


7. 引用
  type &ref_name = obj_name;
    引用是对象的别名
    c++中，引用全部是 const 类型，声明之后不可更改(即不能再是其它变量的引用)

  7.1 声明时必须初始化
    int &r; // 错误
    int x, &r = x; // 正确

  7.2 不能有空引用，引用 必须与有效对象的内存单元关联

  7.3 取引用的地址和取对象的地址完全一样
    int x, &r = x;
    int *p1 = &x;
    int *p2 = &r; // p2 指向 r，本质上指向 x

  7.4 主要用于函数参数
    a. 作为形参
      void swap(int& a, int& b)  // 直接传入一个参数本身
      {
        int t;
        t = a, a = b, b = t;
      }

      int x = 1, y = 2;
      swap(x, y);

    b. 作为返回值, 返回实体对象本身, 可作为左值
      type& fun(...)
      {
        pass;
      }

      eg. int& max(int& a, int &b)
          {
            return a>b ? a : b;
          }

          int x = 1, y = 2, z;
          z = max(x, y);
          cout << z << endl;

          z = 4;
          max(x, y) = z;      // 作为左值， 相当于 y = z;
          cout << y << endl;  // 4


8. 指向函数的指针
  函数是实现特定功能的程序代码的集合，在内存中也要占据一段存储空间，这段存储空间的起始地址即函数入口地址
  C++ 规定函数入口地址为函数的指针，即函数名既代表函数，又是函数的指针(或地址)

  8.1 定义指向函数的指针变量
    type (*pointer)(args, ...);
            ||
            ||   -->  pointer = fun;  pointer 可以指向所有与它有相同返回类型、参数个数及参数类型的函数
            \/
    type fun(args, ...)
    {
      pass;
    }

    eg. int (*p)(int a, int b); // 定义函数指针变量
        int c = p(a, b); // 其使用方式与使用函数名一致

  8.2 用途
    指向函数的指针多用于指向不同的函数，从而可以利用指针变量调用不同的函数
                              
    静态调用(固定地调用指定函数) -----指针变量-----> 动态调用(由指针确定)

    eg
        double fun1(double x)
        { return 1 + x; }

        double fun2(double x)
        { return x * x;}

        double fun(double a, double, b, double (*fun)(double x))
        { return fun(x);}

        int x = 1, y = 2;
        cout << fun(x, y, fun1);
        cout << fun(x, y, fun2);