n = int(input())

#si es par se resta cuatro
#si no, se resta nueve

if(n%2==0):
    # 4 es el primer par compositivo
    print(n-4,4)
else:
    # 9 es el primer impar compositivo
    print(n-9,9)

#en ambos casos, la resta es un número par
#mayor o igual a 4, así que se trata de un 
#número compositivo