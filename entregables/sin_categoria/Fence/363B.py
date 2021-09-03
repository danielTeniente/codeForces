n,k = map(int,input().split())

heights = list(map(int,input().split()))

min_sum = 0
for i in range(k):
    min_sum+=heights[i]

last_idx=k
first_idx=1
j = 0
temp_sum = min_sum
for i in range(1,n-k+1):
    temp_sum = temp_sum-heights[first_idx-1]+heights[last_idx]
    first_idx+=1
    last_idx+=1
    if(temp_sum<min_sum):
        j=i
        min_sum=temp_sum

print(j+1)
