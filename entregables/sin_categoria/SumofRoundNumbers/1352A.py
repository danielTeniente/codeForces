t = int(input())
for _ in range(t):
    n = int(input())
    terms = []
    for i in range(4,-1,-1):
        round_num = n//10**i*10**i
        n-=round_num
        terms.append(round_num)
    round_list = [num for num in terms if num!=0]
    print(len(round_list))
    for num in round_list:
        print(num,end=' ')
    print('\n',end='')
    