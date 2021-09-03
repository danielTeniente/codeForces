n = int(input())
numbers = list(map(int,input().split()))
numbers = sorted(numbers)
for num in numbers:
    print(num,end=' ')

