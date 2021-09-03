bin1 = input()
bin2 = input()

word = ''
for i in range(len(bin1)):
    if(bin1[i]==bin2[i]):
        word+='0'
    else:
        word+='1'

print(word)