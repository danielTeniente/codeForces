# el programa suma el número de lados de una figura

#función que retorna el número de lados
def get_num_sides(figure=''):
    #filtra el valor de acuerdo a la palbra recibida
    if(figure=='Tetrahedron'):
        return 4
    if(figure=='Cube'):
        return 6
    if(figure=='Octahedron'):
        return 8 
    if(figure=='Dodecahedron'):
        return 12
    if(figure=='Icosahedron'):
        return 20

n = int(input())
total_sum = 0
for _ in range(n):
    total_sum+=get_num_sides(input())
print(total_sum)
    
