from src.gui.GUI import Gui
import sys
from PyQt5.QtWidgets import QApplication
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Gui()
    sys.exit(app.exec_())