#在try块中获取资源，然后在finally块中释放资源。用with语句可以更干净完成
with open("poem.txt") as f:
    for line in f:
        print(line,end='')

'''
结构：with open(***) as *

with语句背后使用的协议会获取由哦喷反悔的对象，这里就是"thefile"
总会在代码块开始前调用thefile.__enter__函数，并总在代码块执行完毕后
调用thefile.__exit__

因此在finally代码块中编写的代码应格外留心__exit__方法的自动操作，避免重复显式使用
try..finally语句
'''