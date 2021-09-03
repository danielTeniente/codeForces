s,n =map(int,input().split())
can_pass = True
dragons = []

for _ in range(n):
    x,y = map(int,input().split())
    dragons.append((x,y))

dragons = sorted(dragons,key=lambda x:x[0])

for dragon in dragons:
    if(s>dragon[0]):
        s+=dragon[1]
    else:
        can_pass=False
        break
    
if(can_pass):
    print('YES')
else:
    print('NO')