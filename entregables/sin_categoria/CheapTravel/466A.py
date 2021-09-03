
n, m, a, b= map(int,input().split())

pay_all = n*a
if(m>n):
    pay_m = b
else:
    tickets = n//m
    pay_m = tickets*b
    extra = n-tickets*m
    pay_m = min(pay_m+extra*a,pay_m+b)

print(min(pay_all,pay_m))