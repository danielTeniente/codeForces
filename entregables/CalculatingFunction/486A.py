n = int(input())

even = 0
odd = 0

if(n%2==0):
    even = odd = n//2
else:
    odd = n//2+1
    even = odd-1

d=2

odd_sum=odd*1+d*odd*(odd-1)//2
even_sum=even*2+d*even*(even-1)//2

print(even_sum-odd_sum)