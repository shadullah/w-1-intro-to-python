name='sakib\'s khan' #escape
name2= "shakib khan"
name3= """
    sakib khan
    number one
"""
print(name3)

#string is a sequence of characters
for char in name2:
    print(char)

print(name2[3])
print(name2[1:6])
print(name2[-3])
print(name2[::-1])


#mutable means changeable
#immutabale means you cannot change it

if'khan' in name2:
    print('exists')