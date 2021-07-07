# CodeForces
# A. Way Too Long Words

n = int(input())
for i in range(n):
    string = input()
    if(len(string)>10):
        firstChar = string[0]
        lastChar = string[-1]
        middleLen = len(string[1:-1])
        final_word = firstChar+str(middleLen)+lastChar
    else:
        final_word = string
    print(final_word)