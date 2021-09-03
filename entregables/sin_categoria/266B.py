# Queue at the School

n,t= map(int, input().split())
q = input()
for i in range(t):
    new_q = list(q)
    for j in range(1,n):
        if(q[j]=='G' and q[j-1]=='B'):
            new_q[j]='B'
            new_q[j-1]='G'
    q = new_q
    
new_q = ''
for char in q:
    new_q+=char
print(new_q)
            
