number = eval(input("请输入数字："))

if number == 987654:
    print("恭喜中将")
else:
    print("你未中将")

result = '共享你中将了' if number == 987654 else '未中将'
print(result)