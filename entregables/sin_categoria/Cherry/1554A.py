t = int(input())

for _ in range(t):
    n = int(input())
    numbers = list(map(int,input().split()))
    l=0
    r=1
    max_f_lr = numbers[r]*numbers[l]
    r+=1
    while(r<n):
        max_f_lr=max(max_f_lr,numbers[r]*numbers[r-1])
        r+=1

    print(max_f_lr)

