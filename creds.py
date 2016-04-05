# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'creds.ui'
#
# Created: Wed Apr  6 02:38:00 2016
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

class Ui_creds(object):
    def setupUi(self, creds):
        creds.setObjectName(_fromUtf8("creds"))
        creds.resize(580, 361)
        creds.setMaximumSize(QtCore.QSize(580, 361))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../Downloads/openstack-dashboard.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        creds.setWindowIcon(icon)
        self.formLayoutWidget = QtGui.QWidget(creds)
        self.formLayoutWidget.setGeometry(QtCore.QRect(40, 110, 491, 171))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setMargin(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.formLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.username = QtGui.QLineEdit(self.formLayoutWidget)
        self.username.setObjectName(_fromUtf8("username"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.username)
        self.label_2 = QtGui.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.passwd = QtGui.QLineEdit(self.formLayoutWidget)
        self.passwd.setEchoMode(QtGui.QLineEdit.Password)
        self.passwd.setObjectName(_fromUtf8("passwd"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.passwd)
        self.label_3 = QtGui.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.url = QtGui.QLineEdit(self.formLayoutWidget)
        self.url.setObjectName(_fromUtf8("url"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.url)
        self.label_4 = QtGui.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_4)
        self.project = QtGui.QLineEdit(self.formLayoutWidget)
        self.project.setObjectName(_fromUtf8("project"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.project)
        self.label_5 = QtGui.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_5)
        self.region = QtGui.QLineEdit(self.formLayoutWidget)
        self.region.setObjectName(_fromUtf8("region"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.region)
        self.verticalLayoutWidget = QtGui.QWidget(creds)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 10, 491, 80))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_7 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout.addWidget(self.label_7)
        self.label_8 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.verticalLayout.addWidget(self.label_8)
        self.label_6 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout.addWidget(self.label_6)
        self.save = QtGui.QPushButton(creds)
        self.save.setGeometry(QtCore.QRect(470, 290, 85, 27))
        self.save.setObjectName(_fromUtf8("save"))
        self.back = QtGui.QPushButton(creds)
        self.back.setGeometry(QtCore.QRect(370, 290, 85, 27))
        self.back.setObjectName(_fromUtf8("back"))

        self.retranslateUi(creds)
        QtCore.QMetaObject.connectSlotsByName(creds)

    def retranslateUi(self, creds):
        creds.setWindowTitle(_translate("creds", "Form", None))
        self.label.setText(_translate("creds", "Auth_Username", None))
        self.label_2.setText(_translate("creds", "Auth_Password", None))
        self.label_3.setText(_translate("creds", "Auth_URL", None))
        self.label_4.setText(_translate("creds", "Auth_Project_Name", None))
        self.label_5.setText(_translate("creds", "Auth_Region_Name", None))
        self.label_7.setText(_translate("creds", "You can get your credentials in openrc.sh file as follows:", None))
        self.label_8.setText(_translate("creds", "Project->Access and Security->Download OpenStack RC file.", None))
        self.label_6.setText(_translate("creds", "Note : Don\'\'t include \'/v2.0\' in auth_url", None))
        self.save.setText(_translate("creds", "Save", None))
        self.back.setText(_translate("creds", "Back", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    creds = QtGui.QWidget()
    ui = Ui_creds()
    ui.setupUi(creds)
    creds.show()
    sys.exit(app.exec_())

