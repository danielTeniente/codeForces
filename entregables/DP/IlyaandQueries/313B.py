string = input()
m = int(input())

#se crea un vector alterno donde se cuenten
# los caracteres que cumplan la condición
# s_i = s_(i+1)
n = len(string)
array = [0]*n
if(string[0]==string[1]):
    array[0]=1

for i in range(1,n-1):
    array[i]=array[i-1]
    if(string[i]==string[i+1]):
        array[i]+=1
array[n-1]=array[n-2]
for _ in range(m):
    l,r = map(int,input().split())
    if(l==1):
        print(array[r-2])
    else:
        print(array[r-2]-array[l-2])