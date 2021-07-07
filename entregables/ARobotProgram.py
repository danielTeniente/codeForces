t = int(input())
for _ in range(t):
    entrada = input().split()
    x = int(entrada[0])
    y = int(entrada[1])
    mayor = max(x,y)
    menor = min(x,y)

    pasos_dobles = (mayor-menor-1)
    if(pasos_dobles<0):
        pasos_dobles = 0

    pasos = x + y - pasos_dobles + pasos_dobles *2
    print(pasos)