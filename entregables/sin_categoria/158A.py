## CodeForces
# A. Next Round

# recorrer los valores hasta llegar a un cero
# o encontrar valores menores a k

(n,k) = input().split()
n = int(n)
k = int(k)

#lista de numeros
points = input().split()

counter = 0
min_point = int(points[k-1])
flag = False

for i in range(k):
    if(int(points[i])!=0):
        counter+=1
    else:
        flag = True
        break

if(not flag):
    for i in range(k,len(points)):
        if(int(points[i])==min_point):
            counter+=1
        else:
            break
print(counter)