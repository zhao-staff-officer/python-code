# this one is like your script with argv
def print_two(*args):
    arg1,arg2=args
    print(f"arg1:{arg1},arg2:{arg2}")

#ok,that *args is actually pointless,we can just do this
def print_two_agin(arg1,arg2):
    print(f"arg1:{arg1},arg2:{arg2}")

#this just takes one argument
def print_one(arg1):
    print("arg1:{}".format(arg1))

#this one takes no arguments
def print_none():
    print("I got nothin'.")

print_two("zed","shaw")
print_two_agin("zed","shaw")
print_one("First!")
print_none()
