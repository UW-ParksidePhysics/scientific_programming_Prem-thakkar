#distance in kilometers
km_in =1000*100*(1/2.54)
d1 = 19.47
d1_inch = d1*km_in
d1_feet = d1_inch/12
d1_yards = d1_feet/3
d1_miles = d1_feet/5280

d = .640 
inch = d*km_in 
feet = inch/12 
yards = feet/3 
miles = feet/5280
print(f'Test measurement:{d}km is {inch:.2f}in, {feet:.2f}ft, {yards:.2f}yds and {miles:.2f}mi.')
print(f'My distance is {d1}km; which is {d1_inch:.2f}in, {d1_feet:.2f}ft, {d1_yards:.2f}yds, and {d1_miles:.2f}mi.')

