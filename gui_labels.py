import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QLineEdit  # Ensure all necessary imports
from PyQt5.QtGui import QIcon

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "PyQt Line Edit"
        self.x = 200
        self.y = 200
        self.width = 300
        self.height = 300
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.x, self.y, self.width, self.height)
        self.setWindowIcon(QIcon('pythonico.ico'))

        # Centering the first label
        self.textboxlbl = QLabel("Hello world!", self)
        self.textboxlbl.move(90, 25)

        # Adding QLineEdit
        self.textbox = QLineEdit(self)
        self.textbox.move(30, 50)
        self.textbox.resize(240, 30)
        self.textbox.setText("Set this text value")

        # Adding the new label
        self.infoLabel = QLabel("This program is written in PyCharm", self)
        self.infoLabel.move(50, 90)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
