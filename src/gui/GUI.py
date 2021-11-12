
from src.parsers.wuxia import scrape
from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton,QLineEdit
from PyQt5.QtCore import QObject,QThread, pyqtSignal

class Worker(QObject):
    finished = pyqtSignal()
    def __init__(self, fchap, lchap, site):

        super().__init__()

        self.fchap = fchap
        self.lchap = lchap
        self.site = site


    def run(self):

        scrape(int(self.fchap),int(self.lchap),self.site)
        self.finished.emit()


class Gui(QMainWindow):

    def __init__(self):
        super(Gui,self).__init__()

        fchaplabel= QLabel(self)
        lchaplabel = QLabel(self)
        self.fchap = QLineEdit(self)
        self.lchap = QLineEdit(self)
        self.site = QLineEdit(self)

        self.fchap.move(25,100)
        fchaplabel.setText("First Chapter")
        fchaplabel.move(45,75)


        self.lchap.move(200,100)
        lchaplabel.setText("Last Chapter")
        lchaplabel.move(220,75)

        self.button = QPushButton('Scrape', self)
        self.button.setToolTip('Click here when ready to scrape!')
        self.button.move(110, 150)

        self.button.clicked.connect(self.runTasks)

        self.site.resize(315,25)
        self.site.move(10, 25)






        self.setFixedWidth(350)
        self.setFixedHeight(250)
        self.setWindowTitle("QLineEdit Example")
        self.show()

    def runTasks(self):
        # Step 2: Create a QThread object
        self.thread = QThread()
        # Step 3: Create a worker object
        self.worker = Worker(self.fchap.text(),self.lchap.text(),self.site.text())
        # Step 4: Move worker to the thread
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        # Step 6: Start the thread
        self.thread.start()

        self.button.setEnabled(False)
        self.thread.finished.connect(
            lambda: self.button.setEnabled(True)
        )



