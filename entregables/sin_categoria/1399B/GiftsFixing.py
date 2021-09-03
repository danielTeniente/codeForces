t = int(input())
for _ in range(t):
    n = int(input())
    a_presents = list(map(int,input().split()))
    b_presents = list(map(int,input().split()))
    min_a = min(a_presents)
    min_b = min(b_presents)
    counter = 0
    for i in range(n):
        diff = min(a_presents[i]-min_a,
                    b_presents[i]-min_b)
        counter+=diff
        a_presents[i]-=diff
        b_presents[i]-=diff
        if(a_presents[i]>min_a):
            counter+=(a_presents[i]-min_a)
        else:
            counter+=(b_presents[i]-min_b)

        
    print(counter)

