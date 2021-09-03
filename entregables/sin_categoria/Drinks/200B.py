n = int(input())
numbers = map(int,input().split())

suma = 0
for num in numbers:
    suma+=num

print(suma/n)