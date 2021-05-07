from sys import argv
scrpit,user_name = argv

prompt='> '

print(f"Hi{user_name},i'm the {scrpit} script.")
print("I'd like to ask you a few question.")

print(f"Do you like me {user_name}")
likes =input(prompt)

print("where do you like{}".format(user_name))
lives = input(prompt)

print("what kind of computer do you have?")
computer=input(prompt)

print(f"""
   Alright,sou you said {likes} about likeing me.
   you live in {lives}.not sure where thast is.
   And you haave a {computer} coputer.Nice.
""")


