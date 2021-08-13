t = int(input())

for _ in range(t):
    n = int(input())
    numbers  = map(int,input().split())
    min_num =0
    max_num =0

    for i,num in enumerate(numbers):
        if(num==1):
            min_num=i
        if(num==n):
            max_num=i

    min_moves = 0
    if(min_num<max_num):
        i = min_num
        j = max_num
    else:
        i = max_num
        j = min_num

    if(i+1<n-j):
        min_moves+=i+1
        min_moves+=min(j-i,n-j)
    else:
        min_moves+=n-j
        min_moves+=min(i+1,j-i)

    print(min_moves)
        

