import sys
from PySide6 import QtWidgets, QtCore, QtGui
from ui import Ui_GUI
from script import Spider

class GUI(QtWidgets.QWidget, Ui_GUI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.PF.clicked.connect(self.walkForward)
        self.PB.clicked.connect(self.StartPosition)
        self.PL.clicked.connect(self.TurnLeft)
        self.PR.clicked.connect(self.Turnright)
        self.PU.clicked.connect(self.GetUp)
        self.PD.clicked.connect(self.GetDown)
        self.Pcam.clicked.connect(self.ShowVedio)
        self.WS.clicked.connect(self.Walkside)
        self.FU.clicked.connect(self.FaceUp)
        self.BU.clicked.connect(self.Bottomup)
        self.WA.clicked.connect(self.Wave)
        self.SL.clicked.connect(self.Sleep)
    @QtCore.Slot()
    def walkForward(self):
        spider.walk_please()
        print("forward")

    @QtCore.Slot()
    def StartPosition(self):
        spider.start_position()
        print("Stand")

    @QtCore.Slot()
    def TurnLeft(self):
        spider.tripod_turn(direction='left',steps=1)
        print("Left")

    @QtCore.Slot()
    def Turnright(self):
        spider.tripod_turn(direction='right',steps=1)
        print("Right")

    @QtCore.Slot()
    def GetUp(self):
        spider.move_up()
        print("Up")

    @QtCore.Slot()
    def GetDown(self):
        spider.move_down()
        print("Down")

    @QtCore.Slot()
    def ShowVedio(self):
        print('video')
        import stream


    @QtCore.Slot()
    def Walkside(self):
        spider.walk_sideway()
        print('walkside')

    @QtCore.Slot()
    def FaceUp(self):
        spider.face_up()
        print('Faceup')

    @QtCore.Slot()
    def Bottomup(self):
        spider.bottom_up()
        print('Bottomup')

    def Wave(self):
        spider.wave(5)
        print('wave')

    def Sleep(self):
        spider.sleep_modus()
        print('sleep')

    

if __name__ == "__main__":
    spider= Spider()
    app = QtWidgets.QApplication(sys.argv)
    w1= GUI()
    w1.show()
    sys.exit(app.exec_())

