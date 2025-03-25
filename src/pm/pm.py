import numpy as np
import matplotlib.pyplot as plt
from analog_input_module  import anolog_input_wav

def pm(modulation_signal,t, fc=5000, kp=np.pi):
    """
    Modulación de fase (PM) de una señal de audio.
    
    Parámetros:
    sound: array_like
        Señal de audio a modular.
    t: array_like
        Eje de tiempo correspondiente a la señal de audio.
    fc: float
        Frecuencia de la portadora en Hz.
    kp: float
        Índice de modulación de fase.
    
    Devuelve:
    modulated_signal: array_like
        Señal modulada en fase.
    """
    
    Ac = 1  # Amplitud de la portadora
    modulated_signal = Ac * np.cos(2 * np.pi * fc * t + kp * modulation_signal)
    
    return modulated_signal

