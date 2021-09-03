bin_num = list(bin(int(input())))[2:]
count = 0

for char in bin_num:
    if(char == '1'):
        count+=1

print(count)