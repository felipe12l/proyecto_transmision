<<<<<<< HEAD
import sys
from frontend_module.main_window import MainWindow, QApplication

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
=======
from mpsk_module.mpsk import mpsk
from digital_input_module.digital_input import text_to_signal
from analog_input_module.analog_input import anolog_input_wav
from pcm_module.pcm import pcm, plot_polar_square_wave
import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile
from psk import psk
from mpsk_module import mpsk
if __name__ == '__main__':
    

    # times, values = anolog_input_wav('./AudioPrueba.wav', start_time=40, end_time=41)
    # plt.plot(times, values)
    # plt.xlabel('Tiempo (s)')
    # plt.ylabel('Amplitud')
    # plt.title('Segmento de audio')
    # plt.show()
    
        # Leer el archivo de audio .wav
  

    # print(times, values)
    # print(len(times), len(values))
    
    # pcm_v = pcm(values, 16)
    # # print(pcm_v)
    # # print(len(pcm_v))
    
    # # pcm_v = [1,-1,-1,1,1]
    # plot_polar_square_wave(pcm_v)
    
    
    t, signal, sample_times, sample_values = text_to_signal("hola")
    M = 2
    signal, t_total = mpsk.mpsk(sample_values, M )

    plt.figure(figsize=(10, 4))
    plt.plot(t_total, signal, label="Señal modulada (MPSK)")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Amplitud")
    plt.title(f"Señal {M}-PSK modulada en fase")
    plt.legend()
    plt.grid()
    plt.show()
    
>>>>>>> fm-psk
