from distutils.core import setup
import py2exe

setup(windows=['slav_time_gui.pyw'], options={"py2exe" : {"includes" : ["sip"]}})
