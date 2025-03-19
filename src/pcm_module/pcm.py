from matplotlib import pyplot as plt
import numpy as np

def pcm(values, M, pol_one = 1):

    n_bits = int(np.log2(M))

    min_value = np.min(values)
    max_value = np.max(values)
    levels = np.linspace(min_value, max_value, M)
    pcm_values = np.array([np.argmin(np.abs(levels - v)) for v in values])


    bin_array = [format(num, f'0{n_bits}b') for num in pcm_values]
    bit_stream = [int(bit) for binary in bin_array for bit in binary]

    polar_signal = [pol_one if bit == 1 else -pol_one for bit in bit_stream]
    return polar_signal


def plot_polar_square_wave(bit_stream, bit_duration_ms=1):
    """Grafica la señal cuadrada polar"""
    num_bits = len(bit_stream)
    t = np.linspace(0, num_bits * bit_duration_ms, num_bits, endpoint=False)

    fig, ax = plt.subplots(figsize=(15, 5))
    line, = ax.step(t, bit_stream, where='post', linewidth=1.5, color='b')

    # Agregar puntos rojos en cada bit
    ax.scatter(t + bit_duration_ms / 2, bit_stream, color='red', zorder=3)

    ax.set_ylim(-1.5, 1.5)
    ax.set_xlabel("Tiempo (ms)")
    ax.set_ylabel("Amplitud")
    ax.set_title("Códificación PCM")
    ax.grid(True, linestyle="--", alpha=0.6)
    ax.legend()


    window_size = 50  # Cantidad de bits visibles
    start = 0
    ax.set_xlim(start, start + window_size)


    def update_view(start):
        ax.set_xlim(start, start + window_size)
        plt.draw()


    def on_key(event):
        nonlocal start
        step = 10
        if event.key == "right":
            start = min(start + step, num_bits - window_size)
        elif event.key == "left":
            start = max(start - step, 0)
        update_view(start)

    def on_scroll(event):
        nonlocal start
        step = 5
        if event.step > 0:
            start = max(start - step, 0)  # Desplazarse a la izquierda
        else:
            start = min(start + step, num_bits - window_size)  # Derecha
        update_view(start)

    fig.canvas.mpl_connect("key_press_event", on_key)
    fig.canvas.mpl_connect("scroll_event", on_scroll)

    plt.show()