a,b = map(int,input().split())
diff_pairs = min(a,b)
same_pairs = (max(a,b)-diff_pairs)//2
print(diff_pairs,same_pairs)