# Expression

a = int(input())
b = int(input())
c = int(input())

maximum = a+b+c
maximum = max((a+b)*c,maximum)
maximum = max(a*(b+c),maximum)
maximum = max(a*b*c,maximum)

print(maximum)