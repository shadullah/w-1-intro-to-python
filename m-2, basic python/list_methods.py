numbers=[12,45,98, 68,5]
numbers.append(56)
print(numbers)
numbers.insert(2,71)
# if(98 in numbers):
#     numbers.remove(98)
# numbers.remove(45)
# print(numbers)

last = numbers.pop()
# print(last, numbers)

if 5 in numbers:
    index= numbers.index(5)
    # print(index)



sorted = numbers.sort()
print(numbers)
    