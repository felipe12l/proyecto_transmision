import numpy as np
import scipy.io.wavfile as waves

def fm_modulate(file: str, A: float = 1.0, fc: int = 1000, delta_f: int = 800, fs: int = 10000):
    # Leer el archivo de audio
    sampling, sound = waves.read(file)
    if sound.ndim > 1:
        sound = sound[:, 0]  # Usar solo el primer canal si es estéreo

    # Normalizar la señal moduladora
    modulating_signal = sound / np.max(np.abs(sound))

    # Calcular el índice de modulación
    beta = delta_f / np.max(np.abs(modulating_signal))

    # Crear el vector de tiempo para la señal portadora
    t = np.linspace(0, len(modulating_signal) / sampling, len(modulating_signal), endpoint=False)

    # Señal portadora
    carrier_signal = A * np.cos(2 * np.pi * fc * t)

    # Señal modulada FM
    modulated_signal = A * np.cos(2 * np.pi * fc * t - 2 * np.pi * beta * np.cumsum(modulating_signal) / sampling)
    
    # Recortar los datos para mostrar únicamente el intervalo de 0.39 a 4 segundos
    mask = (t >= 0.39) & (t <= 0.4)
    t_cropped = t[mask]
    modulating_signal_cropped = modulating_signal[mask]
    carrier_signal_cropped = carrier_signal[mask]
    modulated_signal_cropped = modulated_signal[mask]

    return [t_cropped, modulating_signal_cropped], [t_cropped, carrier_signal_cropped], [t_cropped, modulated_signal_cropped]

if __name__ == '__main__':
    fm_modulate('AudioPrueba.wav')