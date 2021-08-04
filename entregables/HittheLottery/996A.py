n = int(input())

dollars = [1,5,10,20,100]
counter = 0

for i in range(len(dollars)-1,-1,-1):
    if(dollars[i]<=n):
        counter+=n//dollars[i]
        n-= n//dollars[i] * dollars[i]
    if(n==0):
        break
print(counter)
