# Word

word = input()
counter=0

for char in word:
    if(char.isupper()):
        counter+=1
if(counter>len(word)-counter):
    print(word.upper())
else:
    print(word.lower())