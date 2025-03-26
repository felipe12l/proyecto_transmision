import numpy as np
import matplotlib.pyplot as plt
from analog_input_module  import anolog_input_wav

# def pm(modulation_signal,t, fc=5000, kp=np.pi):
#     """
#     Modulación de fase (PM) de una señal de audio.
    
#     Parámetros:
#     sound: array_like
#         Señal de audio a modular.
#     t: array_like
#         Eje de tiempo correspondiente a la señal de audio.
#     fc: float
#         Frecuencia de la portadora en Hz.
#     kp: float
#         Índice de modulación de fase.
    
#     Devuelve:
#     modulated_signal: array_like
#         Señal modulada en fase.
#     """
    
#     Ac = 1  # Amplitud de la portadora
#     modulated_signal = Ac * np.cos(2 * np.pi * fc * t + kp * modulation_signal)
    
#     return modulated_signal, t
#     # Si la señal moduladora es una función de numpy, simplemente evalúa la función
#     # en el eje de tiempo `t` antes de realizar la modulación.

def pm_with_function(modulation_function, t, fc=5000, kp=np.pi):
    """
    Modulación de fase (PM) de una señal de audio cuando la señal moduladora es una función de numpy.
        
    Parámetros:
    modulation_function: callable
        Función de numpy que representa la señal moduladora.
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
        
    modulation_signal = modulation_function(t)  # Evalúa la función en el eje de tiempo
    Ac = 1  # Amplitud de la portadora
    modulated_signal = Ac * np.cos(2 * np.pi * fc * t + kp * modulation_signal)
        
    return modulated_signal, t
