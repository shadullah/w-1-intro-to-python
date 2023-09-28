def full_name(first,last):
    name=f'{first} {last}'
    return name
# take paremeters in order
# name= full_name('alu','kodu')

# name= full_name(last='kodu', first='ami')
# print(name)

# def famous(**kargs)
def famous_nm(first,last ,**addition):
    name=f'{first} {last}'
    # print(addition['title'])
    for key,value in addition.items():
        print(key,value)
    return name
name=famous_nm(first='Taher', last='ali', title='hujur', addition='taheriar')
print(name)

# def function_Name(num1, num2, *args, **kargs):


# return multiple things from an array
def a_lot(num1,num2):
    sum= num1+num2
    mult=num1+num2
    remain = num1-num2
    return [sum, mult, remain]
    # return sum, mult, remain ---> tuple

everything= a_lot(55,22)
print(everything)