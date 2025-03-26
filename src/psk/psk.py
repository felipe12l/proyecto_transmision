import numpy as np
def psk(array_values,fc,vc):
    """_summary_

    Args:
        array_values (_type_): arreglo de valores digitales de la señal digital en 1 y 0
        fc (_type_): frecuencia de la portadoraen Hz
        vc (_type_): voltaje de la portadora
    """
    fs = 10000 
    T_symbol = 0.01  # Duración de cada símbolo en segundos
    t_symbol = np.linspace(0, T_symbol, int(fs * T_symbol), endpoint=False)
    signal = np.array([])
    base_2 = [(1<<i) for i in range(2-1, -1, -1)]

    symbols = np.dot(array_values, base_2) 
    for i in array_values:
        if i == 1:
            wave = vc*np.sin(2 * np.pi * fc * t_symbol)
        else:
            wave = -vc*np.sin(2 * np.pi * fc * t_symbol)
        signal = np.concatenate((signal, wave))
    t_total = np.linspace(0, len(symbols) * T_symbol, len(signal), endpoint=False)
    return signal, t_total