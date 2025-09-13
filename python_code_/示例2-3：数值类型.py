# 整数的四种表示形式
num = 987  # 默认十进制，表示整数
num2 = 0b1010101  # 使用二进制表示整数
num3 = 0o765  # 使用八进制表示整数
num4 = 0x87ABF  # 使用十六进制表示整数

print(num, num2, num3, num4)

# 浮点型类型的使用
height = 1.78
print(height)
print(type(height))

# 科学计数法
x = 1.99E1413
print('科学及算法', x, 'x的数据类型', type(x))

# 不确定的尾数问题
print(0.1 + 0.2)
print(round(0.1 + 0.2, 1))

# 复数类型的使用
x = 123 + 456j
print(x.real, x.imag)
