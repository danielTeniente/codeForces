# Even Odds

n,k = map(int,input().split())

if(n%2==0):
    m_1 = n//2
else:
    m_1 = n//2+1

if(k>m_1):
    idx = k-m_1
    print(2*idx)
else:
    print(2*(k-1)+1)
