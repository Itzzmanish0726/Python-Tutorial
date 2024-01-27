dish='Samosa'
print(dish)
print(dish[2])
print(dish[-1])
print(dish[-6])
print(dish[0:3])
print(dish[:3])
print(dish[::2])
print(dish[2:])
print(len(dish))  #gives the length of the string

##in and not in operators allow you to quickly determine if a given value is or isn't part of a collection of values.

myfood='samosa,jalebi'
print('jalebi' in myfood)
print('rice' in myfood)
print('rice' not in myfood)
print(myfood.replace('samosa','biryani')) # But this will not permanently change the string values for that we need to assign it differently
print(myfood)
myfood=myfood.replace('samosa','biryani')
print(myfood)  #now the values will be changed

#dir() will returns all properties and methods of the specified object, without the value
dir(myfood)
print(myfood.lower())
print(myfood.upper())
print(myfood.isdigit())
print(myfood.index('jalebi'))

#Combining Two or more sting and number this will not directly possible converting both to one type
states=29
text="states in India"
print(text+str(states))

#Using single quote in double quote
s="let's learn english"
print(s)

#Multiline String using '''
dialogue='''gabar: Kitne adami the?
kalia: Sardar, do'''
print(dialogue)

#Concatenating strings
first='M.S'
last='Dhoni'
print('Best Cricketer is: ',first+' '+last)


