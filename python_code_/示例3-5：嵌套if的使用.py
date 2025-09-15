answer = input("请问你喝酒了吗：")
if answer == 'y':
    proof = eval(input("你喝了多少酒："))
    if proof <= 20:
        print("构不成酒驾，祝你一路平安")
    elif proof < 80:
        print("已构成酒家标准，请不要开车")
    else:
        print("已达到醉驾")
else:
    print("你走吧")
