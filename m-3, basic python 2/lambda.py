# lambda

# def doubled(x):
#     return x*2

doubled = lambda num: num *2
squared = lambda num: num *num
sum = lambda x,y  : x+y

result = doubled(44) 
result1 = squared(44) 
summ = sum(2,3)
# print(summ)

numbers=[12,56, 98, 78, 56, 12, 6, 98]
doubled_nums=map(doubled, numbers)
squared_nms = map(lambda x: x*x, numbers)
print(numbers)
print(list(doubled_nums))
print(list(squared_nms))


actors = [
    {'name': 'sabana', 'age': 65 },
    {'name': 'sabnoor', 'age': 45 },
    {'name': 'sabila noor', 'age': 30 },
    {'name': 'srabonti', 'age': 38 },
    {'name': 'shaon', 'age': 47 },
]

juniors=filter(lambda actor: actor['age']<40, actors)
fivers=filter(lambda actor: actor['age']%5==0, actors)
print(list(fivers))

