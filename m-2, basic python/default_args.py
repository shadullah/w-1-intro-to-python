def sum(num1,num2):
    result=num1+num2
    return result
total =sum(99,11)
# print('total', total)

def sum(num1,num2, num3=0):
    result=num1+num2+num3
    return result

# total =sum(99,11,2)
# print('total', total)

# args
# def all_sum(*numbers):
#     print(numbers)
#     for num in numbers:
#         print(num)

# total = all_sum(45,56)
# print('all sum: ', total)


def all_sum(num1,num2,*numbers):
    print(numbers)
    sum=0
    for num in numbers:
        print(num)
        sum=sum+num
    return sum

total = all_sum(45,56,20,30)
print('all sum: ', total)


def do_a_lot(*args):
    print(args)