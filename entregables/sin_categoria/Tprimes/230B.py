
criba=[0]*2+[1]*1000001
for i in range(2,1001):
     if criba[i]:
          for j in range(i*2,1000001,i):
               criba[j]=0

n = input()
numbers = map(int,input().split())

for num in numbers:
    #si es cuadrado de un número primo
    if(criba[int(num**(1/2))] and 
    #la raíz cuadrada entera no altera al número
        int(num**(1/2))*int(num**(1/2))==num):
        print('YES')
    else:
        print('NO')