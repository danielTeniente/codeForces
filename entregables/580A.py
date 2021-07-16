# Kefa and First Steps

n = int(input())

numbers = map(int,input().split())
numbers = list(numbers)
current_count = 1
maximum = 1

for i in range(1,len(numbers)):

    if(numbers[i]<numbers[i-1]):
        current_count = 0

    current_count+=1
    
    if(current_count>maximum):
        maximum=current_count

print(maximum)