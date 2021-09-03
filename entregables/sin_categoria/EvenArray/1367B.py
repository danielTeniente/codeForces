t = int(input())

for _ in range(t):
    n = int(input())
    numbers = map(int,input().split())
    counter = 0
    movs = 0
    for i,num in enumerate(numbers):
        if(i%2!=num%2):
            if(num%2==0):
                counter-=1
            else:
                counter+=1
            movs+=1
    if(counter==0):
        print(movs//2)
    else:
        print(-1)
