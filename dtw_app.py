# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 12:39:42 2021
@author: Chaimae
"""
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from main import Ui_DTW
import sounddevice as sd
from scipy.io.wavfile import write
from function import detecter_mot

app = QtWidgets.QApplication(sys.argv)
DTW = QtWidgets.QDialog()
ui = Ui_DTW()
ui.setupUi(DTW)
DTW.show()   

def pressed():
    mot=ui.comboBox.currentText()
    mot1=ui.comboBox_1.currentText()
    print("here test pressed fct mot ="+str(mot))
    resultat=detecter_mot(mot,mot1)
    ui.label_3.setText(resultat)

       
#connexions
#ui.pushButton.clicked.connect(enregistrer)
ui.pushButton_2.clicked.connect(pressed)

sys.exit(app.exec_())