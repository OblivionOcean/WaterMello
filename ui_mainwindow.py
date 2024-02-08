# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'NuitritionUI.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(315, 113)
        icon = QIcon()
        icon.addFile(u"icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Opener = QPushButton(self.centralwidget)
        self.Opener.setObjectName(u"Opener")
        self.Opener.setGeometry(QRect(10, 50, 81, 41))
        self.Generator = QPushButton(self.centralwidget)
        self.Generator.setObjectName(u"Generator")
        self.Generator.setGeometry(QRect(90, 50, 71, 41))
        self.Deployer = QPushButton(self.centralwidget)
        self.Deployer.setObjectName(u"Deployer")
        self.Deployer.setGeometry(QRect(160, 50, 71, 41))
        self.Activator = QPushButton(self.centralwidget)
        self.Activator.setObjectName(u"Activator")
        self.Activator.setGeometry(QRect(230, 50, 71, 41))
        self.Starter = QPushButton(self.centralwidget)
        self.Starter.setObjectName(u"Starter")
        self.Starter.setGeometry(QRect(10, 10, 81, 41))
        self.Remover = QPushButton(self.centralwidget)
        self.Remover.setObjectName(u"Remover")
        self.Remover.setGeometry(QRect(230, 10, 71, 41))
        self.Ruler = QPushButton(self.centralwidget)
        self.Ruler.setObjectName(u"Ruler")
        self.Ruler.setGeometry(QRect(90, 10, 71, 41))
        self.About = QPushButton(self.centralwidget)
        self.About.setObjectName(u"About")
        self.About.setGeometry(QRect(160, 10, 71, 41))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"WaterMello", None))
        self.Opener.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u6587\u4ef6\u5939", None))
        self.Generator.setText(QCoreApplication.translate("MainWindow", u"\u751f\u6210", None))
        self.Deployer.setText(QCoreApplication.translate("MainWindow", u"\u90e8\u7f72", None))
        self.Activator.setText(QCoreApplication.translate("MainWindow", u"\u542f\u52a8", None))
        self.Starter.setText(QCoreApplication.translate("MainWindow", u"\u521d\u59cb\u5316", None))
        self.Remover.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u9664\u7f13\u5b58", None))
        self.Ruler.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u770b\u89c4\u5219", None))
        self.About.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
    # retranslateUi

