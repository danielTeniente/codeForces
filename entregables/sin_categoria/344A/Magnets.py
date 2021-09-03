# Daniel

import sys

cin = iter(sys.stdin.read().split())

n = int(next(cin))
counter = 1
last_pointer = next(cin)[1]

for _ in range(n-1):
    new_magnet = next(cin)
    new_pointer = new_magnet[0]
    if(last_pointer==new_pointer):
        counter+=1
    last_pointer = new_magnet[1]
print(counter)
