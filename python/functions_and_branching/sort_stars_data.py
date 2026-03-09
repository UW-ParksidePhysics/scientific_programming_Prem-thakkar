import numpy as np

nearby_stars_data = [
('Alpha Centauri A',    4.3,  0.26,      1.56),
('Alpha Centauri B',    4.3,  0.077,     0.45),
('Alpha Centauri C',    4.2,  0.00001,   0.00006),
("Barnard's Star",      6.0,  0.00004,   0.0005),
('Wolf 359',            7.7,  0.000001,  0.00002),
('BD +36 degrees 2147', 8.2,  0.0003,    0.006),
('Luyten 726-8 A',      8.4,  0.000003,  0.00006),
('Luyten 726-8 B',      8.4,  0.000002,  0.00004),
('Sirius A',            8.6,  1.00,      23.6),
('Sirius B',            8.6,  0.001,     0.003),
('Ross 154',            9.4,  0.00002,   0.0005), 
]

by_distance = sorted(nearby_stars_data, key=lambda x: x[1])
print("distance:")
print(f"{'name':<10}  {'distance':<10}")
for s in by_distance:
    print(f"{s[0]:<10}  {s[1]:<10}")

by_luminosity = sorted(nearby_stars_data, key=lambda x: x[3], reverse=True)
print("\n luminosity:")
print(f"{'name':<10}  {'luminosity':<10}")
for s in by_luminosity:
    print(f"{s[0]:<10}  {s[3]:<10}")

by_brightness = sorted(nearby_stars_data, key=lambda x: x[2], reverse=True)
print("\n brightness:")
print(f"{'name':<10}  {'brightness':<10}")
for s in by_brightness:
    print(f"{s[0]:<10}  {s[2]:<10}")