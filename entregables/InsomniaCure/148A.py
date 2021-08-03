k = int(input())
l = int(input())
m = int(input())
n = int(input()) 
d = int(input())

damaged_dragons = [0]*(d+1)
avaible_k = [k,l,m,n]
used_k = []
all_dragons = False
counter = 0

for k_i in avaible_k:
    if(k_i not in used_k):
        if(k_i==1):
            all_dragons = True
            break 

        for j in range(k_i,d+1,k_i):
            if(damaged_dragons[j]==0):
                damaged_dragons[j]=1
                counter+=1

        used_k.append(k_i)

if(all_dragons):
    print(d)
else:
    print(counter)
        


