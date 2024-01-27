Sweets=['Ladoo','Jalebi','Gulab Jamun','Halwa']
print(type(Sweets))
print(Sweets[2])
print(Sweets[-1])

#List Slicing
print(Sweets[:3])  #while Accessing we need to give one larger index so that canbe accessed
print(Sweets[-3:])
print(len(Sweets))

# in & not in operator
print('samosa' not in Sweets)
print('Jalebi' in Sweets)

#Adding an item in the list using append function(): Add at the last
Sweets.append('Rasmalai')
print(Sweets)

#Adding item in the list using insert function(): Add at the middle
Sweets.insert(2,'Kulfi')
print(Sweets)

#Now adding to lists PTR: List can be only concatenated using list only
Salty=['Samosa','Sev']
print(Salty)

food=Sweets+Salty
print(food)

#Now deleting and changing item in the list this will not be possible in strings
Sweets[0]='Barfi'
print(Sweets)

Sweets[0:2]='samosa'
print(Sweets)
Sweets[0:6]=['samosa']
print(Sweets)
Sweets[0:2]=[4,5,6,7]
print(Sweets)

#dir()
Sweets.reverse()
print(Sweets)

