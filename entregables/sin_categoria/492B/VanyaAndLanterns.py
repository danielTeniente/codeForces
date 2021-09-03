n,l = map(int,input().split())

numbers = map(int,input().split())

numbers = sorted(numbers,reverse=True)

max_distance = 0

for i in range(1,len(numbers)):
    distance = numbers[i-1]-numbers[i]
    if(distance>max_distance):
        max_distance= distance


max_distance = max_distance/2
if(l-numbers[0]>max_distance):
    max_distance = l-numbers[0]

if(numbers[len(numbers)-1]>max_distance):
    max_distance = numbers[len(numbers)-1]

print(max_distance)