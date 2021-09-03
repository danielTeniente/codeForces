t = int(input())

for _ in range(t):
    x,y,n = map(int,input().split())
    if(n%x!=y):
        m = n%x-y
        if(m<1):
            m+=x
    else:
        m = 0
    print(n-m)