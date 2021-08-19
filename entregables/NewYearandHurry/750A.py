n, k = map(int,input().split())

contest_time = 4 * 60
time_limit = contest_time-k

a = 0
b = n

while(a<=b):
    c = (a+b)//2
    #sumatoria de suceciones
    work_time = c*5+(5*c*(c-1))//2
    if(work_time<=time_limit):
        #hago un problema más
        possible_work_time = (c+1)*5+(5*(c+1)*((c+1)-1))//2
        #si puedo, el límite está arriba
        if(possible_work_time<=time_limit):
            a=c+1
        else:
            break
    else:
        b=c-1
print(c)
