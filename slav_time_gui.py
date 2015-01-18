__author__ = 'Serhii Sheiko sergy@sheyko.pp.ua'
# http://energodar.net/vedy/kalendar.html
# http://midgard-svaor.com/mernye-velichiny-nashix-predkov/

__timezone__ = +2  # timezone with no daylight saving time(winter time) in Kyiv

from PyQt4.QtGui import QSystemTrayIcon

import sl_time
import os
import sys
from PyQt4 import QtCore, QtGui, uic

class MainWindow(QtGui.QMainWindow):

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        if os.path.exists('slav_time_gui.ui'):
            uic.loadUi('slav_time_gui.ui', self)
        elif os.path.exist(sys.argv[0][:0-len('slav_time_gui.py')] + 'slav_time_gui.ui'):
            uic.loadUi(sys.argv[0][:0-len('slav_time_gui.py')] + 'slav_time_gui.ui', self)
        if os.path.exists('slav_time_gui.png'):
            self.setWindowIcon(QtGui.QIcon('slav_time_gui.png'))

        self.trayIcon = QtGui.QSystemTrayIcon(QtGui.QIcon('slav_time_gui.png'))
        self.trayIcon.show()

        h, c, d = sl_time.cur_conv_time(__timezone__)
        h = int(h)
        c = int(c)
        self.label_h.setText(str(h))
        self.label_c.setText(str(c))
        self.label_d.setText(str(d))
        self.progressBar_h.setValue(h)
        self.progressBar_c.setValue(c)
        self.progressBar_d.setValue(d)

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
        self.label_h.setText(str(h))
        self.label_c.setText(str(c))
        self.label_d.setText(str(d))
        self.progressBar_h.setValue(h)
        self.progressBar_c.setValue(c)
        self.progressBar_d.setValue(d)
        self.trayIcon.setToolTip(str(h)+':'+str(c)+':'+str(d))

    #http://stackoverflow.com/questions/5506781/pyqt4-application-on-windows-is-crashing-on-exit
    def closeEvent(self, event):
        exit()

app = QtGui.QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec_())