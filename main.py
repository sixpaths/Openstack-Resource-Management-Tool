from PyQt4 import QtGui
import sys
import ResourceManagement,creds,functions,welcome,Images
from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver
import os


class ResourceManagement(QtGui.QMainWindow,ResourceManagement.Ui_MainWindow):

    def __init__(self):
        super(self.__class__,self).__init__()
        self.setupUi(self)
        stackedWidget=self.stackedWidget
        welcome = Welcome(stackedWidget)
        stackedWidget.addWidget(welcome)
        stackedWidget.setCurrentWidget(welcome)



class Welcome(QtGui.QWidget,welcome.Ui_welcome):

    def __init__(self, stackedWidget, parent=None):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.getstarted.clicked.connect(lambda : self.toCreds(stackedWidget))

    def toCreds(self, stackedWidget):
        cred = Creds(stackedWidget)
        stackedWidget.addWidget(cred)
        stackedWidget.setCurrentWidget(cred)

class Creds(QtGui.QWidget,creds.Ui_creds):

    def __init__(self,stackedWidget,parent=None):
        super(Creds, self).__init__(parent)
        self.setupUi(self)
        self.save.clicked.connect(lambda : self.toFunction(stackedWidget))
        self.back.clicked.connect(lambda  : self.toWelcome(stackedWidget))
    def toFunction(self,stackedWidget):
        uname = self.username.text()
        auth_username = str(uname)
        passwd = self.passwd.text()
        url = self.url.text()
        project = self.project.text()
        region = self.region.text()
        auth_passwd = str(passwd)
        auth_url = str(url)
        project_name = str(project)
        region_name = str(region)
        provider = get_driver(Provider.OPENSTACK)
        conn = provider(auth_username,
                        auth_passwd,
                        ex_force_auth_url=auth_url,
                        ex_force_auth_version='2.0_password',
                        ex_tenant_name=project_name,
                        ex_force_service_region=region_name)
        functions=Function(conn,stackedWidget)
        stackedWidget.addWidget(functions)
        stackedWidget.setCurrentWidget(functions)

    def toWelcome(self,stackedWidget):
        welcome=Welcome(stackedWidget)
        stackedWidget.addWidget(welcome)
        stackedWidget.setCurrentWidget(welcome)


class Function(QtGui.QWidget,functions.Ui_functions):

    def __init__(self, conn, stackedWidget, parent=None):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.listImage.clicked.connect(lambda: self.toListImages(conn,stackedWidget))
        self.back1.clicked.connect(lambda  : self.toCreds(stackedWidget))
        self.window4 = None
        self.window5 = None
        self.window6 = None
        self.window7 = None
        self.window8 = None
        self.window9 = None
        self.window10 = None
        self.window11 = None
        self.window12 = None

    def toListImages(self,conn,stackedWidget):
        images = conn.list_images()
        if self.window4 == None:
            self.window4 = Images(images)
        self.window4.show()

    def toCreds(self,stackedWidget):
        creds=Creds(stackedWidget)
        stackedWidget.addWidget(creds)
        stackedWidget.setCurrentWidget(creds)



class Images(QtGui.QWidget,Images.Ui_Images):
    def __init__(self,images):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        rowpos=self.tableWidget.rowCount()
        for image in images:
            self.tableWidget.insertRow(rowpos)
            self.tableWidget.setItem(rowpos,0,QtGui.QTableWidgetItem(image.id))
            self.tableWidget.setItem(rowpos,1,QtGui.QTableWidgetItem(image.name))
            self.tableWidget.setItem(rowpos, 2, QtGui.QTableWidgetItem(str(image.driver)))
            self.tableWidget.setItem(rowpos, 3, QtGui.QTableWidgetItem(str(image.extra)))
            self.tableWidget.resizeColumnsToContents()
            self.tableWidget.resizeRowsToContents()
            rowpos=rowpos+1

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    form = ResourceManagement()
    form.show()
    sys.exit(app.exec_())