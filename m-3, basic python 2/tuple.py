def multiply():
    return 3,4
# print(multiply())

things= 'pen', 'tripod', 'sofa', 'laptop', 'phone', 'web cam'
# print(type(things))

if 'phone' in things:
    print('exists')

for item in things:
    print(item)

# tuple can't be changed
# things[0]='wagon'
# print(things)

# but if tuple have mutable type then it can be changable
mega = ([2,3,4], [6,7,8,9])
mega[0][1]=233
print(mega)