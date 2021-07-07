## CodeForces
# A. String Task

vowels = 'aeiouy'
vowels += vowels.upper()

input_string = input()
new_str = ''

for char in input_string:
    if(char not in vowels):
        new_str+='.'+char.lower()


print(new_str)
    
