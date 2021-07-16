# Tram

n = int(input())
n_passengers = 0
max_num = 0

for i in range(n):
    a,b = input().split()
    a = int(a)
    b = int(b)
    n_passengers-=a
    n_passengers+=b

    if(max_num<n_passengers):
        max_num=n_passengers
print(max_num)