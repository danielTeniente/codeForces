t = int(input())
for _ in range(t):
    a,b = map(int,input().split())
    min_side = min(a,b)
    max_side = max(a,b)
    sq1 = min_side*2
    if(sq1<max_side):
        print(max_side**2)
    else:
        print(sq1**2)
    