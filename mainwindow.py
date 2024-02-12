import os
from PyQt5.QtWidgets import QMainWindow, QHBoxLayout, QWidget
#from PyQt5.QtGui import QICon

class MainWindow(QMainWindow):
    def __init__(self, viewController):
        QMainWindow.__init__(fself)

        self.setWindowTitle('OpenTPS')
        # TODO self.setWindowIcon()
        self.resize(1400, 920)

        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        self.mainLayout = QHBoxLayout()
        centralWidget.setLayout(self.mainLayout)

        self._viewController = viewController



