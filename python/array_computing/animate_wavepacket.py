import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

def f(x, t, alpha, freq, k, omega):
    return np.exp(-(alpha * x - freq * t) ** 2) * np.sin(k * x - omega * t)

if __name__ == "__main__":
    alpha = 1
    freq = 3
    k = 3 * np.pi
    omega = 3 * np.pi

    x = np.linspace(-6, 6, 1001)
    t_values = np.linspace(-1, 1, 61)

    fig, ax = plt.subplots()
    line, = ax.plot([], [], lw=2)

    ax.set_xlim(-6, 6)
    ax.set_ylim(-1.1, 1.1)
    ax.set_xlabel("x")
    ax.set_ylabel("f(x,t)")
    ax.set_title("Animated Wave Packet")
    ax.grid(True)

    def init():
        line.set_data([], [])
        return line,

    def update(frame):
        t = t_values[frame]
        y = f(x, t, alpha, freq, k, omega)
        line.set_data(x, y)
        ax.set_title(f"Animated Wave Packet, t = {t:.2f}")
        return line,

    anim = FuncAnimation(
        fig,
        update,
        frames=len(t_values),
        init_func=init,
        blit=True
    )

    anim.save("wavepacket.gif", writer=PillowWriter(fps=6))
    plt.show()