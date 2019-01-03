#1 用户输入内容

#判断回文
def reverse(text):
    return text[::-1]
'''
切片功能反转文本：
已知可用seq[a:b]确定位置，从a到b结束时对序列进行切片。
第三个参数是步长，默认为1，返回一个连续的文本，如果是-1，
则将返回翻转后的文本
'''
def is_palindrome(text):
    return text == reverse(text)

something = input('Enter text:')

if is_palindrome(something):
    print('Yes,it is a palindrome')
else:
    print('No,it is not a palindrome')