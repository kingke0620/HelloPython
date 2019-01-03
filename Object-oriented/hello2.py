#继承
#老师和学生

#方法的实现顺序，方法若被重写，则先尝试运行子类中的，无法运行时再尝试运行基类中的
#coding=UTF-8

class SchoolMember:
    '''校内任何成员'''
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print('(Initialized SchoolMember : {})'.format(self.name))

    def tell(self):
        print('Name:"{}" Age:"{}"'.format(self.name,self.age),end=' ')

#继承直接写在类后括号内
class Teacher(SchoolMember):
    def __init__(self,name,age,salary):#如果在子类中没有构造初始化方法，python将会自动调用基类的构造函数
        SchoolMember.__init__(self,name,age)
        self.salary = salary
        print('(Initialized Teacher: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Salary:"{:d}"'.format(self.salary))

class Student(SchoolMember):
    def __init__(self,name,age,marks):
        SchoolMember.__init__(self,name,age)
        self.marks = marks
        print('(Initialized Student:{})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Marks:"{:d}"'.format(self.marks))

t = Teacher('Mrs Chris',25,8000)
s = Student('Robot',15,75)

print()#打印空白行

members = [t,s]#通过列表，对全体使用方法
for member in members:
    member.tell()
