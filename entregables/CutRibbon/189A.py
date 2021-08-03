n, a, b, c = map(int, input().split())

#se debe maximizar x+y+z
#en la ecuación ax+by+cz = n
max_cuts = 0
if(a==1 or b==1 or c==1):
    max_cuts = n
elif(a==b):
    #recorro posibles ax
    for ax in range(0,n+1,a):
        by = 0
        #encuentro Z y debe ser entero
        z = (n-ax-by)//c
        #si z no es entero la relación no se cumple
        if(ax+by+c*z==n):
            x = ax//a
            y = by//b
            max_cuts = max(max_cuts,x+y+z)

else:
    #recorro posibles ax
    for ax in range(0,n+1,a):
        #recorro posibles by quitando ax
        for by in range(0,n-ax+1,b):
            #encuentro Z y debe ser entero
            z = (n-ax-by)//c
            #si z no es entero la relación no se cumple
            if(ax+by+c*z==n):
                x = ax//a
                y = by//b
                max_cuts = max(max_cuts,x+y+z)

print(max_cuts)
