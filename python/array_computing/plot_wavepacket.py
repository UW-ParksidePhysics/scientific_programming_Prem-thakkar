import numpy as np
import matplotlib.pyplot as plt

def f(x, t, alpha, freq, k, omega):
    return np.exp(-(alpha * x - freq * t) ** 2) * np.sin(k * x - omega * t)

if __name__ == "__main__":
    t = 0
    f_value = 3
    k = 3 * np.pi
    omega = 3 * np.pi

    x = np.linspace(-4, 4, 1001)

    alpha_values = [0.5, 1, 2]

    for alpha in alpha_values:
        y = f(x, t, alpha, f_value, k, omega)
        plt.plot(x, y, label=f"alpha = {alpha}")

    plt.xlabel("x")
    plt.ylabel("f(x,t)")
    plt.title("Wave Packet at t = 0")
    plt.legend()
    plt.grid(True)
    plt.show()