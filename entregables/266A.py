## CodeForces
# A. Stones on the Table

n = int(input())
str_list = input()
new_str = ' '
moves = 0

for i in range(n):
    if(new_str[-1]!=str_list[i]):
        new_str+=str_list[i]
    else:
        moves+=1

print(moves)