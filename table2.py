# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'table2.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!
from pymongo import MongoClient
from PyQt5 import QtCore, QtGui, QtWidgets
import time
class Ui_Form1(object):
    def setupUi1(self, Form):
        Form.setObjectName("Form")
        Form.resize(878, 661)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(70, 80, 591, 481))
        self.tableWidget.setMinimumSize(QtCore.QSize(591, 0))
        self.tableWidget.setMaximumSize(QtCore.QSize(591, 16777215))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(200)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(400, 20, 111, 31))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(240, 20, 121, 31))
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        conn = MongoClient('127.0.0.1', 27017)
        db = conn.runoob  # 连接mydb数据库，没有则自动创建
        my_set = db.second
        i = 0
        for z in my_set.find().sort("date",-1):
            aa = z.get('id')
            bb = z.get('name')
            ff = z.get('date')
            aa1 = QtWidgets.QTableWidgetItem(aa)
            bb1 = QtWidgets.QTableWidgetItem(bb)
            ff1 = QtWidgets.QTableWidgetItem(ff)
            self.tableWidget.setItem(i, 0, aa1)
            self.tableWidget.setItem(i, 1, bb1)
            self.tableWidget.setItem(i, 2, ff1)
            i = i + 1

    def chazhao(self):
        text = self.lineEdit.text()
        item = self.tableWidget.findItems(text, QtCore.Qt.MatchExactly)
        row = item[0].row()
        self.tableWidget.verticalScrollBar().setSliderPosition(row)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "_id"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "date"))
        self.pushButton.setText(_translate("Form", "查找"))
        self.pushButton.clicked.connect(self.chazhao)



import sys
import table2
from PyQt5.QtWidgets import QApplication, QMainWindow
if __name__ =='__main__':
    print("主窗体2")
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = table2.Ui_Form1()
    ui.setupUi1(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

