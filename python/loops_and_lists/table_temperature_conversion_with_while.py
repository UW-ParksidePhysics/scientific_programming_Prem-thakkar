import numpy as numpy


Fahrenheit = 0
print(f'Starting Fahrenheit:{Fahrenheit}')
print(f'F:C')

Fahrenheit_step = 10

while Fahrenheit < 100:
    Celcius = 9/5*(Fahrenheit) - 32
    print(Fahrenheit, Celcius)
    Fahrenheit += Fahrenheit_step

print(f'Ending Fahrenheit:{Fahrenheit}')

