n=int(input())
a=list(map(int, input().split()))

elemnt_cnt={}

for num in a:
    if num in elemnt_cnt:
        elemnt_cnt[num]+=1
    else:
        elemnt_cnt[num]=1

removed=0

for num, cnt in elemnt_cnt.items():
    if cnt > num:
        removed+=cnt -num
    elif num > cnt:
        removed+=cnt

print(removed)