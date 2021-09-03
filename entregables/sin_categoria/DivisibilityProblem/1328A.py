t = int(input())

for _ in range(t):
    a,b = map(int,input().split())

    if(a%b!=0):
        div = a//b
        higher = b*(div+1)
        print(higher-a)
    else:
        print(0)