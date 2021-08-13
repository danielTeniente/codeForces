n = int(input())
numbers = list(map(int, input().split()))

# S es el número de 1 que existen en la lista
S = sum(numbers)
# S + movimiento se debe maximizar
mov = [x*(-2)+1 for x in numbers]
suma = mov[0]
maximo = suma
for i in range(1,len(mov)):
    suma += mov[i]
    if(suma<mov[i]):
        suma = mov[i]
    if(maximo<suma):
        maximo = suma
print(S+maximo)