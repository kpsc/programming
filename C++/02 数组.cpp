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
        
        
        
        
        整个数组不能进行赋值、算术运算等，只能对元素进行操作