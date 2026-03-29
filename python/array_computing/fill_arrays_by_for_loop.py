import math

def gaussian(x):
    return (1 / math.sqrt(2 * math.pi)) * math.exp(-0.5 * x**2)

if __name__ == "__main__":
    x_values = []
    y_values = []

    for i in range(41):
        x = -4 + i * (8 / 40)
        x_values.append(x)
        y_values.append(gaussian(x))

    print("x_values =", x_values)
    print("y_values =", y_values)