# Young Physicist
n = int(input())
sum = [0,0,0]

for i in range(n):
    num_ls = input().split(' ')
    for j in range(3):
        sum[j]+=int(num_ls[j])

if(sum[0]==0 and sum[1]==0 and sum[2]==0):
    print('YES')
else:
    print('NO')