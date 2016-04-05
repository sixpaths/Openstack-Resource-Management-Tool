# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Images.ui'
#
# Created: Wed Apr  6 03:17:33 2016
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

class Ui_Images(object):
    def setupUi(self, Images):
        Images.setObjectName(_fromUtf8("Images"))
        Images.resize(580, 361)
        Images.setMaximumSize(QtCore.QSize(580, 361))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../Downloads/openstack-dashboard.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Images.setWindowIcon(icon)
        self.tableWidget = QtGui.QTableWidget(Images)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 580, 361))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)

        self.retranslateUi(Images)
        QtCore.QMetaObject.connectSlotsByName(Images)

    def retranslateUi(self, Images):
        Images.setWindowTitle(_translate("Images", "Images", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Images", "Image ID", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Images", "Image Name", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Images", "Driver", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Images", "Extra", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Images = QtGui.QWidget()
    ui = Ui_Images()
    ui.setupUi(Images)
    Images.show()
    sys.exit(app.exec_())

