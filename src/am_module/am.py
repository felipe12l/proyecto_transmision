import numpy as np
import matplotlib.pyplot as plt


def am_modulate(baseband_signal, t, carrier_freq=100, bias=0.5, modulation_index=0.5):
    """
    Aplica modulación de amplitud (AM) a una señal baseband.

    Parámetros:
      - baseband_signal: Vector de la señal digital (en niveles 0 y 1).
      - t: Vector de tiempo correspondiente.
      - carrier_freq: Frecuencia de la portadora en Hz.
      - bias: Desplazamiento DC que asegura que la envolvente sea positiva.
      - modulation_index: Factor de modulación que escala la señal base.

    Retorna:
      - modulated_signal: La señal modulada en AM.
    """
    # Calcular la envolvente: se suma un bias para que la señal nunca sea negativa
    envelope = bias + modulation_index * baseband_signal
    # Generar la portadora sinusoidal
    carrier = np.cos(2 * np.pi * carrier_freq * t)
    # Señal AM
    modulated_signal = envelope * carrier
    return modulated_signal


def am_modulate_analog(analog_signal, t, carrier_freq=100, bias=0.5, modulation_index=0.5):
    envelope = bias + modulation_index * analog_signal
    carrier = np.cos(2 * np.pi * carrier_freq * t)
    modulated_signal = envelope * carrier
    return modulated_signal


if __name__ == '__main__':
    # Ejemplo de prueba: generar una onda baseband digital simple (onda cuadrada)
    fs = 1000  # Frecuencia de muestreo
    t = np.linspace(0, 1, fs, endpoint=False)
    # Crear una señal digital simple: por ejemplo, bits alternados
    # baseband = np.where((t * 10 % 1) < 0.5, 0, 1)

    # mod_signal = am_modulate(
    #    baseband, t, carrier_freq=100, bias=0.5, modulation_index=0.5)

    # Ejemplo de señal analógica: una onda senoidal normalizada para oscilar entre 0 y 1.
    # Se genera una señal con frecuencia 3 Hz.
    analog_signal = (np.sin(2 * np.pi * 3 * t) + 1) / 2
    # Aplicar modulación AM a la señal analógica
    mod_signal = am_modulate_analog(
        analog_signal, t, carrier_freq=100, bias=0.5, modulation_index=0.5)

    plt.figure(figsize=(10, 4))
    plt.plot(t, mod_signal, label="Señal AM")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Amplitud")
    plt.title("Ejemplo de modulación AM")
    plt.legend()
    plt.grid(True)
    plt.show()
