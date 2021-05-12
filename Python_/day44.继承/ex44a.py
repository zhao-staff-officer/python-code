class Parent(object):
    def implicit(self):
        print("PARENT IMPLICIT()")

class Children(Parent):
    pass



if __name__ == '__main__':
    dad =Parent()
    son =Children()

    dad.implicit()
    son.implicit()

