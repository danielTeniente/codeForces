numbers = map(int,input().split())

diff_sh = []
buy_new = 0

for num in numbers:
    if(num in diff_sh):
        buy_new+=1
    else:
        diff_sh.append(num)
print(buy_new)