x1,x2,x3 = sorted(map(int,input().split()))

min_distance = x1+x2+x3
# punto p
for p in range(x1,x3+1):
    min_distance = min(min_distance,
        abs(p-x1)+abs(p-x2)+abs(p-x3))

print(min_distance)

