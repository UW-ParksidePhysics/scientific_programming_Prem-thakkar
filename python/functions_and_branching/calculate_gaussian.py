#sigma = 2
#n= 2
#x_bar = 4
from math import pi, exp, sqrt

x_minus = []
x_plus = []
sigma = 2
x_bar = 100
n = 2

def compute_gaussian_function(x):
    return(1/sqrt(2*pi*sigma))*exp((-0.5)*((x-x_bar)/sigma)**2)

print(25*'-')
print(f'    Gaussian Function   ') #table title
print(25*'-')

print(f'{"x":>7} {"f(x)":>11}')
print(f'{"-----":>9} {"--------":>11}')

for x in range(int(x_bar-5*sigma), (x_bar+5*sigma)+1, n):
    print (f'{x:>8} {compute_gaussian_function(x):>12.6f}')

print(25*'-')
