#Remove Smallest

t = int(input())

for _ in range(t):
    n = int(input())
    numbers = map(int,input().split())

    numbers = sorted(numbers)
    is_posible = True
    for i in range(1,len(numbers)):
        if(numbers[i]-numbers[i-1]>1 or 
            numbers[i]-numbers[i-1]<-1):
            is_posible=False
            break

    if(is_posible):
        print('YES')
    else:
        print('NO')