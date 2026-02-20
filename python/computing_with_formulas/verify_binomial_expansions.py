a = 3.3 
b=5.3 
a_two = a**2
b_two = b**2

binomial_sum_squared_terms = a_two + 2*a*b + b_two
binomial_difference_squared_terms = a_two - 2*a*b + b_two
binomial_sum_squared = (a + b)**2
binomial_difference_squared = (a - b)**2

print(f'First equation:  {binomial_sum_squared:.1f} = {binomial_sum_squared_terms:.1f}')
print(f'Second equation: {binomial_difference_squared:.1f} = {binomial_difference_squared_terms:.1f}')
              