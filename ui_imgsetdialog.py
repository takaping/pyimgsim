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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QLabel,
    QLineEdit, QListView, QPushButton, QSizePolicy,
    QWidget)

class Ui_imgSetDialog(object):
    def setupUi(self, imgSetDialog):
        if not imgSetDialog.objectName():
            imgSetDialog.setObjectName(u"imgSetDialog")
        imgSetDialog.resize(393, 358)
        self.realOpenButton = QPushButton(imgSetDialog)
        self.realOpenButton.setObjectName(u"realOpenButton")
        self.realOpenButton.setGeometry(QRect(20, 20, 81, 24))
        self.synthOpenButton = QPushButton(imgSetDialog)
        self.synthOpenButton.setObjectName(u"synthOpenButton")
        self.synthOpenButton.setGeometry(QRect(130, 20, 81, 24))
        self.realComboBox = QComboBox(imgSetDialog)
        self.realComboBox.setObjectName(u"realComboBox")
        self.realComboBox.setGeometry(QRect(20, 100, 80, 24))
        self.synthComboBox = QComboBox(imgSetDialog)
        self.synthComboBox.setObjectName(u"synthComboBox")
        self.synthComboBox.setGeometry(QRect(130, 100, 80, 24))
        self.similarityButton = QPushButton(imgSetDialog)
        self.similarityButton.setObjectName(u"similarityButton")
        self.similarityButton.setGeometry(QRect(20, 180, 75, 24))
        self.similarityListView = QListView(imgSetDialog)
        self.similarityListView.setObjectName(u"similarityListView")
        self.similarityListView.setGeometry(QRect(110, 181, 256, 171))
        self.realViewComboBox = QComboBox(imgSetDialog)
        self.realViewComboBox.addItem("")
        self.realViewComboBox.addItem("")
        self.realViewComboBox.setObjectName(u"realViewComboBox")
        self.realViewComboBox.setGeometry(QRect(20, 60, 80, 24))
        self.synthViewComboBox = QComboBox(imgSetDialog)
        self.synthViewComboBox.addItem("")
        self.synthViewComboBox.addItem("")
        self.synthViewComboBox.setObjectName(u"synthViewComboBox")
        self.synthViewComboBox.setGeometry(QRect(130, 60, 80, 24))
        self.numCumlustersEdit = QLineEdit(imgSetDialog)
        self.numCumlustersEdit.setObjectName(u"numCumlustersEdit")
        self.numCumlustersEdit.setGeometry(QRect(150, 150, 81, 21))
        self.numCumlustersEdit.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.label = QLabel(imgSetDialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 150, 111, 16))

        self.retranslateUi(imgSetDialog)

        QMetaObject.connectSlotsByName(imgSetDialog)
    # setupUi

    def retranslateUi(self, imgSetDialog):
        imgSetDialog.setWindowTitle(QCoreApplication.translate("imgSetDialog", u"Dialog", None))
        self.realOpenButton.setText(QCoreApplication.translate("imgSetDialog", u"Open Real...", None))
        self.synthOpenButton.setText(QCoreApplication.translate("imgSetDialog", u"Open Synth...", None))
        self.similarityButton.setText(QCoreApplication.translate("imgSetDialog", u"Similarity", None))
        self.realViewComboBox.setItemText(0, QCoreApplication.translate("imgSetDialog", u"Original", None))
        self.realViewComboBox.setItemText(1, QCoreApplication.translate("imgSetDialog", u"KeyPoints", None))

        self.synthViewComboBox.setItemText(0, QCoreApplication.translate("imgSetDialog", u"Original", None))
        self.synthViewComboBox.setItemText(1, QCoreApplication.translate("imgSetDialog", u"KeyPoints", None))

        self.numCumlustersEdit.setInputMask("")
        self.numCumlustersEdit.setText(QCoreApplication.translate("imgSetDialog", u"100", None))
        self.label.setText(QCoreApplication.translate("imgSetDialog", u"number of clusters", None))
    # retranslateUi

