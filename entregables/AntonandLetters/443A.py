string = input().replace('{','').replace('}','').replace(' ','')

if(string):
    count = 1
    if(len(string)>1):
        string_list = sorted(string.split(','))
        for i in range(1,len(string_list)):
            
            if(string_list[i]!=string_list[i-1]):
                count+=1
else:
    count = 0
print(count)