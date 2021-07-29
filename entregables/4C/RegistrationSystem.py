n = int(input())
names = {}

for _ in range(n):
    word = input()
    try:
        names[word]+=1
        print(word+str(names[word]))
    except:
        names[word]=0
        print('OK')

