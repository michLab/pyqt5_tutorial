# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'employer_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(430, 427)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(60, 380, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 20, 385, 351))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.dateEdit = QtWidgets.QDateEdit(self.layoutWidget)
        self.dateEdit.setObjectName("dateEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.dateEdit)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.comboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.comboBox_2 = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.comboBox_2)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBox)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.textEdit = QtWidgets.QTextEdit(self.layoutWidget)
        self.textEdit.setObjectName("textEdit")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.textEdit)
        self.label.setBuddy(self.lineEdit)
        self.label_2.setBuddy(self.dateEdit)
        self.label_3.setBuddy(self.comboBox)
        self.label_4.setBuddy(self.comboBox_2)
        self.label_6.setBuddy(self.doubleSpinBox)
        self.label_5.setBuddy(self.textEdit)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.lineEdit, self.dateEdit)
        Dialog.setTabOrder(self.dateEdit, self.comboBox)
        Dialog.setTabOrder(self.comboBox, self.comboBox_2)
        Dialog.setTabOrder(self.comboBox_2, self.doubleSpinBox)
        Dialog.setTabOrder(self.doubleSpinBox, self.textEdit)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Employee &name"))
        self.label_2.setText(_translate("Dialog", "&Employment date"))
        self.label_3.setText(_translate("Dialog", "&Department"))
        self.label_4.setText(_translate("Dialog", "&Position"))
        self.label_6.setText(_translate("Dialog", "&Annual salary"))
        self.label_5.setText(_translate("Dialog", "&Job description"))

