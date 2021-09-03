#2<=n<=100
n = int(input())
# 1<=num<=100
numbers = list(map(int,input().split()))

min_sold = min(numbers)
max_sold = max(numbers)
idx_max = 101
idx_min = 0


for i in range(n):
    if(numbers[i]==max_sold and i<idx_max):
        idx_max = i
    if(numbers[i]==min_sold and i>idx_min):
        idx_min = i

if(idx_max>idx_min):
    print(idx_max+n-1-idx_min-1)
else:
    print(idx_max+n-1-idx_min)


