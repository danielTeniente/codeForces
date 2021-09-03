# Bear and Big Brother

#aplicaré búsqueda binaria

def get_weight(num,base,idx):
    return num * base**idx

idx_max = 100
idx_min = 1

a,b = input().split()
a = int(a)
b = int(b)

while (idx_min<=idx_max):
    idx_mean = (idx_max+idx_min)//2
    #a tiene que ser mayor a b para que sea correcto
    if(get_weight(a,3,idx_mean)>get_weight(b,2,idx_mean)):
        #si el indice anterior sigue siendo mayor, se pasa
        if(get_weight(a,3,idx_mean-1)<=get_weight(b,2,idx_mean-1) or idx_mean==1):
            print(idx_mean)
            break
        #la respuesta está más abajo
        else:
            idx_max = idx_mean-1
    # la respuesta está arriba
    else:
        idx_min = idx_mean+1


