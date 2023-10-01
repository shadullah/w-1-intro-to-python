# set: unique items collection
numbers=[12,56, 98, 78, 56, 12, 6, 98]
print(numbers)
number_set= set(numbers)
print(number_set)
number_set.add(55)
print(number_set)
number_set.remove(6)
print(number_set)
# number_set[1]=5 #set can't be reassgined
for item in number_set:
    print(item)

if 9 in number_set:
    print('9 exist')
elif 98 in number_set:
    print('98 exists')

a={1,3,5}
b={1,2,3,4,5}
print(a & b)
print(a|b) # a U b