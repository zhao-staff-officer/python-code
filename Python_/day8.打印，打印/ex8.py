formatter ="{} {} {} {}"
print(formatter.format(1,2,3,4))
print(formatter.format("one","two","three","four"))
print(formatter.format(True,False,False,True))
print(formatter.format(formatter,formatter,formatter,formatter))
print(formatter.format(
    "Try your",
    "own text here",
    "maybe a poem",
    "or a song about fear"
))
