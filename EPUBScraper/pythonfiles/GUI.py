import sys
from wuxia import scrape
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QComboBox, QPushButton,QWidget, QLineEdit


class Gui(QMainWindow):

    def __init__(self):
        super().__init__()

        fchaplabel= QLabel(self)
        lchaplabel = QLabel(self)
        fchap = QLineEdit(self)
        lchap = QLineEdit(self)
        site = QLineEdit(self)

        fchap.move(25,100)
        fchaplabel.setText("First Chapter")
        fchaplabel.move(45,75)


        lchap.move(200,100)
        lchaplabel.setText("Last Chapter")
        lchaplabel.move(220,75)

        button = QPushButton('Scrape', self)
        button.setToolTip('Click here when ready to scrape!')
        button.move(110, 150)

        button.clicked.connect(lambda: self.on_click(fchap.text(),lchap.text(),site.text()))

        site.resize(315,25)
        site.move(10, 25)






        self.setFixedWidth(350)
        self.setFixedHeight(250)
        self.setWindowTitle("QLineEdit Example")
        self.show()



    def on_click(self,fchap,lchap,novel):
            scrape(int(fchap),int(lchap),novel)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())