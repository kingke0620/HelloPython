#coding=utf-8

#***************函数

#1 格式化方法format

temp1 = 23
temp2 = 'hellicrown'

print('Could it run {0},{1}'.format(temp1,temp2))
print('Could it run {},{}'.format(temp1,temp2))#same
print('{name} is a {thing}'.format(name='This',thing='Test'))
print('{0:.3f}'.format(1/3))
print('{0:*^8}'.format(temp1))
print('a',end='')
print('b',end=' ')
print('c')#自动换行，用end决定结尾是什么


#2 转义序列
print('what\'s your name')#单引号转义
print('change line\n This a new line')
print(" Its a line \
 This is still a line")#无\将报错
print(r'change line\n This a new line')#加个r是原始字符串，不转义

#运算符
#<<左移 >>右移
print(2)
print(2<<2)#后面的数字表示移几位
print(11>>1)#2的二进制10，左移2位后1000，是8。11=1011，右移变101=5



#3 if格式：
'''
 if 判断语句:
 elif 判断语句：
 else ：
'''


#4 for类似java的for:each

for i in range(1,5):
    print(i)
else:
    print('The loop is over')#注意不会到5，不把第二个参数包含在内

for i in range(1,5,2):#每次递增默认1.改为2
    print(i)
else:
    print('The loop2 is over')

for i in list(range(5)):#完整列表
    print(i)
else:
    print('The loop is over')

#5 Continue循环中继续后续代码执行，用法类似else
#而且，continue语句同样能用于for循环

#6 函数定义，关键字def来定义

def say_hello():
    print('hello')

say_hello()
say_hello()

#7 定义函数中有传入的参数，则是函数中的局部变量，如果想在程序顶层给变量赋值，用global语句

x = 50
def func():#注意不是func(x),x在函数内用global引用
    global x

    print('x is ',x)
    x = 2
    print('now,x is',x)
func()
print('x is ',x)

#8 默认参数值（定义时设置）除非用户更改，否则默认执行
def func1(message,times=1):#注意只有参数末尾的才能被赋予默认参数值
    print(message * times)
func1('hello')
func1('hello',5)

#9 关键字参数，不用考虑位置的修改方式
def func2(a,b=1,c=3):
    print('a = ',a,'b = ',b,'c = ',c)
func2(8,9)
func2(11,c=23)
func2(c=44,a=1)#注意赋值顺序是先关键字，再默认

#10 可变参数，*号改变变量数量----------------------------概念元组和字典在后方有继续讲解
def total(a=5,*numbers,**phonebook):
    print('a',a)

    #遍历元组所有项目
    for single_item in numbers:
        print('single_item',single_item)

    #遍历字典中所有项目
    for first_part, second_part in phonebook.items():
        print(first_part,second_part)
print(total(10,1,2,3,Jack=1123,John=2231,Inge=1560))


#11 文档字符串DocStrings
def print_max(x,y):
    '''The charm of this method is just here.
    
    And this is the second line'''
    # 之后的文档最好都按此格式

    x=int(x)
    y=int(y)

    if(x>y):
        print(x,'is maximum')
    else:
        print(y,'is maximum')
print_max(3,5)
print(print_max.__doc__)#doc获取函数的文档字符串属性，因为python将所有东西都视为一个对象

help(print_max)#展示文档字符串，解释器中按q退出

