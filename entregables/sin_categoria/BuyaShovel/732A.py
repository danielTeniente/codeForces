k,r = map(int,input().split())

for y in range(1,11):
    if((k*y-r)%10==0):
        print(y)
        break
    elif((k*y)%10==0):
        print(y)
        break
