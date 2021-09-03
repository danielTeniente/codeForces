## CodeForces
# A. Petya and Strings

n = 5
pos = [0,0]
for i in range(n):
    bin_list = input().replace(' ','')
    if('1' in bin_list):
        for j in range(len(bin_list)):
            if(bin_list[j]=='1'):
                pos=[i,j]
                break

col = pos[0] - 2
row = pos[1] - 2

if(col<0):
    col*=-1
if(row<0):
    row*=-1
    
print(col+row)