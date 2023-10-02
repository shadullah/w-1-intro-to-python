str=input()
cntL=0
cntR=0

current_sstr=""
cnt_balanced=0

for i in str:
    if i=='L':
        cntL=cntL+1
    else:
        cntR=cntR+1
    if cntL==cntR:
        cnt_balanced=cnt_balanced+1
        current_sstr=""

print(cnt_balanced)

for i in str:
    if i=='L':
        cntL=cntL+1
    else:
        cntR=cntR+1
    
    current_sstr=current_sstr+i
    if cntL==cntR:
        print(current_sstr)
        current_sstr=""
    