#Try...Finally

import sys
import time

f = None
try:
    f = open("poem.txt")
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print(line,end='')
        sys.stdout.flush()#此句保证print的内容可立即打印到屏幕上
        print("Pres ctrl+c now")
        #保证可以运行一段时间
        time.sleep(2)#打印一行后执行两秒休眠

except IOError:
    print("Could not find file poem.txt")
except KeyboardInterrupt:
    print("You cancelled the reading from the file.")

finally:
    if f:#************对文件对象进行的操作
        f.close()
    print("(Cleaning up:Closed the file)")

#在休眠期间摁下ctrl+c中断程序，虽然异常KeyboardInterrupt被抛出，但是退出前finally句子会执行，文件对象(实例)总会被关闭