# while中使用
s = 0
i = 1
while i < 10:
    s += i
    if s > 20:
        print('累加和大于20的当前数是', i)
        break
    i += 1

# for中使用
for i in 'hello':
    if i == 'e':
        print('找到e')
        break
    print(i)
