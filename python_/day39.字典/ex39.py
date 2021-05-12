#create a mapping of state to abbreviation
states={'Oregon':'OR','Florida':'FL','California':'CA','New York':'NY','Michigan':'MI'}

cities={'CA':'San Francisco','MI':'Detroit','FL':'Jacksonville'}
#add some more cities
cities['NY']='New York'
cities['OR']='Portland'

#print out some cities
print('-'*10)
print("NY state has:",cities['NY'])
print("OR State has:",cities['OR'])

#print some states
print('-'*10)
print("Michigan's abbreviation is:",states['Michigan'])
print("Florida's abbreviation is:",states['Florida'])

#do it using the state then cities dict
print("-"*10)
print("Michigan has:",cities[states['Michigan']])
print("Florida has:",cities[states['Florida']])

#print every state abbreviation
print('-'*10)
for state,abbreve in list(states.items()):
    print(f"{state} is abbreviated{abbreve}")

#print every city in state
print('-'*10)
for abbreve,city in list(cities.items()):
    print(f"{abbreve} has the city {city}")

#now do both at the sam time
print('-'*10)

for state,abbreve in list(states.items()):
    # print(state,abbreve)
    print(f"{state} state is abbreviated {abbreve}")
    print(f"and has city {cities[abbreve]}")

#safely get a abbreviation by state that might not be there
print('-'*10)
state = states.get('Texas')
if not state:
    print("Sorry ,no Texas.")

#get a city a default value
city = cities.get('Tx',"Does Not Exits")
print(f"the city for the state 'TX' is:{city}")
