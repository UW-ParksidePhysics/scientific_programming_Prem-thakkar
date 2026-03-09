earth_times = [0.00, 0.11, 0.23, 0.34, 0.45, 0.57, 0.68, 0.79, 0.91, 1.02] #seconds
earth_positions = [0.00, 0.09, -9.62, -29.15, -58.48, -97.62, -146.58, -205.34, -273.92, -352.31]

moon_times = [0.00, 0.68, 1.36, 2.04, 2.73, 3.41, 4.09, 4.77, 5.45, 6.13]
moon_positions = [0.00, 4.19, 6.74, 7.67, 6.96, 4.62, 0.66, -4.93, -12.16, -21.02]

print (f'    Earth')
print(13*'-')

print (f'{"t(s)":>5} {"y(m)":>5}')
print (f'{"----":>5} {"----":>5}')

for times, p in zip(earth_times, earth_positions):
    print(f'{times:.2f}, {p:.2f}')

print (13*'-')
print (f'    Moon')
print(13*'-')

print (f'{"t(s)":>5} {"y(m)":>5}')
print (f'{"----":>5} {"----":>5}')

for t, positions in zip(moon_times, moon_positions):
    print(f'{t:.2f},  {positions:.2f}')

print (13*'-')
