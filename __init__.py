from PyQt4.QtCore import *
from PyQt4.QtGui import *

import renamerUi, renamer
import commonLib

from PyQt4 import QtGui
import sys

path = ""
appendText = ""

width = 500
height = 300

class RenamerApp(QtGui.QDialog, renamerUi.Ui_Dialog):
    def __init__(self):

        super(self.__class__, self).__init__()

        self.setupUi(self)

        self.setWindowTitle("Yoni's file renamer (by pyordan)")

        self.setFixedSize(width, height)

        self.filePathEditText.lineWrapMode()

        self.connect(self.selectDir, SIGNAL("clicked()"), self.selectDirClicked)

        self.connect(self.selectFile, SIGNAL("clicked()"), self.selectFileClicked)

    def selectDirClicked(self):

        directory = QtGui.QFileDialog.getExistingDirectory()

        print directory

        if commonLib.isFileOrDir(directory):
            self.filePathEditText.setText(directory)

    def selectFileClicked(self):

        global path

        _file = QtGui.QFileDialog.getOpenFileNameAndFilter()

        print _file[0]

        if (commonLib.isFileOrDir(_file[0])):
            self.filePathEditText.setText(_file[0])

    def accept(self):

        global appendText, path

        if QString.isNull(self.filePathEditText.toPlainText()) or QString.isEmpty(self.filePathEditText.toPlainText()):
            QMessageBox.about(self, "Error", "path doesn't exist")
            return

        path = str(self.filePathEditText.toPlainText())

        if QString.isNull(self.appendEditText.toPlainText()) or QString.isEmpty(self.appendEditText.toPlainText()):
            QMessageBox.about(self, "Error", "appeng text cant be empty")
            return

        appendText = str(self.appendEditText.toPlainText())

        if (commonLib.isFile(path)):
            renamer.appendNameOnFile(path, appendText)

        if (commonLib.isDir(path)):
            renamer.appendNameOnFilesInDir(path, appendText)

        sys.exit(0)


def main():
    app = QtGui.QApplication(sys.argv)
    form = RenamerApp()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()
