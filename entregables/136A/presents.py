# Presents
import sys

cin = iter(map(int,sys.stdin.read().split()))

n = next(cin)
final_list = [0]*n

for i in range(n):
    number = next(cin)
    final_list[number-1]=i+1

for num in final_list:
    print(num,end=' ')


