from GUI.GUI import *
import sys
from photomosaic_A import takeScreenshot, makemosaic

class GUIApp(Ui_Dialog):

    def clickTest():
        print('test')


    def __init__(self, window):
        self.setupUi(window)
        self.photomosaic.clicked.connect(self.clickTest)

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

ui = GUIApp(MainWindow)

MainWindow.show()
app.exec_()


