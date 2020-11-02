#global
caminos = []

#global
acciones = [1,-1]

def encontrar_caminos(camino_original,camino_actual,idx_actual):
    if(idx_actual==len(camino_original)):
        global caminos
        caminos.append(camino_actual.copy())
    else:
        if(camino_original[idx_actual]==0):
            global acciones
            for accion in acciones:
                camino_actual[idx_actual]=accion
                encontrar_caminos(camino_original,camino_actual,idx_actual+1)
        else:
            encontrar_caminos(camino_original,camino_actual,idx_actual+1)
            
            
def str2num(camino_str):
    camino = []
    for char in camino_str:
        if(char=='+'):
            camino.append(1)
        elif(char=='-'):
            camino.append(-1)
        else:
            camino.append(0)
    return camino
            
camino_deseado = input()
camino_recibido = input()

camino_deseado = str2num(camino_deseado)
camino_recibido = str2num(camino_recibido)

encontrar_caminos(camino_recibido,camino_recibido.copy(),0)

final_deseado = sum(camino_deseado)
finales_posibles = 0

for camino in caminos:
    if(sum(camino)==final_deseado):
        finales_posibles +=1
print(finales_posibles/len(caminos))



    