import matplotlib.pyplot as plt

def parse_sum_output(filename):
    tolerances = []
    errors = []
    maximum_indices = []

    infile = open(filename, "r")

    for line in infile:
        if "epsilon" in line:
            parts = line.strip().split(",")

            epsilon = float(parts[0].split(":")[1].strip())
            error = float(parts[1].split(":")[1].strip())
            n = int(parts[2].split("=")[1].strip())

            tolerances.append(epsilon)
            errors.append(error)
            maximum_indices.append(n)

    infile.close()
    return tolerances, errors, maximum_indices


def plot_logarithmic_sum_error(tolerances, errors, maximum_indices):
    plt.semilogy(maximum_indices, tolerances, "o-")
    plt.semilogy(maximum_indices, errors, "s-")
    plt.xlabel("maximum index (n)")
    plt.ylabel("tolerance / error")
    plt.show()


if __name__ == "__main__":
    tolerances, errors, maximum_indices = parse_sum_output("logarithmic_sum.out")
    plot_logarithmic_sum_error(tolerances, errors, maximum_indices)