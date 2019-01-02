#第三版，实现相关修改和zip的文件名产生关联
import  os
import  time
source = ['E:\python\workspace\hellopython\解决问题——备份文件\dir_copyOut']
'''
因为source是一个列表，所以可以使用添加其他目录或者文件传递进脚本中
使用sys.argv获得这些额外文件的名称
使用list.extend方法把他们添加进source
'''

target_dir = 'E:\python\workspace\hellopython\解决问题——备份文件\di_copyIn'

#验证目标目录是否存在
if not os.path.exists(target_dir):
    os.mkdir(target_dir)

today = target_dir + os.sep + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

#-----------------------
#添加一条来自用户的注释以创建
#zip文件的文件名
comment = input('Enter a comment -->')
#检查是否有评论键入
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + \
             comment.replace(' ','_') + '.zip'

#-----------------------

#验证子目录是否存在
if not os.path.exists(today):
    os.mkdir(today)
    print('Successfully created directory',today)

zip_command = 'zip -r {0} {1}'.format(target,''.join(source))
#可选 -v 显示信息的详尽程度 -q 使程序静默运行（quiet）

#运行
print('Zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('Successful backup to',target)
else:
    print('Backup FAILED')
