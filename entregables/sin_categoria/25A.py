# IQ test

n = int(input())
numbers = map(int,input().split())

count_even = 0 
count_odd = 0
last_even = 0
last_odd = 0
for i,num in enumerate(numbers):
    if(num%2 == 0):
        count_even+=1
        last_even = i+1
    else:
        count_odd+=1
        last_odd = i+1

if(count_even<count_odd):
    print(last_even)
else:
    print(last_odd)