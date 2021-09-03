n = int(input())
string = input().lower()

str_keys = ''
counter=0

for i,char in enumerate(string):
    if(i%2==0):
        str_keys+=char
    else:
        if(char in str_keys):
            str_keys = str_keys.replace(char,'',1)
        else:
            counter+=1
print(counter)