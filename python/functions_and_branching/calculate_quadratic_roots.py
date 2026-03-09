from numpy.lib.scimath import sqrt

def calculate_quadratic_roots(a, b, c):

    quadratic_root_positive = (-b + (sqrt(b**2-4*a*c)))/2*a
    quadratic_root_negative = (-b - (sqrt(b**2-4*a*c)))/2*a

    if quadratic_root_negative == quadratic_root_positive:
        return quadratic_root_positive
    else:
        quadratic_roots = [quadratic_root_negative, quadratic_root_positive]

        return quadratic_roots

    

print(f'x^2 + 2x + 1 = 0: x = 1      ; calculate_quadratic_roots(1, 2, 1) = {calculate_quadratic_roots(1., 2., 1.)}')

print(f'x^2 - 2x + 1 = 0: x = 3, -1. ; calculate_quadratic_roots(1, -2, -3) = {calculate_quadratic_roots(1., -2., -3.)}')

print(f'x^2 + 0x + 1 = 0: x = i, -i  ; calculate_quadratic_roots(-2, 2, -1) =  {calculate_quadratic_roots(-2, 2, -1)}')
 
