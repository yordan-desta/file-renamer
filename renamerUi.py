# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'YoniAppUtility.ui'
#
# Created: Mon May 15 16:04:21 2017
#      by: PyQt4 UI code generator 4.10.4
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(500, 265)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 230, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.filePathEditText = QtGui.QTextEdit(Dialog)
        self.filePathEditText.setGeometry(QtCore.QRect(10, 30, 371, 30))
        self.filePathEditText.setObjectName(_fromUtf8("filePathEditText"))
        self.appendEditText = QtGui.QTextEdit(Dialog)
        self.appendEditText.setGeometry(QtCore.QRect(110, 80, 281, 31))
        self.appendEditText.setObjectName(_fromUtf8("appendEditText"))
        self.selectDir = QtGui.QPushButton(Dialog)
        self.selectDir.setGeometry(QtCore.QRect(390, 10, 98, 27))
        self.selectDir.setObjectName(_fromUtf8("selectDir"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 90, 91, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.selectFile = QtGui.QPushButton(Dialog)
        self.selectFile.setGeometry(QtCore.QRect(390, 40, 98, 27))
        self.selectFile.setObjectName(_fromUtf8("selectFile"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.selectDir.setText(_translate("Dialog", "select Dir", None))
        self.label.setText(_translate("Dialog", "Text Append", None))
        self.selectFile.setText(_translate("Dialog", "select File", None))

