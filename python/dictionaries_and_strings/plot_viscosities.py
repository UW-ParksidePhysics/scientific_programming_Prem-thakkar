import matplotlib.pyplot as plt

def parse_viscosity_data(filename):
    data = {}
    file = open(filename, "r")

    for line in file:
        parts = line.split()

        if len(parts) == 4:
            name = parts[0]
            C = float(parts[1])
            T0 = float(parts[2])
            mu0 = float(parts[3])

            data[name] = {
                "viscosity": C,
                "reference_temperature": T0,
                "reference_viscosity": mu0
            }

    file.close()
    return data


def calculate_viscosity(T, gas, data):
    C = data[gas]["viscosity"]
    T0 = data[gas]["reference_temperature"]
    mu0 = data[gas]["reference_viscosity"]

    mu = mu0 * ((T / T0) ** 1.5) * ((T0 + C) / (T + C))
    return mu


def plot_viscosity(data):
    temps = list(range(200, 1001, 50))

    for gas in ["air", "carbon_dioxide", "hydrogen"]:
        values = []
        for T in temps:
            values.append(calculate_viscosity(T, gas, data))

        plt.plot(temps, values, label=gas)

    plt.xlabel("Temperature (K)")
    plt.ylabel("Viscosity")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    viscosity_data = parse_viscosity_data("viscosity_of_gases.dat")
    plot_viscosity(viscosity_data)