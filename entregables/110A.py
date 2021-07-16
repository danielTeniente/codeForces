#  Nearly Lucky Number

from typing import Counter


n = map(int,list(input()))
counter = 0

for digit in n:
    if(digit==4 or digit==7):
        counter+=1

if(counter==4 or counter==7):
    print('YES')
else:
    print('NO')