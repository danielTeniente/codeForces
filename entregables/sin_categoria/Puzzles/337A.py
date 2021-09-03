n,m = map(int,input().split())


puzzles = list(map(int,input().split()))
puzzles = sorted(puzzles,reverse=True)

min_diff = 10000000

for i in range(m-n+1):
    l_pointer = i+n-1
    diff = puzzles[i]-puzzles[l_pointer]
    if(diff<min_diff):
        min_diff=diff

print(min_diff)


