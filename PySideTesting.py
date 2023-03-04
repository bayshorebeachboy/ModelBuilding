import PySide2
from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtWidgets import QMainWindow, QApplication, QWidget
from PySide2.QtCore import *
import sys

class OffsetCalc(QtWidgets.QDialog):
    """"""
    #app = QApplication(sys.argv)
    
    ## Create a Qt widget, which will be our window.
    #window = QWidget()
    #window.show()     
    
    
    
    def __init__(self):
        # self.setFont(QFont('Helvetica'))
        super(OffsetCalc, self).__init__()
        self.initUI()
    def __str__(self):
        return "OffsetCalc([])"
    def __str__(self):
        return "intUI([])"


    #def initUI(self):
        #self.result = userCancelled


    def initUI(self):
        self.result = userCancelled
        self.setFont('Helvetica')
        # setting font and size
        # create our window
        # define window		xLoc,yLoc,xDim,yDim
        self.setGeometry(850, 550, 350, 250)
        self.setWindowTitle("Ship Offset Calculator")
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        # 
        
        #app = QApplication(sys.argv)
        #win = QWidget()                    
        
        # create label widgets
    
        # The beginning of the coordinate system is at the left top corner. 
        # The x values grow from left to right. The y values grow from top to bottom.
        
        self.lSta = QtWidgets.QLabel("Station #", self)
        self.lSta.setFont('Helvetica') # set to a non-proportional font
        self.lSta.move(20, 20)        
        
        global lStat
        lStat = QtWidgets.QLabel("Station Length", self)
        lStat.setFont('Helvetica') # set to a non-proportional font
        lStat.move(20, 50)	        
        
        global lStatt #calc length based on station number * ave_sta_len
        lStatt = QtWidgets.QLabel("_______", self)
        lStatt.setFont('Helvetica')
        lStatt.move(120, 50)
        
        self.lSta = QtWidgets.QLabel("H.B/W.L.", self)
        self.lSta.setFont('Helvetica') # set to a non-proportional font
        self.lSta.move(20, 80)


        self.lSta = QtWidgets.QLabel("Feet", self)
        self.lSta.setFont('Helvetica') # set to a non-proportional font
        self.lSta.move(20, 110)


        self.lSta = QtWidgets.QLabel("Inches", self)
        self.lSta.setFont('Helvetica') # set to a non-proportional font
        self.lSta.move(20, 140)


        self.lSta = QtWidgets.QLabel("Eights", self)
        self.lSta.setFont('Helvetica') # set to a non-proportional font
        self.lSta.move(20, 170)

        
        
        # create input widgets
        
        global iSta
        iSta = QtWidgets.QLineEdit(self)
        iSta.editingFinished.connect(updatestationlength)
        iSta.setFixedWidth(50)
        iSta.move(120, 20)        

        self.iwlht = QtWidgets.QLineEdit(self)
        self.iwlht.setInputMask("999")
        #self.iwlht.setText("000")
        self.iwlht.setFixedWidth(50)
        self.iwlht.move(120, 80)

        self.ifeet = QtWidgets.QLineEdit(self)
        self.ifeet.setInputMask("999")
        #self.ifeet.setText("000")
        self.ifeet.setFixedWidth(50)
        self.ifeet.move(120, 110)

        self.iinch = QtWidgets.QLineEdit(self)
        self.iinch.setInputMask("999")
        #self.iinch.setText("020")
        self.iinch.setFixedWidth(50)
        self.iinch.move(120, 140)

        self.ieight = QtWidgets.QLineEdit(self)
        self.ieight.setInputMask("999")
        #self.ieight.setText("000")
        self.ieight.setFixedWidth(50)
        self.ieight.move(120, 170)


        bok = QtWidgets.QPushButton("OK", self)
        # bok.clicked.connect(self.onbok)
        bok.move(20, 200)

        self.hbht = QtWidgets.QCheckBox("Calc H.B", self)
        self.hbht.move(200, 50)

        self.half = QtWidgets.QCheckBox("Half Station?", self)
        self.half.move(200, 20)		

        #buttonBox = QtGui.QDialogButtonBox()
        #buttonBox = QtGui.QDialogButtonBox(QtCore.Qt.Horizontal)
        #buttonBox.addButton(self.bok, QtGui.QDialogButtonBox.ActionRole)
        
        
        
        
        self.show()

ave_sta_len = 20.71

def updatestationlength():
    newtext = int(iSta.text()) * ave_sta_len
    newtext = '{:.2f}'.format(newtext)
    print(newtext)
    lStatt.setText(str(newtext))
    lStatt.repaint()

userCancelled = "Cancelled"
userOK = "OK"

app = QApplication(sys.argv)

# Create a Qt widget, which will be our window.
window = QWidget()
window.show()     


form = OffsetCalc()
form.exec_()