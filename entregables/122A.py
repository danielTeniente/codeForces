# Lucky Division

lucky_numbers = [4,7]

for i in range(10,778):
    is_lucky = True
    word = str(i)
    for char in word:
        if (int(char) not in lucky_numbers):
            is_lucky = False
    if(is_lucky):
        lucky_numbers.append(i)

n = int(input())

is_psLucky = False
for luckyNum in lucky_numbers:
    if(n%luckyNum==0):
        is_psLucky = True
        break

if(is_psLucky):
    print('YES')
else:
    print('NO')




