# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'slav_time_gui.ui'
#
# Created: Sun Jan 18 23:06:22 2015
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(223, 76)
        self.progressBar_h = QtGui.QProgressBar(Form)
        self.progressBar_h.setGeometry(QtCore.QRect(110, 10, 118, 13))
        self.progressBar_h.setMaximum(15)
        self.progressBar_h.setProperty("value", 0)
        self.progressBar_h.setFormat(_fromUtf8(""))
        self.progressBar_h.setObjectName(_fromUtf8("progressBar_h"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 46, 13))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 46, 13))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 50, 46, 13))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_h = QtGui.QLabel(Form)
        self.label_h.setGeometry(QtCore.QRect(60, 10, 46, 13))
        font = QtGui.QFont()
        font.setKerning(True)
        self.label_h.setFont(font)
        self.label_h.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_h.setObjectName(_fromUtf8("label_h"))
        self.label_c = QtGui.QLabel(Form)
        self.label_c.setGeometry(QtCore.QRect(60, 30, 46, 13))
        self.label_c.setObjectName(_fromUtf8("label_c"))
        self.label_d = QtGui.QLabel(Form)
        self.label_d.setGeometry(QtCore.QRect(60, 50, 46, 13))
        self.label_d.setObjectName(_fromUtf8("label_d"))
        self.progressBar_c = QtGui.QProgressBar(Form)
        self.progressBar_c.setGeometry(QtCore.QRect(110, 30, 118, 13))
        self.progressBar_c.setMaximum(143)
        self.progressBar_c.setProperty("value", 0)
        self.progressBar_c.setFormat(_fromUtf8(""))
        self.progressBar_c.setObjectName(_fromUtf8("progressBar_c"))
        self.progressBar_d = QtGui.QProgressBar(Form)
        self.progressBar_d.setGeometry(QtCore.QRect(110, 50, 118, 13))
        self.progressBar_d.setMaximum(1296)
        self.progressBar_d.setProperty("value", 0)
        self.progressBar_d.setFormat(_fromUtf8(""))
        self.progressBar_d.setObjectName(_fromUtf8("progressBar_d"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Time", None))
        self.label.setText(_translate("Form", "Часов", None))
        self.label_2.setText(_translate("Form", "Частей", None))
        self.label_3.setText(_translate("Form", "Долей", None))
        self.label_h.setText(_translate("Form", "0", None))
        self.label_c.setText(_translate("Form", "0", None))
        self.label_d.setText(_translate("Form", "0", None))
