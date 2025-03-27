import numpy as np
import matplotlib.pyplot as plt


def am_modulate_analog(analog_signal, t, carrier_freq=100, bias=0.5, modulation_index=0.5):
    envelope = bias + modulation_index * analog_signal
    carrier = np.cos(2 * np.pi * carrier_freq * t)
    modulated_signal = envelope * carrier
    return modulated_signal


if __name__ == '__main__':
    # Ejemplo de prueba: generar una onda baseband digital simple (onda cuadrada)
    fs = 1000  # Frecuencia de muestreo
    t = np.linspace(0, 1, fs, endpoint=False)

    # Ejemplo de señal analógica: una onda senoidal normalizada para oscilar entre 0 y 1.
    # Se genera una señal con frecuencia 3 Hz. Al sumarle 1 y dividir por 2 para normalizarla
    analog_signal = (np.sin(2 * np.pi * 3 * t) + 1) / 2
    # Aplicar modulación AM a la señal analógica
    mod_signal = am_modulate_analog(
        analog_signal, t, carrier_freq=100, bias=0.5, modulation_index=0.5)

    plt.figure(figsize=(10, 4))
    plt.plot(t, mod_signal, label="Señal AM")
    # plt.plot(t, analog_signal, label="Señal analógica")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Amplitud")
    plt.title("Ejemplo de modulación AM")
    plt.legend()
    plt.grid(True)
    plt.show()
