import numpy as np
import matplotlib.pyplot as plt

def gaussian(x):
    return (1 / np.sqrt(2 * np.pi)) * np.exp(-0.5 * x**2)

if __name__ == "__main__":
    x = np.linspace(-4, 4, 41)
    y = gaussian(x)

    plt.plot(x, y)
    plt.xlabel("x")
    plt.ylabel("g(x)")
    plt.title("Gaussian Function")
    plt.grid()
    plt.show()