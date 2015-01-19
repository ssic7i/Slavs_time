__author__ = 'Serhii Sheiko sergy@sheyko.pp.ua'
# http://energodar.net/vedy/kalendar.html
# http://midgard-svaor.com/mernye-velichiny-nashix-predkov/

__timezone__ = +2  # timezone with no daylight saving time(winter time) in Kyiv

from PyQt4.QtGui import QSystemTrayIcon

import sl_time
import os
import sys
from PyQt4 import QtCore, QtGui
import datetime

from slav_time_gui_ui import Ui_Form

class MainWindow(QtGui.QMainWindow):

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        #if os.path.exists('slav_time_gui.ui'):
        #    uic.loadUi('slav_time_gui.ui', self)
        #elif os.path.exist(sys.argv[0][:0-len('slav_time_gui.pyw')] + 'slav_time_gui.ui'):
        #    uic.loadUi(sys.argv[0][:0-len('slav_time_gui.pyw')] + 'slav_time_gui.ui', self)
        self.ui=Ui_Form()
        self.ui.setupUi(self)

        if os.path.exists('slav_time_gui.png'):
            self.setWindowIcon(QtGui.QIcon('slav_time_gui.png'))
            self.trayIcon = QtGui.QSystemTrayIcon(QtGui.QIcon('slav_time_gui.png'))
        elif os.path.exist(sys.argv[0][:0-len('slav_time_gui.pyw')] + 'slav_time_gui.png'):
            self.setWindowIcon(QtGui.QIcon(sys.argv[0][:0-len('slav_time_gui.pyw')] + 'slav_time_gui.png'))
            self.trayIcon = QtGui.QSystemTrayIcon(QtGui.QIcon(sys.argv[0][:0-len('slav_time_gui.pyw')] + 'slav_time_gui.png'))

        #self.trayIcon = QtGui.QSystemTrayIcon(QtGui.QIcon('slav_time_gui.png'))
        self.trayIcon.show()

        h, c, d = sl_time.cur_conv_time(__timezone__)
        h = int(h)
        c = int(c)
        self.ui.label_h.setText(str(h))
        self.ui.label_c.setText(str(c))
        self.ui.label_d.setText(str(d))
        self.ui.progressBar_h.setValue(h)
        self.ui.progressBar_c.setValue(c)
        self.ui.progressBar_d.setValue(d)

        self.trayIcon.showMessage('Current time', str(h)+':'+str(c)+':'+str(d), QSystemTrayIcon.Information, 10000)

        self.timer = QtCore.QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.run_app)
        self.timer.start()


    def run_app(self):
        #self.trayIcon.show()
        h, c, d = sl_time.cur_conv_time(2)
        h = int(h)
        c = int(c)
        self.ui.label_h.setText(str(h))
        self.ui.label_c.setText(str(c))
        self.ui.label_d.setText(str(d))
        self.ui.progressBar_h.setValue(h)
        self.ui.progressBar_c.setValue(c)
        self.ui.progressBar_d.setValue(d)
        self.trayIcon.setToolTip(str(h)+':'+str(c)+':'+str(d))
        self.ui.label_cur_time.setText(str(datetime.datetime.utcnow()))

    #http://stackoverflow.com/questions/5506781/pyqt4-application-on-windows-is-crashing-on-exit
    def closeEvent(self, event):
        sys.exit(0)

app = QtGui.QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec_())