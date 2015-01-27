# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\sergy\Dropbox\slav_time\slav_time_gui.ui'
#
# Created: Tue Jan 27 23:54:18 2015
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
        Form.resize(200, 200)
        Form.setMinimumSize(QtCore.QSize(200, 200))
        Form.setMaximumSize(QtCore.QSize(200, 200))
        Form.setBaseSize(QtCore.QSize(200, 200))
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
        self.label_cur_time = QtGui.QLabel(Form)
        self.label_cur_time.setGeometry(QtCore.QRect(10, 180, 201, 16))
        self.label_cur_time.setObjectName(_fromUtf8("label_cur_time"))
        self.label_hour_name = QtGui.QLabel(Form)
        self.label_hour_name.setGeometry(QtCore.QRect(10, 70, 181, 16))
        self.label_hour_name.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.label_hour_name.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_hour_name.setObjectName(_fromUtf8("label_hour_name"))
        self.label_hour_descr = QtGui.QLabel(Form)
        self.label_hour_descr.setGeometry(QtCore.QRect(10, 90, 181, 16))
        self.label_hour_descr.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.label_hour_descr.setObjectName(_fromUtf8("label_hour_descr"))
        self.label_hour_descr_2 = QtGui.QLabel(Form)
        self.label_hour_descr_2.setGeometry(QtCore.QRect(10, 110, 101, 16))
        self.label_hour_descr_2.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.label_hour_descr_2.setObjectName(_fromUtf8("label_hour_descr_2"))
        self.label_hour_descr_3 = QtGui.QLabel(Form)
        self.label_hour_descr_3.setGeometry(QtCore.QRect(10, 127, 111, 16))
        self.label_hour_descr_3.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.label_hour_descr_3.setObjectName(_fromUtf8("label_hour_descr_3"))
        self.label_hour_descr_4 = QtGui.QLabel(Form)
        self.label_hour_descr_4.setGeometry(QtCore.QRect(10, 160, 111, 16))
        self.label_hour_descr_4.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.label_hour_descr_4.setObjectName(_fromUtf8("label_hour_descr_4"))
        self.label_round_years = QtGui.QLabel(Form)
        self.label_round_years.setGeometry(QtCore.QRect(120, 110, 46, 16))
        self.label_round_years.setObjectName(_fromUtf8("label_round_years"))
        self.label_round_life = QtGui.QLabel(Form)
        self.label_round_life.setGeometry(QtCore.QRect(120, 127, 46, 16))
        self.label_round_life.setObjectName(_fromUtf8("label_round_life"))
        self.label_cpsc = QtGui.QLabel(Form)
        self.label_cpsc.setGeometry(QtCore.QRect(120, 160, 46, 16))
        self.label_cpsc.setObjectName(_fromUtf8("label_cpsc"))
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(10, 145, 31, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_month = QtGui.QLabel(Form)
        self.label_month.setGeometry(QtCore.QRect(50, 145, 61, 16))
        self.label_month.setObjectName(_fromUtf8("label_month"))
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(120, 145, 31, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_date = QtGui.QLabel(Form)
        self.label_date.setGeometry(QtCore.QRect(160, 145, 31, 16))
        self.label_date.setObjectName(_fromUtf8("label_date"))

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
        self.label_cur_time.setText(_translate("Form", "0", None))
        self.label_hour_name.setText(_translate("Form", "0", None))
        self.label_hour_descr.setText(_translate("Form", "0", None))
        self.label_hour_descr_2.setText(_translate("Form", "Лето в круге лет", None))
        self.label_hour_descr_3.setText(_translate("Form", "Лето в круге жизни", None))
        self.label_hour_descr_4.setText(_translate("Form", "Лето С.М.З.Х", None))
        self.label_round_years.setText(_translate("Form", "0", None))
        self.label_round_life.setText(_translate("Form", "0", None))
        self.label_cpsc.setText(_translate("Form", "0", None))
        self.label_4.setText(_translate("Form", "Месяц", None))
        self.label_month.setText(_translate("Form", "0", None))
        self.label_5.setText(_translate("Form", "Число", None))
        self.label_date.setText(_translate("Form", "0", None))

