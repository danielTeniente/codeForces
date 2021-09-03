#el programa verificará que las letras mezcladas
#puedan generar los dos nombres de arriba

name1 = input()
name2 = input()
shuffle  = input()

#se juntan las letras de los dos nombres
# y se ordena para comprobar
# que se pueda generar a partir de la mezcla
all_letters = sorted(name1+name2)
print('YES') if(all_letters==sorted(shuffle)) else print('NO')

