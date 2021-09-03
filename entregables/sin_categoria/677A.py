# A. Vanya and Fence
n,h = map(int,input().split())

number_list = map(int,input().split())
w=0

for h_i in number_list:
    if(h_i>h):
        w+=2
    else:
        w+=1

print(w)
