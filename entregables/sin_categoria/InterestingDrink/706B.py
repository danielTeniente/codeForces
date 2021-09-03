n = int(input())

prices = sorted(list(map(int,input().split())))

q = int(input())

for _ in range(q):
    coins = int(input())
    total_shops = 0
    if(coins >= prices[-1]):
        total_shops = n
    else:
        a = 0
        b = n-1
        while(a<b):
            c = (a+b)//2
            poss_shop = prices[c]
            if(coins>=poss_shop):
                total_shops=c+1
                a=c+1 
            else:
                b=c
    print(total_shops)
