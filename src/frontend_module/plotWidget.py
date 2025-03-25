from PyQt5.QtWidgets import QVBoxLayout, QWidget, QApplication, QMainWindow
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import numpy as np

class PlotWidget(QWidget):
    def __init__(self):
        super().__init__()

        # 📌 Crear layout para los gráficos
        layout = QVBoxLayout()

        # 📌 Crear figura con tres ejes
        self.figure, self.axes = plt.subplots(3, 1, figsize=(15, 5), dpi=100)
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)

        layout.addWidget(self.toolbar)  # Barra de herramientas
        layout.addWidget(self.canvas)
        self.setLayout(layout)

        # 🔥 Conectar el scroll del mouse para mover los gráficos
        self.canvas.mpl_connect("scroll_event", self.plot_scroll)
        self.canvas.mpl_connect("button_press_event", self.zoom_scroll)

    def set_plots(self, t, baseband_signal, carrier, modulated_signal, modulation_type, units, digitals, sample_times ,sample_vals ):
        # Limpiar solo los ejes sin borrar toda la figura
        for ax in self.axes:
            ax.clear()
        self.figure.subplots_adjust(hspace=0.8)  

        # Redibujar los gráficos en los ejes existentes
        if( digitals[0] == True):
            self.axes[0].step(t, baseband_signal, where='post', linewidth=1.5, color='b')
            self.axes[0].scatter(sample_times, sample_vals, color='red', zorder=3)
            
        else:
            self.axes[0].plot(t, baseband_signal, color='blue')
            
        self.axes[0].set_title("Señal moduladora")
        self.axes[0].set_xlabel(f"Tiempo ({units[0]})")
        self.axes[0].set_ylabel(f"Ampitud ({units[1]})")
        self.axes[0].grid(True)

        if( digitals[1] == True):
            self.axes[1].step(t, carrier, where='post', linewidth=1.5, color='orange')
        else:
            self.axes[1].plot(t, carrier, color='orange')


        self.axes[1].set_title("Señal portadora")
        self.axes[1].set_xlabel(f"Tiempo ({units[0]})")
        self.axes[1].set_ylabel(f"Ampitud ({units[1]})")
        self.axes[1].grid(True)

        if(digitals[2] == True):
            self.axes[2].step(t, modulated_signal, where='post', linewidth=1.5, color='green')
            self.axes[2].scatter(t + 1 / 2, modulated_signal, color='red', zorder=3)
        else:
            self.axes[2].plot(t, modulated_signal, color='green')
        self.axes[2].set_title(f"Señal modulada ({modulation_type})")
        self.axes[2].set_xlabel(f"Tiempo ({units[0]})")
        self.axes[2].set_ylabel(f"Ampitud ({units[1]})")
        self.axes[2].grid(True)

        # Redibujar la figura con los nuevos gráficos
        self.canvas.draw()

    def plot_scroll(self, event):
        """ Mueve el gráfico horizontalmente con la rueda del mouse """
        desplazamiento = (event.step / 10)  # Cuánto se mueve con cada paso del scroll

        for ax in self.axes:
            xlim = ax.get_xlim()
            rango = xlim[1] - xlim[0]  # Tamaño actual de la ventana del gráfico
            nuevo_xlim = [xlim[0] + desplazamiento * rango, xlim[1] + desplazamiento * rango]

            ax.set_xlim(nuevo_xlim)  # Aplicar desplazamiento

        self.canvas.draw()  # Redibujar la figura

    def zoom_scroll(self, event):
        """ Permite hacer zoom usando la rueda del mouse """

        if event.button == 3:
            scale_factor = 1.2
        elif event.button == 1:
            scale_factor = 0.8

        for ax in self.axes:
            xlim = ax.get_xlim()
            x_center = (xlim[0] + xlim[1]) / 2  # Centro del zoom
            x_range = (xlim[1] - xlim[0]) * scale_factor  # Nuevo rango

            ax.set_xlim([x_center - x_range / 2, x_center + x_range / 2])  # Aplicar zoom

        self.canvas.draw()

