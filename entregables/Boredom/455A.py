n = int(input())

array = list(map(int,input().split()))
m = max(array)
counter = [0]*(m+1)
#counter for every number in the array
for a in array:
    counter[a] += 1

#function for dp
f = [0,counter[1]]
for i in range(2,m+1):
    f.append(max(f[i-1],f[i-2]+counter[i]*i))

print(f[m])


    

