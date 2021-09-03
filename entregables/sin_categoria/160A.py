# Twins

_ = int(input())
coins = map(int,input().split())

coins = sorted(coins,reverse=True)
total_value = 0
counter = 0
get_all = False

for i in range(len(coins)):
    counter+=1
    total_value+=coins[i]
    if(i == len(coins)):
        get_all = True
        break
    if(total_value>sum(coins[i+1:])):
        break

if(get_all):
    print(len(coins))
else:
    print(counter)
