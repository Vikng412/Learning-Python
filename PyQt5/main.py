import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon, QPixmap
from pathlib import Path

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    icon_path = Path(__file__).parent / "pic.jpg"  
    icon = QIcon(str(icon_path))  
    win.setGeometry(500,170,500,500)
    win.setWindowTitle("Kanishk's First GUI")
    win.setWindowIcon(icon)
    win.setToolTip("Mouse is Hovering")
    win.show()
    sys.exit(app.exec_())

window()