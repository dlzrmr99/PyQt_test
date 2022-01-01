import sys
from PyQt5.QtWidgets import QApplication, QWidget


if __name__ == '__main__':

    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(500, 650)
    w.move(600, 600)
    w.setWindowTitle('Simple')
    w.show()

    sys.exit(app.exec_())