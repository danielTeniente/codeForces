n,t = map(int,input().split())

books = list(map(int,input().split()))

max_count = 0
i=0
j=0
#tomo el primer libro
reading_time = books[i]

while(j<n):
    #está dentro del límite
    if(reading_time>t):
        #muevo ventana
        reading_time-=books[i]
        i+=1
    else:
        len_books = j-i+1
        max_count = max(max_count,len_books)
    #la ventana crece        
    j+=1
    if(j<n):
        reading_time+=books[j]

print(max_count)