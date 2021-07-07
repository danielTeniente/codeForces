# Codeforces
#A. Football

bin_ls = input()
counter = 1
max_c = 0
is_dangerous = False
for i in range(1,len(bin_ls)):
    if(bin_ls[i]==bin_ls[i-1]):
        counter+=1
        if(counter==7):
            is_dangerous = True
            break
    else:
        counter=1

if(is_dangerous):
    print('YES')
else:
    print('NO')