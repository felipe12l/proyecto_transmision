import numpy as np
import matplotlib.pyplot as plt
from digital_input_module.digital_input import text_to_signal  # Asegúrate de tener __init__.py en cada carpeta

def fsk_modulate(text: str, f1: int = 200, f2: int = 500, A: float = 1.0, fs: int = 8000, T_symbol: float = 0.01):
    # Convertir el texto a señal binaria y extraer sample_values
    _, _, _, sample_values = text_to_signal(text)
    
    k = 1  # Número de ciclos por símbolo (ajustable)
    fc1 = k / T_symbol
    fc2 = k / T_symbol

    t_symbol = np.linspace(0, T_symbol, int(fs * T_symbol), endpoint=False)
    signal = np.array([])  # Señal modulada
    carrier_signal = np.array([])  # Señal portadora

    for bit in sample_values:
        if bit == 0:
            wave = A * np.cos(2 * np.pi * f1 * t_symbol)
            carrier_wave = A * np.cos(2 * np.pi * fc1 * t_symbol)
        else:
            wave = A * np.cos(2 * np.pi * f2 * t_symbol)
            carrier_wave = A * np.cos(2 * np.pi * fc2 * t_symbol)
        signal = np.concatenate((signal, wave))
        carrier_signal = np.concatenate((carrier_signal, carrier_wave))
    
    t_total = np.linspace(0, len(sample_values) * T_symbol, len(signal), endpoint=False)

    # Creación de figura de depuración sin mostrarla
    fig, axs = plt.subplots(3, 1, figsize=(10, 6))
    axs[0].step(np.arange(len(sample_values)) * T_symbol, sample_values, where='post')
    axs[0].set_title('Señal Moduladora')
    axs[0].set_xlabel('t (segundos)')
    axs[0].set_ylabel('Amplitud')
    axs[0].set_xlim([0, 0.2])
    axs[0].set_ylim([-1.5, 1.5])
    
    axs[1].plot(t_total, carrier_signal)
    axs[1].set_title('Señal Portadora')
    axs[1].set_xlabel('t (segundos)')
    axs[1].set_ylabel('Amplitud')
    axs[1].set_xlim([0, 0.2])
    
    axs[2].plot(t_total, signal)
    axs[2].set_title('Señal FSK Modulada')
    axs[2].set_xlabel('t (segundos)')
    axs[2].set_ylabel('Amplitud')
    axs[2].set_xlim([0, 0.2])
    
    plt.tight_layout()
    # Se eliminó plt.show() para evitar ventana separada

    return signal, t_total