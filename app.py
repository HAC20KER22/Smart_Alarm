# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTextEdit, QTimeEdit, QWidget)
import sys
import ctypes
from PySide6 import QtWidgets

class Ui_MainWindow(object):
    def addalarm(self):
        f = open("E:\\Python Project\\Smart Alarm\\donottouch.txt",'a')
        title = self.titleinput.text()
        date = self.dateinput.text()
        time = self.timeinput.text()
        desc = self.description.toPlainText()
        if(title.isspace() or title==''):
            ctypes.windll.user32.MessageBoxW(0, "The Title is empty.", "Error!", 1)
        else:
            s=title+','+date+','+time+','+desc+'\n'
            f.write(str(s))
            f.close()
            sys.exit()



    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(746, 543)
        MainWindow.setMaximumSize(QSize(735, 550))
        MainWindow.setAnimated(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        self.timeinput = QTimeEdit(self.centralwidget)
        self.timeinput.setObjectName(u"timeinput")
        self.timeinput.setGeometry(QRect(120, 170, 161, 31))
        font = QFont()
        font.setPointSize(12)
        self.timeinput.setFont(font)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(90, 130, 101, 41))
        font1 = QFont()
        font1.setFamilies([u"Tahoma"])
        font1.setPointSize(12)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)

        self.dateinput = QDateEdit(self.centralwidget)
        self.dateinput.setObjectName(u"dateinput")
        self.dateinput.setGeometry(QRect(430, 170, 151, 31))
        self.dateinput.setFont(font)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(390, 130, 121, 41))
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.description = QTextEdit(self.centralwidget)
        self.description.setObjectName(u"description")
        self.description.setGeometry(QRect(80, 240, 571, 141))
        font2 = QFont()
        font2.setFamilies([u"Palatino Linotype"])
        font2.setPointSize(14)
        font2.setBold(False)
        self.description.setFont(font2)

        self.activate = QPushButton(self.centralwidget)
        self.activate.setObjectName(u"activate")
        self.activate.setGeometry(QRect(500, 420, 141, 41))
        self.activate.setFont(font)
        self.activate.clicked.connect(self.addalarm)

        self.titleinput = QLineEdit(self.centralwidget)
        self.titleinput.setObjectName(u"titleinput")
        self.titleinput.setGeometry(QRect(80, 50, 571, 41))
        font3 = QFont()
        font3.setFamilies([u"Palatino Linotype"])
        font3.setPointSize(14)
        font3.setBold(True)
        self.titleinput.setFont(font3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 746, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(statustip)
        MainWindow.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(statustip)
        self.timeinput.setStatusTip(QCoreApplication.translate("MainWindow", u"Time your alarm rings", None))
#endif // QT_CONFIG(statustip)
        self.label.setText(QCoreApplication.translate("MainWindow", u"Time", None))
#if QT_CONFIG(statustip)
        self.dateinput.setStatusTip(QCoreApplication.translate("MainWindow", u"Date of your alarm", None))
#endif // QT_CONFIG(statustip)
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Date", None))
#if QT_CONFIG(statustip)
        self.description.setStatusTip(QCoreApplication.translate("MainWindow", u"Description of the Alarm", None))
#endif // QT_CONFIG(statustip)
        self.description.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Palatino Linotype'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-size:7.8pt;\"><br /></p></body></html>", None))
        self.description.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Description", None))
#if QT_CONFIG(statustip)
        self.activate.setStatusTip(QCoreApplication.translate("MainWindow", u"Set the Alarm", None))
#endif // QT_CONFIG(statustip)
        self.activate.setText(QCoreApplication.translate("MainWindow", u"Activate", None))
#if QT_CONFIG(shortcut)
        self.activate.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.titleinput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Title", None))
    # retranslateUi

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())