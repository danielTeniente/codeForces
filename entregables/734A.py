# Anton and Danik
n = int(input())
str_input = input()

anton_ctr = 0
for char in str_input:
    if(char == 'A'):
        anton_ctr+=1

if(anton_ctr>n-anton_ctr):
    print('Anton')
elif(anton_ctr<n-anton_ctr):
    print('Danik')
else:
    print('Friendship')