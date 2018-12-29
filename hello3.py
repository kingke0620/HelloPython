#数据结构
#Python有四种内置数据结构——列表（List）、元组（Tuple）、字典（Dictionary）、集合（Set）。

#1 列表，用方括号括起来的清单
#2 对象与类的概念略过，与java雷同
shoplist = ['apple','mango','carrot','banana']

print('The first item I will buy is',shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print('I bought ',olditem)
print('My list now is ',shoplist)

#3 元组，类似于列表，但是无法编辑或更改。通过特别指定项目来定义，推荐用括号。
# 通常用于保证函数可安全地采用一组数值，元组内数值不会改变

old_list = ('a','b','c')
print('number of old_list is ',len(old_list))

new_list = ('d','e',old_list)
print('number of positions in new_list is',len(new_list))
print('all words in new_list are ',new_list)
print('words from old_list are',new_list[2])#从0开始
print('last word brought from old_list is',new_list[2][2])#元组的嵌套定位
print('number of words in the new_list is',len(new_list) + len(new_list[2]) - 1)

#4 字典：键值和值
ab = {#ab是adress和book的缩写，地址簿
    'A':'Here is the value of key A',
    'B':'Here is the value of key B',
    'C':'Here is the value of key C'
}

print('The value of A is',ab['A'])

del ab['C']#删除一对键值

print('\nThere are {} keys is address-book '.format(len(ab)))

for name,address in ab.items():
    print('Key {} at {}'.format(name,address))

#添加一对键值
ab['D'] = 'Here is the value of key D'

if 'D' in ab:#检索键值是否存在
    print('Value of {} is {}'.format('D',ab['D']))

#5 序列：主要是资格测试和索引操作，允许我们直接获取序列中的特定项目
#切片运算符（Slicing），允许我们序列中的某段切片——序列中的一部分(列表，元组和字符串都可以)

shoplist = ['apple','mango','carrot','banana']
name = 'swaroop'

#索引
print('Item 0 is',shoplist[0])
print('Item 1 is',shoplist[1])
print('Item 2 is',shoplist[2])
print('Item 3 is',shoplist[3])
print('Item -1 is',shoplist[-1])#向前循环
print('Item -2 is',shoplist[-2])
print('Character 0 is',name[0])

#列表切片
print('Item 1 to 3 is',shoplist[1:3])#实际上是索引 1和 2的元素，不到底
print('Item 2 to end is',shoplist[2:])#包含起始位置，但是不包含结束位置
print('Item 1 to -1 is',shoplist[1:-1])
print('Item start to end is',shoplist[:])

#字符串切片

#同上，不赘述

#也可以采用步长
print(shoplist[::1])

#6 集合（set）：简单对象的无序集合（Collection）
'''
可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
创建格式：
parame = {value01,value02,...}
或者
set(value)
'''
bri = {'brazil','russia','india'}
#写法2：bri = set(['brazil','russia','india'])
print('india' in bri)
print('usa' in bri)

bric = bri.copy()
bric.add('china')
print(bric.issuperset(bri))
bri.remove('russia')
print(bri&bric)
#OR bri.intersection(bric)

#7 引用
bri1 = ['a','b','c']

fake_bri1 = bri1#指向同一个变量
fake_bri1_1 = bri1[:]#创建了一份副本

del bri1[0]
print(bri1)
print(fake_bri1)
print(fake_bri1_1)
print('\n')
del fake_bri1_1[0]
print(bri1)
print(fake_bri1)
print(fake_bri1_1)

#8 字符串的常用方法
name = 'Swaroop'

if name.startswith('Swa'):
    print('yes,started with swa')
if 'a' in name:
    print('yes a is in name')
if name.find('war') != -1:
    print('yes,it contains this string "war" ')

delimiter = '_*_'
mylist = ['Brazil','Russia','India','China']
print(delimiter.join(mylist))#join方法，将列表项连接起来，做为分隔符，返回一串更大的字符串