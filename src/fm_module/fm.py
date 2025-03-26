import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as waves

def fm_modulate(file: str, A: float = 1.0, fc: int = 1000, delta_f: int = 800, fs: int = 10000):
    # Leer el archivo de audio
    sampling, sound = waves.read(file)
    sound = sound[:, 0]  # Usar solo el primer canal si es estéreo

    # Normalizar la señal moduladora
    modulating_signal = sound / np.max(np.abs(sound))

    # Calcular el índice de modulación
    beta = delta_f / np.max(np.abs(modulating_signal))

    # Crear el tiempo para la señal portadora
    t = np.linspace(0, len(modulating_signal) / sampling, len(modulating_signal), endpoint=False)

    # Señal portadora
    carrier_signal = A * np.cos(2 * np.pi * fc * t)

    # Implementar la modulación FM con el signo invertido
    modulated_signal = A * np.cos(2 * np.pi * fc * t - 2 * np.pi * beta * np.cumsum(modulating_signal) / sampling)

    # Crear una figura con subplots
    fig, axs = plt.subplots(3, 1, figsize=(10, 6))  # Ajustar la altura de la ventana

    # Graficar la señal moduladora
    axs[0].plot(t, modulating_signal)
    axs[0].set_xlabel('t (segundos)')
    axs[0].set_ylabel('Amplitud')
    axs[0].set_title('Señal Moduladora (Datos)')
    axs[0].set_xlim([0.39, 0.4])  # Mostrar de 0.38 a 0.4 segundos de la señal moduladora
    axs[0].set_ylim([-1.5, 1.5])  # Ajustar los límites del eje y para ver la parte negativa

    # Graficar la señal portadora
    axs[1].plot(t, carrier_signal)
    axs[1].set_xlabel('t (segundos)')
    axs[1].set_ylabel('Amplitud')
    axs[1].set_title('Señal Portadora')
    axs[1].set_xlim([0.39, 0.4])  # Mostrar de 0.38 a 0.4 segundos de la señal portadora

    # Graficar la señal modulada
    axs[2].plot(t, modulated_signal)
    axs[2].set_xlabel('t (segundos)')
    axs[2].set_ylabel('Amplitud')
    axs[2].set_title('Señal Modulada FM')
    axs[2].set_xlim([0.39, 0.4])  # Mostrar de 0.38 a 0.4 segundos de la señal modulada

    # Ajustar el layout y mostrar la figura
    plt.tight_layout()
    plt.show()

    return modulated_signal

if __name__ == '__main__':
    fm_modulate('AudioPrueba.wav')