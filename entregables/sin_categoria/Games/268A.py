n = int(input())
host = []
guest = []
counter = 0

for _ in range(n):
    h,g = map(int,input().split())
    host.append(h)
    guest.append(g)

for h in host:
    for g in guest:
        if(h==g):
            counter+=1

print(counter)

