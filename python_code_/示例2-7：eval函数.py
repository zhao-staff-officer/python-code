# 用于去掉函数字符串最外侧的引号，并按照python语句方式执行去掉引号后的字符串
# eval()函数经常和input()函数一起用

s = '3.14+3'
print(type(s))
print(eval(s))
print(type(eval(s)))

age = eval(input('请输入你的年龄：'))
print(age)
print(type(age))
