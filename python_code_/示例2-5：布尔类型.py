'''
False 或则None
数值中的0，包含0，0.0 ，虚数0
空序列，包含空字符，空数组，空列表，空字典，空集合
自定义对象的实例，该对象的_bool_()方法返回False或_len_()方法返回0

'''

X = True
print(X)
print(type(X))
print(X + 10)
print(False + 10)

print(bool(18))
print(bool(0), bool(0.0))
# 非0的整数类型都是True

print(bool('北京欢迎您'))
print(bool(''))
# 所有非空字符串都是True


print(bool(False))
print(bool(None))
