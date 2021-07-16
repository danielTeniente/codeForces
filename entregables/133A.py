# A. HQ9+
word = input()

instructions = 'HQ9'
some_output = False

for char in word:
    if(char in instructions):
        print('YES')
        some_output=True
        break

if(not some_output):
    print('NO')

    