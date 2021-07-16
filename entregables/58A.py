word = input() 
example = 'hello'
idx = 0

for char in word:
    if(example[idx]==char):
        idx+=1
    if(idx==len(example)):
        break

if(idx==len(example)):
    print('YES')
else:
    print('NO')