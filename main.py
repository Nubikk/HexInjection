import inject_png
from PyQt6 import QtWidgets, uic
import easygui
import time


def fileopen_primary():
    win.main_label.setText(easygui.fileopenbox().replace("\\", "\\\\"))

def fileopen_second():
    win.second_label.setText(easygui.fileopenbox().replace("\\", "\\\\"))




def inject():
    if win.PNG.isChecked() and len(win.main_label.text()) > 0 and len(win.second_label.text()) > 0:
        inject_png.inject_png(win.second_label.text(), win.main_label.text())

    if len(win.StringLine.text()) > 0 and win.String.isChecked():
        inject_png.inject_str(win.StringLine.text(),win.main_label.text())
    if win.EXE.isChecked() and len(win.main_label.text()) > 0 and len(win.second_label.text()) > 0:
        inject_png.inject_exe(win.second_label.text(), win.main_label.text())



app = QtWidgets.QApplication([])
win = uic.loadUi("InjectionGUI.ui")

win.main_label.hide()
win.second_label.hide()

win.OpenMainFile.clicked.connect(fileopen_primary)

win.OpenSecondFile.clicked.connect(fileopen_second)

win.Start.clicked.connect(inject)

win.show()
app.exec()