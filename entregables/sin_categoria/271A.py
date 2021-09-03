# Beautiful Year

is_beautiful_year = False
y = int(input())
idx = y+1

while(not is_beautiful_year):
    used_numbers = []
    digits = list(str(idx))

    for num in digits:
        if(num in used_numbers):
            break
        used_numbers.append(num)

    if(len(used_numbers)==len(digits)):
        is_beautiful_year=True

    idx += 1

beaut_year = ''
for num in used_numbers:
    beaut_year+=num
print(beaut_year)
    




