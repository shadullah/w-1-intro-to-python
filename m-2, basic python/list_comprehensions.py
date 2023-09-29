numbers = [45, 87, 96, 65, 43, 85, 14, 26,61]
odds=[]
for num in numbers:
    if num%2 == 1:
        odds.append(num)

print(odds)

# print(odds)
# odd_nums=[num for num in numbers]
# odd_nums=[num for num in numbers if num %2==1 if num%5==0]

print(odd_nums)