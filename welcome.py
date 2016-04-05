# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'welcome.ui'
#
# Created: Wed Apr  6 02:38:02 2016
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

class Ui_welcome(object):
    def setupUi(self, welcome):
        welcome.setObjectName(_fromUtf8("welcome"))
        welcome.resize(580, 361)
        self.verticalWidget = QtGui.QWidget(welcome)
        self.verticalWidget.setGeometry(QtCore.QRect(10, 20, 530, 237))
        self.verticalWidget.setObjectName(_fromUtf8("verticalWidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalWidget)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_10 = QtGui.QLabel(self.verticalWidget)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.verticalLayout_2.addWidget(self.label_10)
        self.label_11 = QtGui.QLabel(self.verticalWidget)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.verticalLayout_2.addWidget(self.label_11)
        self.gridWidget_2 = QtGui.QWidget(self.verticalWidget)
        self.gridWidget_2.setObjectName(_fromUtf8("gridWidget_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.gridWidget_2)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_12 = QtGui.QLabel(self.gridWidget_2)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout_2.addWidget(self.label_12, 0, 0, 1, 1)
        self.label_13 = QtGui.QLabel(self.gridWidget_2)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.gridLayout_2.addWidget(self.label_13, 1, 0, 1, 1)
        self.label_14 = QtGui.QLabel(self.gridWidget_2)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout_2.addWidget(self.label_14, 2, 0, 1, 1)
        self.label_15 = QtGui.QLabel(self.gridWidget_2)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.gridLayout_2.addWidget(self.label_15, 4, 0, 1, 1)
        self.label_16 = QtGui.QLabel(self.gridWidget_2)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.gridLayout_2.addWidget(self.label_16, 3, 0, 1, 1)
        self.label_17 = QtGui.QLabel(self.gridWidget_2)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.gridLayout_2.addWidget(self.label_17, 5, 0, 1, 1)
        self.label_18 = QtGui.QLabel(self.gridWidget_2)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.gridLayout_2.addWidget(self.label_18, 6, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.gridWidget_2)
        self.getstarted = QtGui.QPushButton(welcome)
        self.getstarted.setGeometry(QtCore.QRect(380, 270, 151, 51))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.getstarted.sizePolicy().hasHeightForWidth())
        self.getstarted.setSizePolicy(sizePolicy)
        self.getstarted.setObjectName(_fromUtf8("getstarted"))

        self.retranslateUi(welcome)
        QtCore.QMetaObject.connectSlotsByName(welcome)

    def retranslateUi(self, welcome):
        welcome.setWindowTitle(_translate("welcome", "Welcome", None))
        self.label_10.setText(_translate("welcome", "Welcome to OpenStack Resource Management Tool. This app will help you to", None))
        self.label_11.setText(_translate("welcome", "perform multiple cloud management tasks as follows: ", None))
        self.label_12.setText(_translate("welcome", "1. List available cloud images", None))
        self.label_13.setText(_translate("welcome", "2. List available flavours", None))
        self.label_14.setText(_translate("welcome", "3. Create an instance", None))
        self.label_15.setText(_translate("welcome", "5. Import Keypairs", None))
        self.label_16.setText(_translate("welcome", "4. Delete an instance", None))
        self.label_17.setText(_translate("welcome", "6. Add security Groups", None))
        self.label_18.setText(_translate("welcome", "7. Associate Floating IP\'s", None))
        self.getstarted.setText(_translate("welcome", "Get Started", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    welcome = QtGui.QWidget()
    ui = Ui_welcome()
    ui.setupUi(welcome)
    welcome.show()
    sys.exit(app.exec_())

