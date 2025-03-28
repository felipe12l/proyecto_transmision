import numpy as np

def pmModulation(portadora, mensaje, kp):
    """
    Realiza la modulación en fase (PM) usando una portadora y un mensaje dados.

    Parámetros:
    - portadora: Señal portadora (numpy array)
    - mensaje: Señal moduladora (mensaje) (numpy array)
    - kp: Índice de modulación de fase

    Retorna:
    - modulada_pm: Señal modulada en fase
    """
    # Extraer la amplitud de la portadora
    Ap = np.max(np.abs(portadora))  # Asume que la portadora tiene amplitud constante

    # Generar la señal modulada en fase
    modulada_pm = Ap * np.sin(np.angle(portadora) + kp * mensaje)

    return modulada_pm
