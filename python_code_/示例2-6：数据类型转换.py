'''
int(x) 将X转转换为整数类型
float(x) 将x转换为浮点类型
str(x) 将x转换为字符串
chr(x)将整数x转化为一个字符
ord(x)将一个字符x转换为其对应的整数值
hex(x)将一个整数x转为为一个十六进制字符串
otc(x)将一个整数x转为一个八进制字符串
bin(x)将有一个整数转化为二进制字符串
'''
x = 10
y = 3
z = x / y
print(z)
print(type(z))  # 隐士转换，通过运算隐士的转了结果的类型

# 将float转换为int
print('float转换为int类型', int(3.14))
print('float转换为int类型', int(3.9))
print('float转换为int类型', int(-3.14))
print('float转换为int类型', int(-3.9))

# 将int转换为float
print('int转换为float类型', float(10))

# 将str转换为int类型
print('str转换为int类型', int('100') + int('200'))
# 将str转换为float类型报错情况
# print(int('18a'))
# print(int('3.14'))

# chr() ord() 一对
print(ord('杨'))
print(chr(26472))

# 进制之前的转换
print('十进制转换为十六进制', hex(26472))
print('十进制转换为八进制', oct(26472))
print('十进制转换为二进制', bin(26472))
