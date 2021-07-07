## CodeForces
# A. Theatre Square

def get_num_flagstones(n,m,a):
    side1 = n//a
    if(n%a!=0):
        side1+=1
    side2 = m//a
    if(m%a!=0):
        side2+=1    
    return(side1*side2)


def main():
    input_str = input()
    (n,m,a) = input_str.split()
    n = int(n)
    m = int(m)
    a = int(a)

    print(get_num_flagstones(n,m,a))

if __name__ == '__main__':
    main()
