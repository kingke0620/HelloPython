#第二版在制作多份备份的时候能够正常工作，保存在一个子目录内
import os
import time

source = ['E:\python\workspace\hellopython\解决问题——备份文件\dir_copyOut']
target_dir = 'E:\python\workspace\hellopython\解决问题——备份文件\di_copyIn'

if not os.path.exists(target_dir):
    os.mkdir(target_dir)

#当前日期做主备份目录下的子目录名称
#当前时间作为zip的文件名
today = target_dir + os.sep + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

target = today + os.sep +now + '.zip'

if not os.path.exists(today):#--------------这是和ver1不同的主要改动
    os.mkdir(today)
    print('Successfully created directory',today)

zip_command = 'zip -r {0} {1}'.format(target,' '.join(source))


#运行备份
print('Zip command is')
print(zip_command)
print('Running')
if os.system(zip_command) == 0:
    print('Successfull backup tp',target)
else:
    print('Backup FAILED')