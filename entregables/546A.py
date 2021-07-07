# Soldier and Bananas

(k,n,w) = input().split(' ')
k = int(k)
n = int(n)
w = int(w) 

pago = w*(1+w)/2*k

if(n<pago):
    print(int(pago-n))
else:
    print(0)