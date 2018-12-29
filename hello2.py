#1 模块，代码复用的关键
import sys#sys是一个内置模块，import命令会去寻找（java的包）
print('The command line argument are:')
for i in sys.argv:#指明argv是sys模块的一部分，不和程序中另一个argv变量冲突
    print(i)#脚本名称总是位列第一，对应sys.argv[0].我设置的脚本参数为123 456 789 ，分别对应sys.argv[1]sys.argv[2]sys.argv[3]
print('\n\nThe PYTHONPATH is ',sys.path,'\n')#如果不是一个已编译好的模块，将会从sys.path所提供的目录中进行搜索，找到后，该模块中的语句将开始运行（注意初始化工作只会在第一次导入的时候完成）
#可以直接导入当前目录的模块，否则必须将模块放入sys.path所列出的目录中才可以导入
#当前目录可以通过
import os;
print(os.getcwd())
#来查看
#python将命令行参数存储在sys.path变量中给我们使用(使用IDE时，可用“运行”->“编辑结构”修改脚本参数)

#*******编译过程：python先把代码(.py文件)编译成字节码，交给字节码虚拟机，
# 然后虚拟机会从编译得到的PyCodeObject对象中一条一条执行字节码指令，并在当前的上下文环境中执行这条字节码指令，从而完成程序的执行。
#PYC：将.py文件转换成.pyc文件，pyc是已编译好的二进制文件，相当于省掉了你编译的过程，所以相较于导入模块会提高速度。而且这些按字节码编译的文件是独立于运行平台的

#2 from..import语句，直接将argv变量导入程序，省的每次输入sys.
from math import sqrt
print("Square root of 16 is",sqrt(16))

#3 模块的__name__,每个模块的都有名称，模块中的语句可以确定他们所处模块的名称。可以用以确定模块是独立运行还是被导入进来的
if __name__ == "__main__":#此处的name变量跟随的是当前模块的name
    print("running by itself")
else:
    print("being imported")

#4 自定义模块
#定义一个方法，在mymodule.py中引用
def say_hai():
    print('hi,mymodule')
__version__ = '0.1'


#5 dir函数，返回由对象定义的名称列表。若此对象是一个模块，则该列表会包含函数内所定义的函数、类与变量。
'''
在解释器中运行
import sys
dir(sys)#给出sys模块中属性名
dir()#当前模块
a=5
del a
dir()#对当前模块的变量增删
'''
#6 包：包是模块间的层次结构，包含模块与一个特殊文件__init__.py
'''
例子：
    -world/
        -__init__.py
        -asia/
            -__init__.py
            -india/
                -__init__.py
                -foo.py
        -africa/
            -__init__.py
            -madagascar/
                -__init__.py
                -bar.py
'''
