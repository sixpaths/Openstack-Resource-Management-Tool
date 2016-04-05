# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'functions.ui'
#
# Created: Wed Apr  6 02:37:57 2016
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

class Ui_functions(object):
    def setupUi(self, functions):
        functions.setObjectName(_fromUtf8("functions"))
        functions.resize(580, 361)
        functions.setMaximumSize(QtCore.QSize(580, 361))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../Downloads/openstack-dashboard.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        functions.setWindowIcon(icon)
        self.verticalLayoutWidget = QtGui.QWidget(functions)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 10, 471, 291))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setSpacing(15)
        self.horizontalLayout_8.setMargin(4)
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.listImage = QtGui.QPushButton(self.verticalLayoutWidget)
        self.listImage.setObjectName(_fromUtf8("listImage"))
        self.horizontalLayout_8.addWidget(self.listImage)
        self.listFlavour = QtGui.QPushButton(self.verticalLayoutWidget)
        self.listFlavour.setObjectName(_fromUtf8("listFlavour"))
        self.horizontalLayout_8.addWidget(self.listFlavour)
        self.creatInstance = QtGui.QPushButton(self.verticalLayoutWidget)
        self.creatInstance.setObjectName(_fromUtf8("creatInstance"))
        self.horizontalLayout_8.addWidget(self.creatInstance)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setSpacing(15)
        self.horizontalLayout_10.setMargin(4)
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.destroyInstance = QtGui.QPushButton(self.verticalLayoutWidget)
        self.destroyInstance.setObjectName(_fromUtf8("destroyInstance"))
        self.horizontalLayout_10.addWidget(self.destroyInstance)
        self.importKeypair = QtGui.QPushButton(self.verticalLayoutWidget)
        self.importKeypair.setObjectName(_fromUtf8("importKeypair"))
        self.horizontalLayout_10.addWidget(self.importKeypair)
        self.addSecurity = QtGui.QPushButton(self.verticalLayoutWidget)
        self.addSecurity.setObjectName(_fromUtf8("addSecurity"))
        self.horizontalLayout_10.addWidget(self.addSecurity)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setSpacing(15)
        self.horizontalLayout_7.setMargin(4)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.privateIP = QtGui.QPushButton(self.verticalLayoutWidget)
        self.privateIP.setObjectName(_fromUtf8("privateIP"))
        self.horizontalLayout_7.addWidget(self.privateIP)
        self.publicIP = QtGui.QPushButton(self.verticalLayoutWidget)
        self.publicIP.setObjectName(_fromUtf8("publicIP"))
        self.horizontalLayout_7.addWidget(self.publicIP)
        self.floatingIP = QtGui.QPushButton(self.verticalLayoutWidget)
        self.floatingIP.setObjectName(_fromUtf8("floatingIP"))
        self.horizontalLayout_7.addWidget(self.floatingIP)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.back1 = QtGui.QPushButton(functions)
        self.back1.setGeometry(QtCore.QRect(410, 310, 98, 27))
        self.back1.setObjectName(_fromUtf8("back1"))

        self.retranslateUi(functions)
        QtCore.QMetaObject.connectSlotsByName(functions)

    def retranslateUi(self, functions):
        functions.setWindowTitle(_translate("functions", "Functions", None))
        self.listImage.setText(_translate("functions", "List Images", None))
        self.listFlavour.setText(_translate("functions", "List Flavours", None))
        self.creatInstance.setText(_translate("functions", "Create Instance", None))
        self.destroyInstance.setText(_translate("functions", "Destroy Instance", None))
        self.importKeypair.setText(_translate("functions", "Import Keypair", None))
        self.addSecurity.setText(_translate("functions", "Add Security Group", None))
        self.privateIP.setText(_translate("functions", "Get Private IP", None))
        self.publicIP.setText(_translate("functions", "Get Public IP", None))
        self.floatingIP.setText(_translate("functions", "Associate Floating IP", None))
        self.back1.setText(_translate("functions", "Back", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    functions = QtGui.QWidget()
    ui = Ui_functions()
    ui.setupUi(functions)
    functions.show()
    sys.exit(app.exec_())

