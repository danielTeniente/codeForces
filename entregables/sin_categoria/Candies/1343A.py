t = int(input())

for _ in range(t):
    n = int(input())
    #sucesiones geometricas
    # n = x*(2^k-1)
    k=2
    while(2**k<=n+1):
        x=n//(2**k-1)
        if(n==x*(2**k-1)):
            print(x)
            break
        k+=1
