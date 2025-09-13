# 字符串类型
city = '天津'
address = 'xx街'
print(city, address)

# 多行字符串
info = '''
收件人：你好
手机号：1111222
'''
print(info)

# 转义字符
print('北京')
print('欢迎您')
print('北京\n欢迎您')  # 遇到\n换行
print('北京\t欢迎您')  # 一个制表位是8个字符
print('老师说：\'好好学习，天天向上\'')
print('老师说：\"好好学习，天天向上\"')

# 原字符，使转义失效的字符R或者r
print(r'北\n京欢迎您')
print(R'北\n京欢迎您')

# 字符串索引及切片
s = 'HELLOWORLD'
print(s[0], s[-10])  # 序号0和序号-10表示的是同一个字符
print('北京欢迎您'[0])
print(s[2:7])  # 从2开始到7结束，不包含7,正向递增
print(s[-8:-3])  # 反向递减
print(s[:2])  # 默认N从0开始
print(s[5:])  # m,默认N到末尾结束

# 字符串类型操作
x = '2022年'
y = '北京冬奥会'
print(x + y)  # 链接两个字符
print(x * 3)  # 对x这个字符复制
print(3 * x)  # 对x这个字符复制
print('北京' in y)  # 判断字符串是否存在
