t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    
    a = 1
    b = 10**9 * n
    while(a<=b):
        c=(a+b)//2
        if(c%n==0):
            c+=1
        current_k = c - (c-c%n)//n
        if(current_k==k):
            break
        elif(current_k<k):
            a=c+1
        else:
            b=c-1
    print(c)


    

    