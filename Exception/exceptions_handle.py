#1 异常处理

# try :
#     text = input('Enter sth -->')
# except EOFError:  #输入crtl+d激活错误
#     print('Its EOF error')
# except KeyboardInterrupt:#输入crtl+c激活错误
#     print('You cancelled the operation')
# else:
#     print('You entered {}'.format(text))

#2 抛出异常
#所引发的错误或者异常，必须是直接或者间接从属于Exception（异常）类的派生类
#encoding=UTF-8

class ShortInputException(Exception):
    '''
    一个由用户定义的异常类
    判断是否过短
    属性有长度length，和最小标准atleast
    '''
    def __init__(self,length,atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast

try :
    text = input('Enter something -->')
    if len(text) < 3:#利用raise引发一次异常，并使用异常字段的属性
        raise ShortInputException(len(text),3)
    #其他工作此处可以正常运行

except EOFError:
    print('It\'s a EOF error')
except ShortInputException as ex:  #将该类存储（as）相应地错误名或者异常名
    #这里的ex是异常类的实例，有length和atleast的属性
    print(('ShortInputException: The imput was' +
           '{0} long, excepted at least {1}').format(ex.length,ex.atleast))
else:
    print('No exception was raised.')