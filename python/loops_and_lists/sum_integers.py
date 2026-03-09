maximum_integer = 20
initial_integer = 0

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
initial_number = 0

for i in range (initial_integer, maximum_integer + 1):
    print(f'n = {i}')

for number in numbers:
    initial_number += number

print(f'sum(1,n) = {initial_number}')

famous_formula = (maximum_integer * (maximum_integer + 1))/2

print(f'n(n+1)/2 = {famous_formula}')


