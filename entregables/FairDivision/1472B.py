t = int(input())

for _ in range(t):
    n = int(input())
    candies = map(int,input().split())
    if(n==1):
        print('NO')
        continue
    suma_impares = 0
    for c in candies:
        if(c%2!=0):
            suma_impares+=1
    if(suma_impares%2==0 and (suma_impares!=0 or n%2==0)):
        print('YES')
    else:
        print('NO')

    