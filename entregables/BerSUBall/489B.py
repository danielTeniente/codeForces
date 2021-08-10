n = int(input())

boys = sorted(list(map(int,input().split())))

m = int(input()) 
girls = sorted(list(map(int,input().split())))


#emparejar a cada chico
n_idx = 0
m_idx = 0
counter =0

last_avaible_girl = 0

for n_idx in range(n):
    for m_idx in range(last_avaible_girl, m):
        if(-1<=girls[m_idx]-boys[n_idx]<=1):
            last_avaible_girl=m_idx+1
            counter+=1
            #pasar al siguiente chico
            break

print(counter)


