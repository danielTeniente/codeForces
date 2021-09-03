numbers_sums = map(int,input().split())
numbers_sums = sorted(numbers_sums,reverse=True)
total_sum = numbers_sums[0] # a+b+c
# c = total_sum - a - b
z = numbers_sums[1] # a+c
# a + total_sum - a - b = z
# b = total_sum - z 
y = numbers_sums[2] # b+c
x = numbers_sums[3] # a+b

b = total_sum-z
a = x-b
c = y-b
print(a,b,c)

