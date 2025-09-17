# 遍历字符串
for i in 'hello':
    print(i)

# rang()函数，python内置函数，产生一个[n,m]的整数序列，包含n,不包含m
for i in range(1, 11):
    if i % 2 == 0:
        print(i, '是偶数')

# 遍历1-10之间的累加和
s = 0
for i in range(1, 11):
    s += i
print('1-10累加和', s)

# 输出100-999之间的水仙花数
for i in range(100, 1000):
    sd = i % 10
    tens = i // 10 % 10
    hundreds = i // 100
    if sd ** 3 + tens ** 3 + hundreds ** 3 == i:
        print(i, '是水仙花数')

s = 0
for i in range(1, 11):
    s += i
else:
    print(s)
