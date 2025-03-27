import sys
import os
import numpy as np

#OWN MODULES
from digital_input_module.digital_input import text_to_signal
from analog_input_module.analog_input import anolog_input_wav

from fm_module.fm import fm_modulate              
from am_module.am import am_modulate, am_modulate_analog
from ask_module.ask import ask_modulate, ask_modulate_analog

from fsk_module.fsk import fsk_modulate
from pcm_module.pcm import pcm
from mpsk_module.mpsk import mpsk

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QComboBox, QPushButton, QLineEdit
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from . import plotWidget



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Interfaz de Modulación")
        self.setGeometry(100, 100, 800, 600)

        # Widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # Panel de controles
        control_layout = QHBoxLayout()
        main_layout.addLayout(control_layout)

        # Selector de fuente de señal
        signal_label = QLabel("Tipo de Señal:")
        self.signal_combo = QComboBox()
        self.signal_combo.addItems(["Digital", "Analógica"])
        self.signal_combo.currentIndexChanged.connect(self.update_signal_input)
        control_layout.addWidget(signal_label)
        control_layout.addWidget(self.signal_combo)

        # Campo de texto para la señal digital
        self.text_input = QLineEdit()
        self.text_input.setPlaceholderText(
            "Ingresa el texto para la señal digital")
        control_layout.addWidget(self.text_input)

        # Reproductor de audio para señal analógica
        self.audio_player = QMediaPlayer()
        self.play_button = QPushButton("Reproducir Audio")
        self.play_button.clicked.connect(self.play_audio)
        control_layout.addWidget(self.play_button)

        # Selector de modulación
        modulation_label = QLabel("Modulación:")
        self.modulation_combo = QComboBox()

        # Añadir más opciones de modulación
        # self.modulation_combo.addItems(["AM", "ASK"])
        control_layout.addWidget(modulation_label)
        control_layout.addWidget(self.modulation_combo)

        # Botón para generar las gráficas
        self.generate_button = QPushButton("Generar Gráficas")
        self.generate_button.clicked.connect(self.generate_plots)
        control_layout.addWidget(self.generate_button)

        # Área de gráficas usando Matplotlib embebido
        # self.figure = Figure(figsize=(5, 4))
        # self.canvas = FigureCanvas(self.figure)
        self.canvas = plotWidget.PlotWidget()
        main_layout.addWidget(self.canvas)

        # Inicializar visibilidad de los elementos
        self.update_signal_input()

    def update_signal_input(self):
        """Muestra el campo de texto si es señal digital o el botón de audio si es analógica."""
        self.modulation_combo.clear()
        if self.signal_combo.currentText() == "Digital":
            self.text_input.show()
            self.play_button.hide()

            self.modulation_combo.addItems(['ASK','FSK','PSk','4-PSK','8-PSK','16-PSK'])


        else:
            self.text_input.hide()
            self.play_button.show()

            self.modulation_combo.addItems(['AM','FM','PM','PCM'])

    def play_audio(self):
        """Reproduce el audio predeterminado."""
        audio_path = "./AudioPrueba.wav"  # Asegúrate de que el archivo existe en esta ruta
        if not os.path.exists(audio_path):
            print(f"Error: El archivo '{audio_path}' no existe.")
        self.audio_player.setMedia(
            QMediaContent(QUrl.fromLocalFile(audio_path)))
        self.audio_player.play()


    def generate_plots(self):
        fs = 1000  # Frecuencia de muestreo
        carrier_freq = 100  # Frecuencia de la portadora en Hz

        # Según la fuente seleccionada: digital o analógica
        if self.signal_combo.currentText() == "Digital":
            text = self.text_input.text() if self.text_input.text() else "Hello World"
            t, baseband_signal, sample_times, sample_vals = text_to_signal(
                text)
        else:
            file = "./AudioPrueba.wav"
            t, baseband_signal = anolog_input_wav(
                file, start_time=1, end_time=1.01)
            sample_times = []
            sample_vals = []

        carrier = np.cos(2 * np.pi * carrier_freq * t)
        modulation_type = self.modulation_combo.currentText()

        base_signal = [ t, baseband_signal ]
        carrier_signal = [t, carrier]
        units = [['s', 'V'] for _ in range(3)]
        digital_signals = [False, False, False]

        
        '''
            TO - DO:
            Add for each method:
            modulated signal [t, values]
            carriet signal [t, values] if neccesary
            units [ [time units, amplitude units] for each signal ]
            digital_signals = [ if base signal , if carrier , if modulated]

        '''


        if self.signal_combo.currentText() == "Digital":
            
            ## Agregar los casos para las demás modulaciones ##
            modulated_signal = [t,t] #REMOVE THIS AFTER PUT ALL THE MODULATION SIGNALS

            if modulation_type == "ASK":
                a1 = 1.0
                modulated_sign = ask_modulate(
                    baseband_signal, t, carrier_freq, a1)
                modulated_signal = [t, modulated_sign]
                units = [['s', 'V'] for _ in range(3)]
                digital_signals = [True, False, False]
            elif modulation_type == "FSK":
                signal, t_total = fsk_modulate(text)
                modulated_signal = [t_total, signal]
                digital_signals = [True, False, False]
            elif modulation_type.__contains__('-PSK'):
                m = int(modulation_type.split('-')[0])
                vals, t_signal, carr_sign = mpsk(sample_vals, m)
                modulated_signal = [t_signal,vals]
                carrier_signal = [t_signal, carr_sign]
                digital_signals = [True, False, False]
                units = [['s', 'V'] for _ in range(3)]
            
        else:
            ## Agregar los casos para las demás modulaciones ##
            modulated_signal = [t,t] #REMOVE THIS AFTER PUT ALL THE MODULATION SIGNALS
            if modulation_type == "AM":
                bias = 0.5
                modulation_index = 0.5
                carrier_freq = 6000 
                carrier = np.cos(2 * np.pi * carrier_freq * t)
                modulated_sign = am_modulate_analog(
                    baseband_signal, t, carrier_freq, bias, modulation_index)
                modulated_signal = [t, modulated_sign]
                units = [['s', 'mV'] for _ in range(3)]


                carrier_signal = [t, carrier]

            elif modulation_type == 'FM':
                base_signal, carrier_signal, modulated_signal = fm_modulate("./AudioPrueba.wav")
            elif modulation_type == 'PM':
                pass
            elif modulation_type == 'PCM':
                m_levels = 8
                t, vals = pcm(baseband_signal, m_levels)
                modulated_signal = [t, vals] 
                carrier_signal = [[], []]
                digital_signals = [False, False, True]
                units = [['s', 'mV'],['s', 'V'],['ms', 'V']]


        #units = [ axis x units, axis y units] 
        #digitals meaning which signals are digitals = [ baseband, carrier, modulate] True if digital else False
        # signals now are an array with [t, values] -> t meaning times and values the values of the signal
        #DO NOT MODIFY THIS LINE!
        self.canvas.set_plots(base_signal, carrier_signal, modulated_signal, modulation_type, units, digital_signals, sample_times, sample_vals)
