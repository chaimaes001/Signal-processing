# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 08:14:12 2021
@author: Chaimae
""" 
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DTW(object):
    def setupUi(self, DTW):
        DTW.setObjectName("DTW")
        DTW.resize(400, 276)
        self.label = QtWidgets.QLabel(DTW)
        self.label.setGeometry(QtCore.QRect(30, 40, 181, 16))
        self.label.setObjectName("label")
        
        self.comboBox_1 = QtWidgets.QComboBox(DTW)
        self.comboBox_1.setGeometry(QtCore.QRect(300, 40, 75, 23))
        self.comboBox_1.setObjectName("comboBox")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
               
        self.label_2 = QtWidgets.QLabel(DTW)
        self.label_2.setGeometry(QtCore.QRect(30, 80, 161, 16))
        self.label_2.setObjectName("label_2")
        
        self.pushButton_2 = QtWidgets.QPushButton(DTW)
        self.pushButton_2.setGeometry(QtCore.QRect(160, 140, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        
        self.comboBox = QtWidgets.QComboBox(DTW)
        self.comboBox.setGeometry(QtCore.QRect(300, 80, 71, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        
        self.label_3 = QtWidgets.QLabel(DTW)
        self.label_3.setGeometry(QtCore.QRect(130, 165, 181, 48))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(DTW)
        QtCore.QMetaObject.connectSlotsByName(DTW)

    def retranslateUi(self, DTW):
        _translate = QtCore.QCoreApplication.translate
        DTW.setWindowTitle(_translate("DTW", "DTW"))
        self.label.setText(_translate("DTW", "Choisir le premier mot "))
        self.label_3.setText(_translate("DTW", "Le résultat de la comparaison ici : "))
        self.label_2.setText(_translate("DTW", "Le deuxième mot "))
        self.pushButton_2.setText(_translate("DTW", "Comparer"))
        
        self.comboBox.setItemText(0, _translate("DTW", "Maison"))
        self.comboBox.setItemText(1, _translate("DTW", "Bonjour"))
        self.comboBox.setItemText(2, _translate("DTW", "Cartable"))
        self.comboBox.setItemText(3, _translate("DTW", "Ecole"))
        self.comboBox.setItemText(4, _translate("DTW", "Image"))
        self.comboBox.setItemText(5, _translate("DTW", "Chaimae"))
        self.comboBox.setItemText(6, _translate("DTW", "Matlab"))
        self.comboBox.setItemText(7, _translate("DTW", "Parole"))
        self.comboBox.setItemText(8, _translate("DTW", "Aujourdhui"))
        self.comboBox.setItemText(9, _translate("DTW", "Bonsoir"))
        
        self.comboBox_1.setItemText(0, _translate("DTW", "Maison"))
        self.comboBox_1.setItemText(1, _translate("DTW", "Bonjour"))
        self.comboBox_1.setItemText(2, _translate("DTW", "Cartable"))
        self.comboBox_1.setItemText(3, _translate("DTW", "Ecole"))
        self.comboBox_1.setItemText(4, _translate("DTW", "Image"))
        self.comboBox_1.setItemText(5, _translate("DTW", "Chaimae"))
        self.comboBox_1.setItemText(6, _translate("DTW", "Matlab"))
        self.comboBox_1.setItemText(7, _translate("DTW", "Parole"))
        self.comboBox_1.setItemText(8, _translate("DTW", "Aujourdhui"))
        self.comboBox_1.setItemText(9, _translate("DTW", "Bonsoir"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DTW = QtWidgets.QDialog()
    ui = Ui_DTW()
    ui.setupUi(DTW)
    DTW.show()
    sys.exit(app.exec_())

