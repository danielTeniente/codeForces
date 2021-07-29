# cAPS lOCK

word = input()
new_word=''

if(word[1:].isupper() or len(word)==1):
    for char in word:
        if(char.isupper()):
            new_word+=char.lower()
        else:
            new_word+=char.upper()
else:
    new_word=word
    
print(new_word)
