m,s = map(int,input().split())
min_digit=0
max_digit=0

if(m>1 and s==0 or s>m*9):
    min_digit=-1
    max_digit=-1
else:
    if(s!=0):
        sub_min = [0]*m
        #no se necesita llegar hasta 10**0
        #el último número debe completar la suma
        sub_sum = s
        for i in range(m-1,-1,-1):
            for j in range(0,10):
                if(i==m-1 and j==0):
                    continue
                sub_sum -= j
                if(sub_sum<=i*9):
                    sub_min[i]=j
                    break
                else:
                    sub_sum+=j
        sub_sum = s
        sub_max = [0]*m
        for i in range(m-1,-1,-1):
            for j in range(9,-1,-1):
                sub_sum-=j
                if(sub_sum>=0):
                    sub_max[i]=j
                    break
                else:
                    sub_sum+=j
        for i in range(m):
            min_digit+=sub_min[i]*10**i
            max_digit+=sub_max[i]*10**i
    else:
        max_digit=0
        min_digit=0
print(min_digit,max_digit)
