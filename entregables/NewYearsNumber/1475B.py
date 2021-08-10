t = int(input())
#resovler la ecuación
#ax+by=c
#2020x+2021y = n

for _ in range(t):
    n = int(input())

    is_possible = False
    limit = (n//2020 +1)*2020
    a = 2020
    b = 2021
    for ax in range(0,limit,a):
        # y = (c-ax)/b
        y = (n-ax)//b
        #si y es entero
        if(ax+b*y==n):
            is_possible=True
            break

    if(is_possible):
        print('YES')
    else:
        print('NO')
    
