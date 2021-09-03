# Taxi

n = int(input())

numbers = map(int,input().split())
numbers = sorted(numbers,reverse=True)

p_incio = 0
p_final = n-1
taxis_ctr = 0

while True:
    taxis_ctr+=1
    passengers = numbers[p_incio]
    while True:
        if(passengers+numbers[p_final]<=4 and
            p_final>p_incio):
            passengers+=numbers[p_final]
        else:
            break
        p_final-=1
    if(p_incio>=p_final):
        break
    p_incio+=1

print(taxis_ctr)


    
