import numpy as np
def mpsk( sample_values:np.ndarray, M: int ):
    # Parámetros
    k = 1  # Número de ciclos por símbolo (ajustable) [1,10]
    T_symbol = 0.01  # Duración de cada símbolo en segundos
    fc = k / T_symbol  # Frecuencia portadora en Hz
    fs = 10000  # Frecuencia de muestreo en Hz
    sample_values = sample_values.astype(int)
    m = int(np.log2(M))
    if( len(sample_values) % m != 0):
       sample_values =  np.append(sample_values, [0 for _ in range(m - (len(sample_values)%m))])

    sample_values = sample_values.reshape(-1, m)

    base_2 = [(1<<i) for i in range(m-1, -1, -1)]

    symbols = np.dot(sample_values, base_2)  # Ejemplo de símbolos transmitidos

    # Crear el tiempo para un solo ciclo de la portadora
    t_symbol = np.linspace(0, T_symbol, int(fs * T_symbol), endpoint=False)

    # Generar la señal modulada en fase
    signal = np.array([])  # Arreglo vacío para construir la señal completa
    for sym in symbols:
        phase = (2 * np.pi * sym) / M  # Calcular el ángulo de fase
        wave = np.sin(2 * np.pi * fc * t_symbol + phase)  # Generar la señal con fase
        signal = np.concatenate((signal, wave))  # Agregar al total

    # Crear eje de tiempo total
    t_total = np.linspace(0, len(symbols) * T_symbol, len(signal), endpoint=False)

    return signal, t_total




if __name__ == '__main__':
    pass

