1. 函数声明只能有一次

2. 默认参数为自右向左, 默认值不可以为局部变量
   int volume(int L,  int W, int H=1);
    
3. 函数重载
    同一个域中用一个函数名来定义多个函数，但参数列表彼此不同，或参数个数不同，或参数类型不同
    
4. 函数模板
   用于设计通用型的函数，只在需要时自动实例化
   
   eg.
     template<模板形参表>
     返回类型 函数名(形参列表)  {函数体}
        
   模板形参表:
       (1) typename param1, typename param2, ...
       (2) class param1, class param2, ...
       
5. 库函数
        
            