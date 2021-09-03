n =int(input())

hate = 'I hate '
love = 'I love '
midd = 'that '
end ='it'
expression = hate

for i in range(1,n):
    expression+=midd
    if(i%2==0):
        expression+=hate
    else:
        expression+=love
    
print(expression+end)