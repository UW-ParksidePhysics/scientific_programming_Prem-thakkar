import math

def gaussian(position):
    return (1 / math.sqrt(2 * math.pi)) * math.exp(-0.5 * position**2)

if __name__ == "__main__":
    positions = []
    gaussian_values = []

    # 41 points from -4 to 4
    for i in range(41):
        x = -4 + i * (8 / 40)   # step = 0.2
        positions.append(x)
        gaussian_values.append(gaussian(x))

    print("positions =", positions)
    print("gaussian_values =", gaussian_values)