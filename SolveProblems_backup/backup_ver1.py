#实现备份功能
import os
import time

#1 需要备份的文件指定在一个列表中
source = ['E:\python\workspace\hellopython\解决问题——备份文件\dir_copyOut']

#2 备份文件存储在一个 主备份目录中
target_dir = 'E:\python\workspace\hellopython\解决问题——备份文件\di_copyIn'

#3 备份文件打包压缩成zip文件
#4 压缩文件名由日期和时间决定
target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'
#sep为分隔符,不同的系统不一样，
#time.strftime('')建立时间戳

#***这里出现过一个错误，直接将list和str用加号连起来了，实际上要进行格式转换，或者list.append(str)

#若目标目录不存在，则进行创建
if not os.path.exists(target_dir):
    os.mkdir(target_dir)

#5 使用zip命令将文件打包成zip格式
zip_command = 'zip -r {0} {1}'.format(target,' '.join(source))
#***fomat后续接上一段用' '.join(***)str.join(元组、列表、字典、字符串) 之后生成的只能是字符串。
#所以很多地方很多时候生成了元组、列表、字典后，可以用 join() 来转化为字符串。
#r是递归，recursively


#运行备份
print('Zip command is')
print(zip_command)
print('Running')
if os.system(zip_command) == 0: #os.system，这一函数可以使命令像是从系统中运行的。也就是说从shell中运行的，如果运行成功，将返回0，如果运行失败，将返回一个错误代码
    print('Successful backup to',target)
else:
    print('Backup FAILED')