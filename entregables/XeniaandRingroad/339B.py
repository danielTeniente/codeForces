n,m = map(int,input().split())
houses = map(int,input().split())
actual_poss = 1
time = 0

for hi in houses:
    if(hi>=actual_poss):
        time+=(hi-actual_poss)
    else:
        time+=(hi+n-actual_poss)
    actual_poss=hi
print(time)