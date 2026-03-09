def compute_heaviside_function(x):
    if x < 0:
        return 0
    else:
        return 1
    
print(f'compute_heaviside_function(-10) = {compute_heaviside_function(-10)}')
print(f'compute_heaviside_function(-10-15) = {compute_heaviside_function(-10 - 15)}')
print(f'compute_heaviside_function(0) = {compute_heaviside_function(0)}')
print(f'compute_heaviside_function(10-15) = {compute_heaviside_function(10-15)}')
print(f'compute_heaviside_function(10) = {compute_heaviside_function(10)}')
