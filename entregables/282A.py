## CodeForces
# A. Bit++

#hay que ver el operador de en medio
n = int(input())
x = 0
for i in range(n):
    statement = input()
    if(statement[1]=='-'):
        x-=1
    else:
        x+=1
print(x)