nearby_star_data = [
('Alpha Centauri A', 4.3, 0.26, 1.56),
('Alpha Centauri B', 4.3, 0.077, 0.45),
('Alpha Centauri C', 4.2, 0.00001, 0.00006),
("Barnard's Star", 6.0, 0.00004, 0.0005),
('Wolf 359', 7.7, 0.000001, 0.00002),
('BD +36 degrees 2147', 8.2, 0.0003, 0.006),
('Luyten 726-8 A', 8.4, 0.000003, 0.00006),
('Luyten 726-8 B', 8.4, 0.000002, 0.00004),
('Sirius A', 8.6, 1.00, 23.6),
('Sirius B', 8.6, 0.001, 0.003),
('Ross 154', 9.4, 0.00002, 0.0005)
]

def convert_list_of_tuples(data):
    stars = {}

    for item in data:
        name = item[0]
        stars[name] = {
            "distance": item[1],
            "apparent brightness": item[2],
            "luminosity": item[3]
        }

    return stars


def print_star_information(name, stars):
    print("Star:", name)
    print("    Distance (ly):", stars[name]["distance"])
    print("    Apparent brightness (m):", stars[name]["apparent brightness"])
    print("    Luminosity (L_sun):", stars[name]["luminosity"])
    print()


if __name__ == "__main__":
    stars = convert_list_of_tuples(nearby_star_data)

    print_star_information("Sirius A", stars)
    print_star_information("Alpha Centauri B", stars)