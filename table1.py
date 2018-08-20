# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'table1.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!
from pymongo import MongoClient
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(914, 694)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 800, 601))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(4000)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(550, 610, 110, 50))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(360, 615, 141, 31))
        self.lineEdit.setObjectName("lineEdit")
        #self.newItem = QtWidgets.QTableWidgetItem('Item')
        #self.tableWidget.setItem(0, 1, self.newItem)
        self.retranslateUi(Form)

        QtCore.QMetaObject.connectSlotsByName(Form)
        conn = MongoClient('127.0.0.1', 27017)
        db = conn.runoob  # 连接mydb数据库，没有则自动创建
        my_set = db.first
        i=0#用不了for语句
        for z in my_set.find().sort("date",-1):
            aa = z.get('_id')
            bb=z.get('name')
            cc=z.get('image1')
            dd=z.get('image2')
            ee=z.get('mainnet')
            ff=z.get('date')
            #将数据库表闯入控件
            #print(aa)
            aa1=QtWidgets.QTableWidgetItem(aa)
            bb1 = QtWidgets.QTableWidgetItem(bb)
            cc1 = QtWidgets.QTableWidgetItem(cc)
            dd1 = QtWidgets.QTableWidgetItem(dd)
            ee1 = QtWidgets.QTableWidgetItem(ee)
            ff1 = QtWidgets.QTableWidgetItem(ff)
            self.tableWidget.setItem(i, 0, aa1)
            self.tableWidget.setItem(i, 1, bb1)
            self.tableWidget.setItem(i, 2, cc1)
            self.tableWidget.setItem(i, 3, dd1)
            self.tableWidget.setItem(i, 4, ee1)
            self.tableWidget.setItem(i, 5, ff1)
            i=i+1

    def chazhao(self):
        text=self.lineEdit.text()
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
        item.setText(_translate("Form", "image1"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "image2"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "mainnet"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "date"))
        self.pushButton.setText("查找")
        self.pushButton.clicked.connect(self.chazhao)

import sys
import table1
from PyQt5.QtWidgets import QApplication, QMainWindow
if __name__ =='__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = table1.Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())