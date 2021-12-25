from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys
import ConverterRTU_TCP
import Serveur_Modbus_TCP
import threading

class ExampleApp(QtWidgets.QMainWindow, ConverterRTU_TCP.Ui_MainWindow):
    def __init__(self, parent=None):
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)

def main():
    #Server = threading.Thread(target=Serveur_Modbus_TCP.startServer)
    #Window=threading.Thread(target=showWindow)
    #Server.start()
    #Window.start()
    #Server.join()
    #Window.join()
    showWindow()
    #print(form.pushButton.connect(Client_Modbus_TCP.convert(form.plainTextEdit)))

def showWindow():
    app = QApplication(sys.argv)
    form = ExampleApp()
    form.show()
    app.exec_()
    app.pushButton.clicked.connect(clickButton)


if __name__ == '__main__':
    main()