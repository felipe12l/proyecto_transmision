import sys
import os
import numpy as np
from digital_input_module.digital_input import text_to_signal
from analog_input_module.analog_input import anolog_input_wav
from am_module.am import am_modulate, am_modulate_analog
from ask_module.ask import ask_modulate, ask_modulate_analog
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QComboBox, QPushButton, QLineEdit
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


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
        self.modulation_combo.addItems(["AM", "ASK"])
        control_layout.addWidget(modulation_label)
        control_layout.addWidget(self.modulation_combo)

        # Botón para generar las gráficas
        self.generate_button = QPushButton("Generar Gráficas")
        self.generate_button.clicked.connect(self.generate_plots)
        control_layout.addWidget(self.generate_button)

        # Área de gráficas usando Matplotlib embebido
        self.figure = Figure(figsize=(5, 4))
        self.canvas = FigureCanvas(self.figure)
        main_layout.addWidget(self.canvas)

        # Inicializar visibilidad de los elementos
        self.update_signal_input()

    def update_signal_input(self):
        """Muestra el campo de texto si es señal digital o el botón de audio si es analógica."""
        if self.signal_combo.currentText() == "Digital":
            self.text_input.show()
            self.play_button.hide()
        else:
            self.text_input.hide()
            self.play_button.show()

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
            file = "../AudioPrueba.wav"
            t, baseband_signal = anolog_input_wav(
                file, start_time=0, end_time=2)

        carrier = np.cos(2 * np.pi * carrier_freq * t)
        modulation_type = self.modulation_combo.currentText()

        if self.signal_combo.currentText() == "Digital":
            ## Agregar los casos para las demás modulaciones ##
            if modulation_type == "AM":
                bias = 0.5
                modulation_index = 0.5
                modulated_signal = am_modulate(
                    baseband_signal, t, carrier_freq, bias, modulation_index)
            elif modulation_type == "ASK":
                a1 = 1.0
                modulated_signal = ask_modulate(
                    baseband_signal, t, carrier_freq, a1)
        else:
            ## Agregar los casos para las demás modulaciones ##
            if modulation_type == "AM":
                bias = 0.5
                modulation_index = 0.5
                modulated_signal = am_modulate_analog(
                    baseband_signal, t, carrier_freq, bias, modulation_index)
            elif modulation_type == "ASK":
                a1 = 1.0
                threshold = 0.0
                modulated_signal = ask_modulate_analog(
                    baseband_signal, t, carrier_freq, a1, threshold)

        self.figure.clear()
        ax1 = self.figure.add_subplot(3, 1, 1)
        ax1.plot(t, baseband_signal, color='blue')
        ax1.set_title("Señal moduladora")
        ax1.grid(True)

        ax2 = self.figure.add_subplot(3, 1, 2)
        ax2.plot(t, carrier, color='orange')
        ax2.set_title("Señal portadora")
        ax2.grid(True)

        ax3 = self.figure.add_subplot(3, 1, 3)
        ax3.plot(t, modulated_signal, color='green')
        ax3.set_title(f"Señal modulada ({modulation_type})")
        ax3.set_xlabel("Tiempo (s)")
        ax3.grid(True)

        self.canvas.draw()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
