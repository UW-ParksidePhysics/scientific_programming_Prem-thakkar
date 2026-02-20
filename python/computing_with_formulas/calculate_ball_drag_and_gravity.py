#forces N = (kg*m)/s^2
from math import pi
import numpy as np

drag_coefficient = 0.2            #C_d
air_density = 1.2                 #(rho) kg/m^3
radius_a = .11                    #meters
cross_area = pi*(radius_a)**2     #A = (pie)a^2

conversion = .277                 #km/hr to m/s
hard_kick = 120*conversion
soft_kick = 10*conversion
ball_velocity = np.array([hard_kick,soft_kick]) #m/s)

ball_mass = .43                   #kg

#forces
gravitational_acceleration = 9.81 #m/s^2
gravitational_force = ball_mass*gravitational_acceleration #F_d = ma
print(f'Gravitational Force:{gravitational_force:.1f} Newtons')

drag_force = 1/2*(drag_coefficient*air_density*cross_area)*(ball_velocity**2) #F_d
print(f'Drag force from [hard kick,soft kick]:{drag_force} Newtons')