import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *


def window():
    app = QApplication(sys.argv)
    win = QWidget()
    
    global l1 
    l1 = QLabel()
    l1.setText("Original")    

    #e1 = QLineEdit()
    #e1.setValidator(QIntValidator())
    #e1.setMaxLength(4)
    #e1.setAlignment(Qt.AlignRight)
    #e1.setFont(QFont("Arial",20))

    #e2 = QLineEdit()
    #e2.setValidator(QDoubleValidator(0.99,99.99,2))

    flo = QFormLayout()
    # flo.addRow("integer validator", e1)
    # flo.addRow("Double validator",e2)

    #e3 = QLineEdit()
    #e3.setInputMask('+99_9999_999999')
    #flo.addRow("Input Mask",e3)

    global e4 
    e4 = QLineEdit()
    e4.textChanged.connect(textchanged)
    newText = e4.text()
    print(newText)
    l1.setText(newText)
    flo.addRow("Text changed",e4)

    #e5 = QLineEdit()
    #e5.setEchoMode(QLineEdit.Password)
    ##flo.addRow("Password",e5)

    #e6 = QLineEdit("Hello Python")
    #e6.setReadOnly(True)
    #flo.addRow("Read Only",e6)

    # e5.editingFinished.connect(enterPress)
    
    # e4.textChanged.connect(textchanged)
    flo.addRow("Changed Text", l1)
    win.setLayout(flo)
    win.setWindowTitle("PyQt")
    win.show()

    sys.exit(app.exec_())

def textchanged(text):
    print("contents of text box: "+text)
    newText = e4.text()
    l1.setText(newText)    
    


def enterPress():
    print("edited")

if __name__ == '__main__':
    window()