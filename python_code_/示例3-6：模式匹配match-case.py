score = input("请输入成绩：")
match score:
    case 'A':
        print("优秀")
    case 'B':
        print("良好")
    case 'C':
        print("及格")
    case 'D':
        print("不及格")
    case _:
        print("输入错误")
