print("let's practive everything.")
print('you\'d need know \'about escapes with \\ that do:')
print('\n newlines and \t tabes.')

poem="""
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion form intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("------------------")
print(poem)
print("------------------")

five =10-2+3-6
print(f"this should be five:{five}")

def secret_formula(started):
    jelly_beans = started *500
    jars = jelly_beans/1000
    crates = jars/100
    return jelly_beans,jars,crates
start_point =10000
beans,jars,crates = secret_formula(start_point)

#remember that this is another way to format a string
print("with a starting point of:{}".format(start_point))

#it's just like with an f"" string
print(f"we'd have {beans},{jars} jars,and {crates} ceates.")

start_point = start_point/10

print("we can alseo do that this way:")
formula = secret_formula(start_point)

#this is an easy way to apply a list to format string
print("we'd have {} benas,{} jars,and {} crates.".format(*formula))
