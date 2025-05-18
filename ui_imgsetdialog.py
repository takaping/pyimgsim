# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'imgsetdialog.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QListView,
    QPushButton, QSizePolicy, QWidget)

class Ui_imgSetDialog(object):
    def setupUi(self, imgSetDialog):
        if not imgSetDialog.objectName():
            imgSetDialog.setObjectName(u"imgSetDialog")
        imgSetDialog.resize(393, 320)
        self.realOpenButton = QPushButton(imgSetDialog)
        self.realOpenButton.setObjectName(u"realOpenButton")
        self.realOpenButton.setGeometry(QRect(20, 20, 81, 24))
        self.synthOpenButton = QPushButton(imgSetDialog)
        self.synthOpenButton.setObjectName(u"synthOpenButton")
        self.synthOpenButton.setGeometry(QRect(170, 20, 81, 24))
        self.realComboBox = QComboBox(imgSetDialog)
        self.realComboBox.setObjectName(u"realComboBox")
        self.realComboBox.setGeometry(QRect(20, 60, 80, 24))
        self.synthComboBox = QComboBox(imgSetDialog)
        self.synthComboBox.setObjectName(u"synthComboBox")
        self.synthComboBox.setGeometry(QRect(170, 50, 80, 24))
        self.similarityButton = QPushButton(imgSetDialog)
        self.similarityButton.setObjectName(u"similarityButton")
        self.similarityButton.setGeometry(QRect(20, 110, 75, 24))
        self.similarityListView = QListView(imgSetDialog)
        self.similarityListView.setObjectName(u"similarityListView")
        self.similarityListView.setGeometry(QRect(110, 110, 256, 192))

        self.retranslateUi(imgSetDialog)

        QMetaObject.connectSlotsByName(imgSetDialog)
    # setupUi

    def retranslateUi(self, imgSetDialog):
        imgSetDialog.setWindowTitle(QCoreApplication.translate("imgSetDialog", u"Dialog", None))
        self.realOpenButton.setText(QCoreApplication.translate("imgSetDialog", u"Open Real...", None))
        self.synthOpenButton.setText(QCoreApplication.translate("imgSetDialog", u"Open Synth...", None))
        self.similarityButton.setText(QCoreApplication.translate("imgSetDialog", u"Similarity", None))
    # retranslateUi

