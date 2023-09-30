# # n = int(input("Enter the number of inputs: "))
# n=int(input())
# numbers = []

# for i in range(n):
#     x = int(input())
#     numbers.append(x)

# for num in numbers:
#     while num>0:
#         last= num%10
#         print(last, end=' ')

#         num=num//10
        
#     print()

# Read the number of test cases
T = int(input())

# Iterate through each test case
for i in range(T):
    # Read the input number as a string
    N = input().strip()
    
    # Reverse the input string and split it into a list of characters
    digits = list(reversed(N))
    # print(digits)
    
    # Print the reversed digits separated by space
    print(" ".join(digits))