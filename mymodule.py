#承接hello2中的模块
from hello2 import say_hai,__version__
say_hai()
print('Version',__version__)#注意导入模块的时候，导入的时候实际上就是对py文件进行了依次初始化，
# 也就是跑一遍代码。那么模块内所有函数自然就被执行了，而且在终端上看到了效果。

#若想单独运行模块时，运行某个函数，用__name__
#在原模块中如下写码，此处不会运行
if __name__ == '___main__':
    say_hai()

