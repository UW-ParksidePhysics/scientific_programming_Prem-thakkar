#density (g/cm^3) = mass/vol 
#mass = density*vol
volume = 1000 #cm^3 1L=1000mL, 1mL=1cm^3


iron_mass = 7.870*volume
air_mass = 0.0012*volume
gasoline_mass = .755*volume
ice_mass = .9167*volume
h_bod_mass = .985*volume
silver_mass = 10.500*volume
platinum_mass = 21.450*volume

print(f'Element Mass(grams) Iron:{iron_mass:.2f} Air:{air_mass:.2f} Ice:{ice_mass:.2f} Silver:{silver_mass:.2f} Platinum:{platinum_mass:.2f}')
print(f'Human Body Mass(grams) = {h_bod_mass:.2f}')
print(f'Gasoline Mass(grams) = {gasoline_mass:.2f}')