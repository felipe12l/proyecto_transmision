import matplotlib.pyplot as plt
from analog_input_module.analog_input import anolog_input_wav
from fm_module.fm import fm_modulate
from digital_input_module.digital_input import text_to_signal
from fsk_module.fsk import fsk_modulate

def main():
    # Integración FM con señal analógica:
    print("Ejecutando modulación FM con integración de señal analógica...")
    audio_file = 'AudioPrueba.wav'
    # Extraer la señal analógica (se puede ajustar start_time/end_time según se requiera)
    t_analog, analog_signal = anolog_input_wav(audio_file, start_time=0, end_time=1)
    # La función fm_modulate ya lee el archivo internamente y modula
    modulated_signal_fm = fm_modulate(audio_file)
    
    # Mostrar la señal analógica extraída
    plt.figure(figsize=(8, 4))
    plt.plot(t_analog, analog_signal)
    plt.xlabel("Tiempo (s)")
    plt.title("Señal analógica extraída")
    plt.show()

    # Integración FSK con señal digital:
    print("Ejecutando modulación FSK con integración de señal digital...")
    text = "Hello"
    # Extraer la señal digital a partir del texto
    t_digital, digital_signal, sample_times, sample_values = text_to_signal(text)
    # La función fsk_modulate usa el texto para la modulación FSK
    modulated_signal_fsk, t_total = fsk_modulate(text)
    
    # Mostrar la señal digital extraída
    plt.figure(figsize=(8, 4))
    plt.plot(t_digital, digital_signal)
    plt.xlabel("Tiempo (s)")
    plt.title("Señal digital extraída")
    plt.show()

if __name__ == '__main__':
    main()