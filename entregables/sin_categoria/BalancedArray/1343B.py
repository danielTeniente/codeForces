t = int(input())

for _ in range(t):
    n = int(input())
    sum_odd=0
    sum_even=0
    if(n%4==0):
        print('YES')
        for even in range(2,n+1,2):
            sum_even+=even
            print(even,end=' ')
        for odd in range(1,n-1,2):
            sum_odd+=odd
            print(odd,end=' ')
        print(sum_even-sum_odd)

    else:
        print('NO')