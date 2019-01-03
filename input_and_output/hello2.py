# #2 文件
# #使用read,readline,write等方法来打开或者使用文件
#
#
# poem = '''\
# Programming is fun
# When the worl is done
# if you wanna make your work also fun:
#  use Python!
# '''
#
# #打开文件以编辑
# f = open('poem.txt','w')#如果没有对应文本，则会在当前目录新建一个文件
# '''
# open可以更改后面的字幕，进入阅读模式('r')，写入模式('w')和追加模式('a')
# 还可以通过文本模式('t'),二进制模式('b')来进行阅读写入追加文本。
# '''
# #向文件中编写文本
# f.write(poem)
# #关闭文件
# f.close()
#
# #如果没有特别指定，将假定启用默认的阅读模式
# f = open('poem.txt')
# while True:
#     line = f.readline()#按行读取
#     #零长度指示EOF
#     if len(line) == 0:
#         break
#     print(line,end='')
# f.close()

#----------------------------------分割-----------------------------------------

# #2 Pickle模块
# #可以将任何纯python对象存储到一个文件（建立一个data后缀的文件）中，并在稍后将其取回。叫做持久地存储对象
# import pickle
# shoplistfile = 'shoplist.data'
# shoplist = ['apple','mango','carrot']
#
# f = open(shoplistfile,'wb') #通过写入二进制模式打开文件，然后调用dump函数，称为封装（Picking）
# #open()会返回一个file对象
# pickle.dump(shoplist,f)#这一步在当期目录创建了data后缀的文件(文件名由之前的变量shoplistfile决定)
# f.close()
#
# del shoplist#删除变量shoplist,证明后面的打印是源从文件内的数据
#
# f = open (shoplistfile,'rb')
# storedlist = pickle.load(f)#通过pickle的load函数接受返回的对象，称为拆封（Unpicking）
# print(storedlist)

#3 将Unicode字符串转换成"UTF-8"格式，生成txt文件，并直接对其进行输入输出

#encoding=utf-8
#上面这句注释必须放置在程序顶端，告知python程序我们使用的是utf-8
import io
f= io.open("abc.txt","wt",encoding="utf-8")
f.write(u"尝试无英文")
f.close()

text = io.open("abc.txt",encoding="utf-8").read()
print(text)