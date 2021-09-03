# George and Accommodation
n = int(input())
counter = 0

for _ in range(n):
    p,q = map(int,input().split())
    if(q-p>1):
        counter+=1
print(counter)
