n,m,k = map(int,input().split())

bin_nums = []

for _ in range(m):
    temp_bin = list(bin(int(input())))[2:]
    if(len(temp_bin)<n):
        temp_bin = ['0']*(n-len(temp_bin))+temp_bin
    bin_nums.append(temp_bin)

my_team = list(bin(int(input())))[2:]
if(len(my_team)<n):
    my_team = ['0']*(n-len(my_team))+my_team
num_friends = 0

for team in bin_nums:
    count = 0
    for i,digit in enumerate(my_team):
        if(digit != team[i]):
            count+=1
    if(count<=k):
        num_friends+=1

print(num_friends)

