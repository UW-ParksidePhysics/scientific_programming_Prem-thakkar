import numpy as numpy


Fahrenheit = 0
print(f'Starting Fahrenheit:{Fahrenheit}')
print(f'F:C:C_aprox')

Fahrenheit_step = 10

while Fahrenheit < 100:
    Celcius = 9/5*(Fahrenheit) - 32
    Celcius_hat = (Fahrenheit - 30)/2
    print(Fahrenheit, Celcius, Celcius_hat)
    Fahrenheit += Fahrenheit_step

print(f'Ending Fahrenheit:{Fahrenheit}')
