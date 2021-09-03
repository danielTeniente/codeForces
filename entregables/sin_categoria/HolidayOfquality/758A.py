n = int(input())
numbers = list(map(int,input().split()))
current_welfare = sum(numbers)
print(max(numbers)*n-current_welfare)