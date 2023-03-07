import PySide2
from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtWidgets import QMainWindow, QApplication, QWidget
from PySide2.QtCore import *
import FreeCAD as App
import sys

# ave_sta_len = 20.71
####################################
# define class OffsetCalc
###################################
class OffsetCalc(QtWidgets.QDialog):
    """"""
    # app = QApplication(sys.argv)
    
    ## Create a Qt widget, which will be our window.
    #window = QWidget()
    #window.show()     
    
    # constants
    font = "Helvetica" 
    ave_sta_len = 20.71    
    
    def __init__(self):
        # self.setFont(QFont('Helvetica'))
        super(OffsetCalc, self).__init__()
        self.initUI()
    def __str__(self):
        return "OffsetCalc([])"
    def __str__(self):
        return "intUI([])"



    def initUI(self):
        # self.result = userCancelled
        self.setFont('Helvetica')
        # setting font and size
        # create our window
        # define window		xLoc,yLoc,xDim,yDim
        self.setGeometry(850, 550, 350, 250)
        self.setWindowTitle("Ship Offset Calculator")
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        # 
        
        
        ## constants
        font = "Helvetica" 
        #ave_sta_len = 20.71
        
        # create label widgets
    
        # The beginning of the coordinate system is at the left top corner. 
        # The x values grow from left to right. The y values grow from top to bottom.
        
        self.lSta = QtWidgets.QLabel("Station #", self)
        self.lSta.setFont('Helvetica') 
        self.lSta.move(20, 20)        
        
        self.lStat = QtWidgets.QLabel("Station Length", self)
        self.lStat.setFont(font)
        self.lStat.move(20, 50)
        
        # global lStatt #calc length based on station number * ave_sta_len
        self.lStatt = QtWidgets.QLabel("---------", self)
        self.lStatt.setFont(font)
        self.lStatt.move(120, 50)
        
        self.lSta = QtWidgets.QLabel("W.L./Butt.", self)
        self.lSta.setFont(font) # constants
        self.lSta.move(20, 80)


        self.lSta = QtWidgets.QLabel("Feet", self)
        self.lSta.setFont(font) 
        self.lSta.move(20, 110)


        self.lSta = QtWidgets.QLabel("Inches", self)
        self.lSta.setFont(font) # set to a non-proportional font
        self.lSta.move(20, 140)


        self.lSta = QtWidgets.QLabel("Eights", self)
        self.lSta.setFont(font) # set to a non-proportional font
        self.lSta.move(20, 170)

        
        
        # create input widgets
       
        self.iSta = QtWidgets.QLineEdit(self)
        self.iSta.editingFinished.connect(lambda: self.updatestationlength(self.iSta.text(),self.half.isChecked()))
        # lambda: calluser(name)
        self.iSta.setFixedWidth(50)
        self.iSta.move(120, 20)        
        
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
        #self.iinch.setText("020")ave_sta_len = 20.71
        self.iinch.setFixedWidth(50)
        self.iinch.move(120, 140)

        self.ieight = QtWidgets.QLineEdit(self)
        self.ieight.setInputMask("999")
        #self.ieight.setText("000")
        self.ieight.setFixedWidth(50)
        self.ieight.move(120, 170)


        bok = QtWidgets.QPushButton("OK", self)
        bok.clicked.connect(self.onbok)
        bok.move(20, 200)

        self.hbht = QtWidgets.QCheckBox("Calc H.B", self)
        self.hbht.move(200, 50) 
               
        self.half = QtWidgets.QCheckBox("Half Station?", self)
        self.half.move(200, 20)
        self.show()
        
       
        userCancelled = "Cancelled" # needed?
        userOK = "OK" #needed? 
             
        
        
        # define class methods 
                
    def onbok(self):
        # print(self.iSta.text())
        sta_len = int(self.iSta.text())
        half = self.half.isChecked()
        # print(sta_len, half)
        self.calc_Y(sta_len, half)
        # self.add_point()
        # reset input form
        self.iwlht.setText("")
        self.iwlht.setFocus()
        self.iwlht.backspace()
        self.iwlht.backspace()
        self.iwlht.backspace()
        self.iwlht.repaint()
        self.iwlht.setFocus()
        self.ifeet.setText("")
        self.ifeet.repaint()
        self.iinch.setText("")
        self.iinch.repaint()
        self.ieight.setText("")
        self.ieight.repaint()
        
            
           
    def calc_Y(self, sta_len, half):
        ###################sta = self.iSta.text()
        # calc_Y - Sta Len (point.Z) in mm and create label suffix based on is half
        ###################
        sta = sta_len
        halfsuffix = ""
        if half:  # True - create half staton
            if sta != 0:
                halfsuffix = "-1/2"
                stal = (float(sta)  + 0.5) * self.ave_sta_len 
                stamm = self.fttomm(stal) # point(Y)
                print(stamm)
                self.add_point(stamm, halfsuffix)
                print("Half Sta. " + str(stamm))
            else:
                halfsuffix = "-1/2"
                print("Sta is zero")
                stal =  0.5 * self.ave_sta_len
                stamm = self.fttomm(stal)
                print(stamm)
                self.add_point(stamm, halfsuffix)
                print("Half Sta. " + str(stamm))       
                
        else:
            stal = float(sta) * self.ave_sta_len
            stamm = self.fttomm(float(stal)) # point(Y)
            # halfsuffix = "-1/2"
            self.add_point(stamm, halfsuffix)
            return(stamm) 

        
    def add_point(self, stamm, halfsuffix):
        wlht = int(self.iwlht.text()) 
        wlhtmm = self.fttomm(int(self.iwlht.text()))
        feet = int(self.ifeet.text())
        inches = int(self.iinch.text())
        eights = int(self.ieight.text())
        inches8 = inches*8 # number of 1/8's in ave_sta_len = 20.71Inches column
        dec_ft = (inches8 + eights)/96
        total_ft = feet + dec_ft
        total_ftmm = self.fttomm(total_ft)
        print(total_ft) 
        print(total_ftmm)
    
        # create empty starboard point
        p = App.ActiveDocument.addObject("Part::Vertex", "p1")
        # create empty port pointsta = self.iSta.text()
        p2 = App.ActiveDocument.addObject("Part::Vertex", "p2")
        p.Y = stamm # Station is always Y
    
        if self.hbht.isChecked():     #True =hb / False =ht
            # use calced X
            # attribute starboard point
            print("Using calc X")
            print(total_ftmm, stamm, wlhtmm)
            p.X = total_ftmm
            p.Y = stamm # Station is always Y * 1.5
            p.Z = wlhtmm
            sta = self.iSta.text()
            pname = "Sta-" + sta + halfsuffix + "-wl-" + str(wlht) + "s"
            print(pname)
            p.Label = pname
            # attribute port point# constants      
            p2.X = total_ftmm * -1
            p2.Y = stamm # Station is always Y
            p2.Z = wlhtmm
            # newtext = int(sta_len) * self.ave_sta_len
            p2name = "Sta-" + str(sta) + halfsuffix + "-wl-" + str(wlht) + "p"
            print(p2name)
            p2.Label = p2name
            print("Station = ", sta, "Height = ", wlht, "Feet = ", feet, "Inches = ", inches, "Eights = ", eights)
            print("Eights of Inches = ", inches8, "Dec Ft. = ", dec_ft, "Total = ", total_ft)            
        else: 
            # use calced Z
            print("Using calced Z")
            # attribute starboard point
            sta = self.iSta.text()
            pname = "Sta-" + str(sta) + halfsuffix + "-ht-" + str(wlht) + "s"
            p.X =  wlhtmm 
            p.Z = total_ftmm
            p.Label = pname
            # attribute port point
            p2.X = total_ftmm * -1
            p2.Y = stamm # Station is always Y
            p2.Z = wlhtmm
            p2name = "Sta-" + str(sta) + halfsuffix + "-ht-" + str(wlht) + "p"
            print(pname)
            print(p2name) 
            p2.Label = p2name
            App.ActiveDocument.recompute()
            # debug stuff
            print("Station = ", sta, "Height = ", wlht, "Feet = ", feet, "Inches = ", inches, "Eights = ", eights)
            print("Eights of Inches = ", inches8, "Dec Ft. = ", dec_ft, "Total = ", total_ft)
            # self.result= userOK
                
                
            
        
    def fttomm(self, ft):
        mm = ft * 304.8
        return mm
    
    def updatestationlength(self, sta_len, half):
        if half:
            newtext = (int(sta_len) + 0.5) * self.ave_sta_len
        else:
            newtext = int(sta_len) * self.ave_sta_len
        newtext = '{:.2f}'.format(newtext)
        print(newtext)
        iStal = int(sta_len) * self.ave_sta_len
        self.lStatt.setText(str(newtext))
        self.lStatt.repaint()
        
            
        #def addpoints():
            #print("#######")
        
        #def onbok():
            #print("#######")



#################################################
# end class definition
#################################################
                

#userCancelled = "Cancelled"
#userOK = "OK"

# app = QApplication(sys.argv)

# Create a Qt widget, which will be our window.
#window = QWidget()
#window.show()     


form = OffsetCalc()
form.exec_()
