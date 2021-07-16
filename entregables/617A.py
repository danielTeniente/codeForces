# A. Elephant

x = int(input())

paso = 5

pasos = x//5

if(pasos*5<x):
    pasos+=1
print(pasos)