from PySide import QtGui, QtCore
import FreeCAD as App
import Part, PartGui

class OffsetCalc(QtGui.QDialog):
    """"""

    ave_sta_len = 20.71
    
    def __init__(self):
        super(OffsetCalc, self).__init__()
        self.initUI()
    def __str__(self):
        return "OffsetCalc([])"
    def __str__(self):
        return "intUI([])"


    def initUI(self):
        self.result = userCancelled


        # setting font and size
        # create our window
        # define window		xLoc,yLoc,xDim,yDim
        self.setGeometry(850, 550, 350, 250)
        self.setWindowTitle("Ship Offset Calculator")
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        

        
        # creating a label widget
            # by default label will display at top left corner

        # The beginning of the coordinate system is at the left top corner. 
        # The x values grow from left to right. The y values grow from top to bottom.

        self.lSta = QtGui.QLabel("Station", self)
        self.lSta.setFont('Ariel') # set to a non-proportional font
        # self.lSta.textChanged.connect(stachanged)
        self.lSta.move(20, 20)	

        #lSta = QtGui.QLabel("Station", self)
        #lSta.setFont('Ariel') # set to a non-proportional font
        ## lSta.textChanged.connect(stachanged)
        #lSta.move(20, 20)	


        self.lStat = QtGui.QLabel("Station Length", self)
        self.lStat.setFont('Ariel') # set to a non-proportional font
        self.lStat.move(20, 50)		

        self.lStal = QtGui.QLabel(str(self.lStat.text()), self)
        self.lStal.setFont('Ariel') # set to a non-proportional font
        self.lStal.move(120, 50)	

        self.lSta = QtGui.QLabel("H.B/W.L.", self)
        self.lSta.setFont('Ariel') # set to a non-proportional font
        self.lSta.move(20, 80)


        self.lSta = QtGui.QLabel("Feet", self)
        self.lSta.setFont('Ariel') # set to a non-proportional font
        self.lSta.move(20, 110)


        self.lSta = QtGui.QLabel("Inches", self)
        self.lSta.setFont('Ariel') # set to a non-proportional font
        self.lSta.move(20, 140)


        self.lSta = QtGui.QLabel("Eights", self)
        self.lSta.setFont('Ariel') # set to a non-proportional font
        self.lSta.move(20, 170)


        # numeric input field
        self.ista = QtGui.QLineEdit(self)
        #self.ista.setInputMask("99 /9")
        #self.ista.setText("000")
        self.ista.setFixedWidth(50)
        self.ista.move(120, 20)

        #self.istal = QtGui.QLineEdit(self)
        #self.istal.setInputMask("999.9")
        ##self.istal.setText("000")
        #self.istal.setFixedWidth(70)
        #self.istal.move(120, 50)		

        self.iwlht = QtGui.QLineEdit(self)
        self.iwlht.setInputMask("999")
        #self.iwlht.setText("000")
        self.iwlht.setFixedWidth(50)
        self.iwlht.move(120, 80)

        self.ifeet = QtGui.QLineEdit(self)
        self.ifeet.setInputMask("999")
        #self.ifeet.setText("000")
        self.ifeet.setFixedWidth(50)
        self.ifeet.move(120, 110)

        self.iinch = QtGui.QLineEdit(self)
        self.iinch.setInputMask("999")
        #self.iinch.setText("020")
        self.iinch.setFixedWidth(50)
        self.iinch.move(120, 140)

        self.ieight = QtGui.QLineEdit(self)
        self.ieight.setInputMask("999")
        #self.ieight.setText("000")
        self.ieight.setFixedWidth(50)
        self.ieight.move(120, 170)


        bok = QtGui.QPushButton("OK", self)
        bok.clicked.connect(self.onbok)
        bok.move(20, 200)

        self.hbht = QtGui.QRadioButton("Calc H.B", self)
        self.hbht.move(150, 205)

        self.half = QtGui.QRadioButton("Half Station?", self)
        self.half.move(200, 20)		

        #buttonBox = QtGui.QDialogButtonBox()
        #buttonBox = QtGui.QDialogButtonBox(QtCore.Qt.Horizontal)
        #buttonBox.addButton(self.bok, QtGui.QDialogButtonBox.ActionRole)

        self.show()

    def stachanged(text):
        # self.lStal = QtGui.QLabel(str(self.lStat.text()), self)
        print("Text Changed")



    def onbok(self):
        sta = self.ista.text()
        # self.lStal.text = str(float(sta) * self.ave_sta_len)
        #self.label.setText("Searching...")
        #self.label.repaint()
        #self.label.setText("Search Complete")

        #self.lStal.setText(str(float(sta) * self.ave_sta_len))
        #self.lStal.repaint()
        if self.half:
            if sta != 0:
                stal = float(self.ista.text()) * self.ave_sta_len
                # stamm = fttomm(float(self.ista.text())) /2
                stamm = fttomm(stal)
                print("Half Sta. " + str(stamm))
            else:
                stamm = fttomm(float(10.35))
                print("Half Sta. " + stamm)
        else:
            stamm = fttomm(float(self.istal.text()))
            print("Full Sta. " + str(stamm))
        # stamm = fttomm(float(self.istal.text()))
        lSta.setText(stamm)
        wlht = int(self.iwlht.text())
        wlhtmm = fttomm(int(self.iwlht.text()))
        feet = int(self.ifeet.text())
        inches = int(self.iinch.text())
        eights = int(self.ieight.text())
        inches8 = inches*8 # number of 1/8's in Inches column
        dec_ft = (inches8 + eights)/96
        total_ft = feet + dec_ft
        total_ftmm = fttomm(total_ft)
        print(total_ft)
        print(total_ftmm)

        # doc = App.activeDocument() 
        #p = Part.Point
        # create starboard point
        p = App.ActiveDocument.addObject("Part::Vertex", "p1")
        # create port point
        p2 = App.ActiveDocument.addObject("Part::Vertex", "p2")
        p.Y = stamm # Station is always Y

        if self.hbht.isChecked:     #True =hb / False =ht
            # use calced X
            # create starboard point
            print("Using calc X")
            p.X = total_ftmm
            p.Z = wlhtmm
            pname = "Sta-" + sta + "-wl-" + str(wlht) + "s"
            p.Label = pname
            # create port point
            p2.X = total_ftmm * -1
            p2.Y = stamm # Station is always Y
            p2.Z = wlhtmm
            p2name = "Sta-" + sta + "-wl-" + str(wlht) + "p"
            p2.Label = p2name						
        else:
            # use calced Z
            print("Using calced Z")
            p.X =  wlhtmm 
            p.Z = total_ftmm
            pname = "Sta-" + str(sta) + "-ht-" + str(wlht) + "s"
            p.Label = pname
            # create port point
            p2.X = total_ftmm * -1
            p2.Y = stamm # Station is always Y
            p2.Z = wlhtmm
            p2name = "Sta-" + str(sta) + "-wl-" + str(wlht) + "p"
            p2.Label = p2name





        App.ActiveDocument.recompute()

        print("Station = ", sta, "Height = ", wlht, "Feet = ", feet, "Inches = ", inches, "Eights + ", eights)
        print("Eights of Inches = ", inches8, "Dec Ft. = ", dec_ft, "Total = ", total_ft)
        self.result			= userOK
        # self.close()



    #def add_Point(self): # remove because of scope
        #doc=App.activeDocument() 
        #p = Part.Point()
        #p.Y = sta # Station is always Y
        #if self.hbht.isChecked:     #True =hb / False =ht
            ## use calced X
            #print("Using calc X")
            #p.X = total_ft
            #p.Z = wlht
            #p.Label = "Test H.B."
        #else:
            ## use calced Z
            #print("Using calced Z")
            #p.X =  wlht 
            #p.Z = total_ft
            #p.Label = "Test Ht"

        #doc.recompute()

    def add_X_Point(self):
        doc=App.activeDocument() 
        p = Part.Point
        p.Y = Sta
        p.X = hb
        p.Z = total_ft 
        doc.recompute()


    def onCancel(self):
        self.result			= userCancelled
        self.close()
    def onOk(self):
        self.result			= userOK
        self.close()
    def mousePressEvent(self, event):
        # print mouse position, X & Y
        print("X = ", event.pos().x())
        print("Y = ", event.pos().y())
        #

def fttomm(ft):
    mm = ft * 304.8
    return mm



userCancelled = "Cancelled"
userOK = "OK"

form = OffsetCalc()
form.exec_()