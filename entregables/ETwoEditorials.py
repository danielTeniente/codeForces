entradas = input().split()

tareas = int(entradas[0])
participantes = int(entradas[1])
explicaciones = int(entradas[2])

interesados = [0]*(tareas+1)

for _ in range(participantes):
    rango = input().split()
    inicio = int(rango[0])-1
    fin = int(rango[1])
    interesados[inicio]+=1
    interesados[fin]-=1

temp_anterior = interesados[0]
for i in range(1,len(interesados)):
    interesados[i] = interesados[i]+interesados[i-1]+temp_anterior
    temp_anterior = interesados[i] - interesados[i-1]



suma_maxima = 0
for i in range(len(interesados)):

    if(i+explicaciones >= len(interesados)-2 ):
        break

    if(i == 0):
        interesados_1 = interesados[i+explicaciones-1]
    else:
        interesados_1 = interesados[i+explicaciones-1] - interesados[i-1] 


    for j in range(i+explicaciones,len(interesados)):
        if(j+explicaciones >= len(interesados)-2 ):
            break

        interesados_2 = interesados[j+explicaciones-1] - interesados[j-1] 
        suma = interesados_1 + interesados_2
        if(suma>suma_maxima):
            suma_maxima = suma

        print(suma,i-1,j-1)
     
print(suma_maxima) 


