## CodeForces
# A. Team

n = int(input())
counter = 0
for i in range(n):
    (a,b,c) = input().split()
    a = int(a)
    b = int(b)
    c = int(c)
    if(a+b+c>1):
        counter+=1
print(counter)


