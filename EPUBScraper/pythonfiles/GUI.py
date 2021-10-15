import sys
from wuxia import scrape
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QComboBox, QPushButton,QWidget, QLineEdit
from PyQt5.QtCore import QRunnable, Qt, QThreadPool

class Runnable(QRunnable):

    def __init__(self, fchap, lchap, site):

        super().__init__()

        self.fchap = fchap
        self.lchap = lchap
        self.site = site


    def run(self):

        scrape(int(self.fchap),int(self.lchap),self.site)



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

        button = QPushButton('Scrape', self)
        button.setToolTip('Click here when ready to scrape!')
        button.move(110, 150)

        button.clicked.connect(self.runTasks)

        self.site.resize(315,25)
        self.site.move(10, 25)






        self.setFixedWidth(350)
        self.setFixedHeight(250)
        self.setWindowTitle("QLineEdit Example")
        self.show()

    def runTasks(self):
        pool = QThreadPool.globalInstance()
        runnable = Runnable(self.fchap.text(),self.lchap.text(),self.site.text())
        pool.start(runnable)




