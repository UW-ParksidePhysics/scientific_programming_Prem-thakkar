import numpy as np
import math 

mean_m = 0
standard_deviation_s = 2
input_value_x = 1

function_x = (1/(math.sqrt(2pi)*standard_deviation_s))**[(-1/2)((input_value_x - mean_m)/standard_deviation_s)**2] 

print(f'Mean:{mean_m}')
print(f'Standard Deviation:{standard_deviation_s}')
print(f'Input Value:{input_value}')
#print(f'Result:{function_x}')