## CodeForces
# A. Domino piling

def max_dom(n,m):
    return n*m//2

def main():
    (n,m) = input().split()
    n = int(n)
    m = int(m)
    print(max_dom(n,m))

if __name__ == '__main__':
    main()