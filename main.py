from PyQt5.QtWidgets import QApplication
from viewcontroller import ViewController

app = QApplication.instance()
if not app:
    app = QApplication([])

def viewController():
    _viewController = ViewController()
    return _viewController

def runWithMainWindow(mainWindow):
    mainWindow.show()
    app.exec_()
    mainWindow.close()


def run():
    _viewController = viewController()
    runWithMainWindow(_viewController.mainWindow)

if __name__== "__main__":
    run()
