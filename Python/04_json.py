1. json
  JSON(JavaScript Object Notation, JS 对象标记) 是一种轻量级的数据交换格式。
  JSON的数据格式其实就是python里面的字典格式，里面可以包含方括号括起来的数组，也就是python里面的列表。

  json:     dumps, dump, loads, load
  pickle:   dumps, dump, loads, load


2. Python -- JSON
    +-------------------+---------------+
    | Python            | JSON          |
    +===================+===============+
    | dict              | object        |
    +-------------------+---------------+
    | list, tuple       | array         |
    +-------------------+---------------+
    | str, unicode      | string        |
    +-------------------+---------------+
    | int, float, long  | number        |
    +-------------------+---------------+
    | True              | true          |
    +-------------------+---------------+
    | False             | false         |
    +-------------------+---------------+
    | None              | null          |
    +-------------------+---------------+


3. dumps / dump
   dumps 只完成了序列化为 obj
   dump  必须传文件描述符，将序列化的 obj 保存到文件中
 
  def dumps(obj, skipkeys=False, ensure_ascii=True, check_circular=True,
          allow_nan=True, cls=None, indent=None, separators=None,
          default=None, sort_keys=False, **kw):
      # Serialize ``obj`` to a JSON formatted ``str``.

  def dump(obj, fp, skipkeys=False, ensure_ascii=True, check_circular=True,
          allow_nan=True, cls=None, indent=None, separators=None,
          default=None, sort_keys=False, **kw):
      '''Serialize 'obj' as a JSON formatted stream to 'fp' (fp.write()-supporting file-like object.)'''

  eg. dump
        Tom = {"name":"Tom", "age":23}
        with open("Tom.json", "w", encoding='utf-8') as fjson:
            fjson.write(json.dumps(Tom, indent=2))
            # json.dump(Tom, fjson, indent=2)

        Tom.json：
        1. Tom = {"name":"Tom", "age":23} 
          {
            "name": "Tom",
            "age": 23
          }

        2. Tom = [{"name":"Tom", "age":23}]
          [
            {
              "name": "Tom",
              "age": 23
            }
          ]

      dumps
        >>> Tom = {"name":"Tom", "age":23}  
        >>> json.dumps(Tom)     # 字典
        '{"name": "Tom", "age": 23}'

4. loads / load 
   loads  只完成了反序列化 json -> obj(python)
   load   只接收文件描述符，完成了读取文件和反序列化
 
  def loads(s, encoding=None, cls=None, object_hook=None, parse_float=None, 
            parse_int=None, parse_constant=None, object_pairs_hook=None, **kw):
      '''Deserialize 's' (a str instance containing a JSON document) to a Python object.'''

  def load(fp, cls=None, object_hook=None, parse_float=None, parse_int=None, 
           parse_constant=None, object_pairs_hook=None, **kw):
      '''Deserialize fp (a fp.read()-supporting file-like object containing a JSON document) to a Python object.'''

  eg. load
        with open("Tom.json", "r", encoding='utf-8') as fjson:
          aa = json.loads(fjson.read())
          fjson.seek(0)
          bb = json.load(fjson)    # 与 json.loads(fjson.read())
        print(aa)  # {'name': 'Tom', 'age': 23}
        print(bb)  # {'name': 'Tom', 'age': 23}


        Tom.json：
        1.{
            "name": "Tom",
            "age": 23
          }
          output: {'name': 'Tom', 'age': 23}

        2.[
            {
              "name": "Tom",
              "age": 23
            }
          ]
          output: [{'name': 'Tom', 'age': 23}]

      loads
        >>> Tom = {"name":"Tom", "age":23}  
        >>> tom = json.dumps(Tom)
        '{"name": "Tom", "age": 23}'
        >>> json.loads(tom)
        >>> {'age': 23, 'name': 'Tom'}
        >>> json.loads('{"name":"Tom", "age":23}')  # 不能直接传入 dict, 得转化为 str(json) 后传入
        >>> {'age': 23, 'name': 'Tom'}
        
5. 处理中文
  data = json.load(f, encoding="utf-8", object_pairs_hook=collections.OrderedDict)
  json.dump(data, f, ensure_ascii=False)