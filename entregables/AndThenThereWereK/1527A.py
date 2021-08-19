t = int(input())

for _ in range(t):
    n = int(input())
    if(n==1):
        print(0)
        continue
    bin_num = bin(n)
    k = '0b'
    for i in range(len(bin_num)-3):
        k+='1'
    print(int(k,2))
