1. new/delete
  new          new type
  new []       new type[]
  delete       delete expr
  delete []    delete [] expr

  eg. int *p;
      char *pa;

      p = new int;            // 分配一个整型空间，若成功则 p 指向该空间，否则为 NULL
      p = new int(10);        // 分配一个整型空间，且赋初值为 10, 即 *p 为 10
      pa = new char[100];     // 分配一个字符数组，p 为字符串指针
      pa = new char[5][100];  // 分配一个二维字符数组， p 为字符串数组指针

      delete p;
      delete [] pa;

      销毁对象后，指针 p 变成没有定义，但其仍然存放先前所指向的对象(已销毁)的地址，指针 p 不再有效，称其为迷途指针
      通常在 delete 后将指针常设为 0 值指针，以避免迷途指针


2. 内存释放
  动态内存释放与分配必须对应，否则会产生"内存泄漏"
  再次释放已经释放的内存空间会导致程序出现崩溃

  静态内存的生命期由编译器自动确定
  动态内存的生命期人为确定


3. 动态分配数组
  3.1 一维数组
    int n = 4;
    int *p = new int[n*n];

  3.2 二维数组
    int m, n;
    int **p = new int* [m];     // 分配一个指针数组，其首地址在 p 中
    for(int i = 0; i < m; i++)  // 为指针数组的每个元素分配一个数组
      p[i] = new int [n];

    动态声明的数组的每一个元素 p[i] 均是一个 int* 类型，即一个地址，故只能通过 p[i][j] 或 *(*(p+i)+j) 来进行元素值的访问

    for(int i = 0; i < m; i++)
      delete [] p[i];
    delete [] p;

  3.3 三维数组
    int m, n, l;
    int ***p = new int** [l];
    for(int i = 0; i < l; i++)
      p[i] = new int* [m];
    for(int i = 0; i < l; i++)
      for(int j = 0; j < m; j++)
        p[i][j] = new int [n];

      