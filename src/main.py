import sys
from frontend_module.main_window import MainWindow, QApplication

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
