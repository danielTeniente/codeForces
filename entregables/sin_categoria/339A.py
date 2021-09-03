## CodeForces
# A. Helpful Maths

sum_list = input().replace('+','')
sum_list = sorted(sum_list)
final_sum = ''
for i in range(len(sum_list)-1):
    final_sum+=sum_list[i]+'+'
print(final_sum+sum_list[len(sum_list)-1])

