n = int(input())

p_s = input().split()
p = int(p_s[0])

be_the_guy = True
levels_x = []
levels_y = []


if(p!=0):
    levels_x = list(map(int,p_s[1:]))
    
p_s = input().split()
p = int(p_s[0])
if(p!=0):
    levels_y = list(map(int,p_s[1:]))

all_together = sorted(levels_x+levels_y)


for i in range(1,n+1):
    if(i not in all_together):
        be_the_guy=False
        break

if(be_the_guy):
    print('I become the guy.')
else:
    print('Oh, my keyboard!')

