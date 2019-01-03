#self --python中的self相当于java中的this指针
#1 类
'''
class Person:
    pass #空代码块

p = Person()
print(p)#会直接给出内存中存储该对象的地址
'''

#2 方法
#与函数的唯一不同------拥有一个额外的self变量
'''
class Person:
    def say_hi(self):
        print("hello，how are you?")

p = Person();
p.say_hi()
'''

#3 __init__方法
#该方法不会被显式的调用
class Person:
    def __init__(self,name): #对目标对象进行初始化，该方法会在类的对象被实例化的时候立即运行
        self.name = name
    def say_hi(self):
        print('Hello, my name is'+self.name)

p = Person('kingke')
p.say_hi()

#4 类变量与对象变量
#类变量可被该类中所有的实例访问，对象变量不会被共享
class Robot:
    population  = 0 #统计机器人数量,这是一个类变量
    def __init__(self,name):#name是一个对象变量。！注意当类变量和对象变量名称相同时，类变量将会被隐藏
        '''初始化数据'''
        self.name = name
        print("(Initializing{})".format(self.name))

        Robot.population += 1#如果有新的实例初始化，个数将会增加一
    def die(self):
        print("{} is being destroyed".format(self.name))

        Robot.population -= 1
        #self.__class__.population -=1也可以，因为每个对象都通过self.__class__属性来引用它的类

        if Robot.population == 0:
            print('{} is the last one\n'.format(self.name))
        else:
            print('There are still {:d} robots working\n'.format(Robot.population))#:d，将格式定为十进制输出

    def say_hi(self):
        print('Greetings, my name is {}'.format(self.name))


    #使用装饰器，将这里标记为类方法
    '''其实等于
        how_many = classmethod(how_many)
    '''
    @classmethod
    def how_many(cls):
        '''打印当前的数量'''
        print('we have {} robots here'.format(cls.population))#作用应该是作为指针指向这个类，最好别换成其它字符串，为了代码整洁


#所有类成员都是公开的，有一个例外，若使用数据成员并在其名字中使用双下划线，例如__private,Python会将其调整为一个私有变量
#所有类成员，包括数据成员，都是公开的，并且python中所有的方法都是虚拟的

droid1 = Robot('robot1')
droid1.say_hi()
Robot.how_many()

droid2 = Robot('robot2')
droid2.say_hi()
Robot.how_many()

print('\nStart to destroy them\n')

droid1.die()
droid2.die()
Robot.how_many()

