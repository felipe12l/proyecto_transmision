import numpy as np
import matplotlib.pyplot as plt

def fsk_modulate(text: str, f1: int = 200, f2: int = 500, A: float = 1.0, fs: int = 8000, T_symbol: float = 0.01):
    # Convertir el texto a una señal binaria
    sample_values = text_to_binary(text)
    
    # Parámetros
    k = 1  # Número de ciclos por símbolo (ajustable) [1,10]
    fc1 = k / T_symbol  # Frecuencia portadora para el bit 0
    fc2 = k / T_symbol  # Frecuencia portadora para el bit 1

    # Crear el tiempo para un solo ciclo de la portadora
    t_symbol = np.linspace(0, T_symbol, int(fs * T_symbol), endpoint=False)

    # Generar la señal modulada en frecuencia
    signal = np.array([])  # Arreglo vacío para construir la señal completa
    carrier_signal = np.array([])  # Arreglo vacío para la señal portadora
    for bit in sample_values:
        if bit == 0:
            wave = A * np.cos(2 * np.pi * f1 * t_symbol)  # Generar la señal con frecuencia f1
            carrier_wave = A * np.cos(2 * np.pi * fc1 * t_symbol)  # Señal portadora para bit 0
        else:
            wave = A * np.cos(2 * np.pi * f2 * t_symbol)  # Generar la señal con frecuencia f2
            carrier_wave = A * np.cos(2 * np.pi * fc2 * t_symbol)  # Señal portadora para bit 1
        signal = np.concatenate((signal, wave))  # Agregar al total
        carrier_signal = np.concatenate((carrier_signal, carrier_wave))  # Agregar al total

    # Crear eje de tiempo total
    t_total = np.linspace(0, len(sample_values) * T_symbol, len(signal), endpoint=False)

    
    # Crear una figura con subplots
    fig, axs = plt.subplots(3, 1, figsize=(10, 6))  # Ajustar la altura de la ventana

    # Graficar la señal moduladora
    axs[0].step(np.arange(len(sample_values)) * T_symbol, sample_values, where='post')
    axs[0].set_xlabel('t (segundos)')
    axs[0].set_ylabel('Amplitud')
    axs[0].set_title('Señal Moduladora')
    axs[0].set_xlim([0, 0.2])  # Mostrar de 0 a 1 segundos de la señal moduladora
    axs[0].set_ylim([-1.5, 1.5])  # Ajustar los límites del eje y para ver la parte negativa

    # Graficar la señal portadora
    axs[1].plot(t_total, carrier_signal)
    axs[1].set_xlabel('t (segundos)')
    axs[1].set_ylabel('Amplitud')
    axs[1].set_title('Señal Portadora')
    axs[1].set_xlim([0, 0.2]) # Mostrar de 0 a 1 segundos de la señal portadora

    # Graficar la señal modulada
    axs[2].plot(t_total, signal)
    axs[2].set_xlabel('t (segundos)')
    axs[2].set_ylabel('Amplitud')
    axs[2].set_title('Señal FSK Modulada')
    axs[2].set_xlim([0, 0.2])  # Mostrar de 0 a 1 segundos de la señal modulada

    # Ajustar el layout y mostrar la figura
    plt.tight_layout()
    plt.show()

    return signal, t_total

if __name__ == '__main__':
    # Ejemplo de uso con una cadena de texto
    text = "Hello"
    fsk_modulate(text)