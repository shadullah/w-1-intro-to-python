n=int(input())
cnt=0
a = [int(x) for x in input().split()]

while True:
    allEven=True
    for i in range(n):
        if a[i]%2!=0:
            allEven=False
            break
        a[i]=a[i]//2
    
    if allEven:
        cnt=cnt+1
    else: 
        break

print(cnt)

