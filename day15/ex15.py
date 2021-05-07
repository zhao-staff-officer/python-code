from sys import argv
script,filename = argv

txt = open(filename)

print("here is your file {}".format(filename))
print(txt.read())

print("Type the file agein:")
file_agin = input(">")
txt_agin = open(file_agin,encoding="utf-8")
print(txt_agin.read())
