# list, array, collection is same (simple terms)

# 
numbers = [45, 56, 12, 89, 87, 32, 89, 59, 46, 93]

print(numbers[3], numbers[-3])

# list(start: end) # start from the start index and stops before the end index
print(numbers[2:6])

# list(start: end: step) # start from the start index and stops before the end index
print(numbers[1:7:1])
print(numbers[1:7:2])
print(numbers[2:7:-1])
print(numbers[7:2:-1])
print(numbers[4:])
print(numbers[:5])
print(numbers[:])
print(numbers[::-1]) # reverse a list