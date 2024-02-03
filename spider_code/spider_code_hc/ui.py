# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_GUI(object):
    def setupUi(self, GUI):
        if not GUI.objectName():
            GUI.setObjectName(u"GUI")
        GUI.resize(522, 241)
        self.layoutWidget = QWidget(GUI)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(50, 20, 431, 201))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.PB = QPushButton(self.layoutWidget)
        self.PB.setObjectName(u"PB")

        self.verticalLayout.addWidget(self.PB)

        self.PF = QPushButton(self.layoutWidget)
        self.PF.setObjectName(u"PF")

        self.verticalLayout.addWidget(self.PF)

        self.PR = QPushButton(self.layoutWidget)
        self.PR.setObjectName(u"PR")

        self.verticalLayout.addWidget(self.PR)

        self.PL = QPushButton(self.layoutWidget)
        self.PL.setObjectName(u"PL")

        self.verticalLayout.addWidget(self.PL)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.WS = QPushButton(self.layoutWidget)
        self.WS.setObjectName(u"WS")

        self.verticalLayout_2.addWidget(self.WS)

        self.PU = QPushButton(self.layoutWidget)
        self.PU.setObjectName(u"PU")

        self.verticalLayout_2.addWidget(self.PU)

        self.PD = QPushButton(self.layoutWidget)
        self.PD.setObjectName(u"PD")

        self.verticalLayout_2.addWidget(self.PD)

        self.Pcam = QPushButton(self.layoutWidget)
        self.Pcam.setObjectName(u"Pcam")

        self.verticalLayout_2.addWidget(self.Pcam)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 1, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.SL = QPushButton(self.layoutWidget)
        self.SL.setObjectName(u"SL")

        self.verticalLayout_3.addWidget(self.SL)

        self.WA = QPushButton(self.layoutWidget)
        self.WA.setObjectName(u"WA")

        self.verticalLayout_3.addWidget(self.WA)

        self.FU = QPushButton(self.layoutWidget)
        self.FU.setObjectName(u"FU")

        self.verticalLayout_3.addWidget(self.FU)

        self.BU = QPushButton(self.layoutWidget)
        self.BU.setObjectName(u"BU")

        self.verticalLayout_3.addWidget(self.BU)


        self.gridLayout.addLayout(self.verticalLayout_3, 0, 2, 1, 1)


        self.retranslateUi(GUI)

        QMetaObject.connectSlotsByName(GUI)
    # setupUi

    def retranslateUi(self, GUI):
        GUI.setWindowTitle(QCoreApplication.translate("GUI", u"Spider Control Table", None))
        self.PB.setText(QCoreApplication.translate("GUI", u"StartPosition", None))
        self.PF.setText(QCoreApplication.translate("GUI", u"Forward", None))
        self.PR.setText(QCoreApplication.translate("GUI", u"Turnright", None))
        self.PL.setText(QCoreApplication.translate("GUI", u"Turnleft", None))
        self.WS.setText(QCoreApplication.translate("GUI", u"Walkside", None))
        self.PU.setText(QCoreApplication.translate("GUI", u"Up", None))
        self.PD.setText(QCoreApplication.translate("GUI", u"Down", None))
        self.Pcam.setText(QCoreApplication.translate("GUI", u"ShowStream", None))
        self.SL.setText(QCoreApplication.translate("GUI", u"Sleep", None))
        self.WA.setText(QCoreApplication.translate("GUI", u"Wave", None))
        self.FU.setText(QCoreApplication.translate("GUI", u"FaceUp", None))
        self.BU.setText(QCoreApplication.translate("GUI", u"BottomUp", None))
    # retranslateUi

