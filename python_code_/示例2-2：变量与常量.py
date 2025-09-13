luck_number = 8  # 创建一个整形变量luck_number，值为8
my_name = "你好"
print("lunck_numner数据类型", type(luck_number))
print(my_name, "的幸运数字", luck_number)

# python动态修改变量的数据类型，通过赋值不同数据类型
luck_number = "8"
print("lunck_numner数据类型", type(luck_number))

# 在python中运行多个变量只想同一个值
no = number = 1024
print(no, number)
print(id(no), id(number))  # 查看对象的内存地址

# 常量定义
pi = 3.14  # 定义一个变量
PI = 3.14  # 定义一个常量
