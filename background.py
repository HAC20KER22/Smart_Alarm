# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'output.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QSizePolicy, QStatusBar, QWidget)

import sys
from PySide6 import QtWidgets
import datetime
import playsound


class Ui_MainWindow(object):
    def show_output(self,l):
        if(l==None):
            sys.exit()
        descriptionToShow = l[3]
        titleToShow = l[0]
        self.desc.setText(descriptionToShow)
        self.title.setText(titleToShow)
        return;





    def setupUi(self, MainWindow):
        l= self.check()
        if(l==''):
            sys.exit()
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(716, 555)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.notif = QLabel(self.centralwidget)
        self.notif.setObjectName(u"notif")
        self.notif.setGeometry(QRect(20, 30, 391, 71))
        font = QFont()
        font.setFamilies([u"MV Boli"])
        font.setPointSize(24)
        self.notif.setFont(font)
        self.notif.setAlignment(Qt.AlignCenter)
        self.title = QLabel(self.centralwidget)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(90, 140, 461, 61))
        font1 = QFont()
        font1.setPointSize(20)
        self.title.setFont(font1)
        self.title.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.desc = QLabel(self.centralwidget)
        self.desc.setObjectName(u"desc")
        self.desc.setGeometry(QRect(100, 240, 471, 151))
        font2 = QFont()
        font2.setPointSize(16)
        self.desc.setFont(font2)
        self.desc.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 716, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
        self.show_output(l)
        self.remove(l)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.notif.setText(QCoreApplication.translate("MainWindow", u"Alarm Goes off!!!", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"Title", None))
        self.desc.setText(QCoreApplication.translate("MainWindow", u"Description", None))
    # retranslateUi
    def check(self):
        f = open("E:\\Python Project\\Smart Alarm\\donottouch.txt",'r')
        alarms = f.readlines()
        today = datetime.date.today()
        today = today.strftime("%Y-%m-%d")
        
        l=[]
        flag=False
        for i in range(len(alarms)):
            alarms[i] = alarms[i][0:len(alarms[i])-1:1]
        enter_back=alarms
        for i in alarms:
            l=i.split(',')
            if(l[1]>today):
                return l
                flag=True
                break;
            elif(l[1]==today):
                t=l[1].split
                currenttime = datetime.datetime.now()
                if(t[1]=='AM' and currenttime.hour>=12):
                    return l
                    flag=True
                    break;
                elif (currenttime.hour>=12):
                    if(currenttime.hour-12>t[0]):
                        return l
                        flag = True
                        break;
                    elif(currenttime.hour == t[0]):
                        if(currenttime.minute >= t[0].split(':')[1]):
                            return l
                            flag = True
                            break;
        f.close()
    def remove(self,l):
        l=",".join(l)
        l=l+'\n'
        f = open("E:\\Python Project\\Smart Alarm\\donottouch.txt",'r')
        alarms = f.readlines()
        f.close()
        alarms.remove(l)
        f = open("E:\\Python Project\\Smart Alarm\\donottouch.txt",'w')
        f.writelines(alarms)
        f.close()
        

        



    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())