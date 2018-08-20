# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'shares011.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import shares011
from PyQt5.QtWidgets import QApplication, QMainWindow,QMessageBox
import tkinter
from tkinter import messagebox
import urllib
import requests
from urllib import request
import subprocess, os
import re
from bs4 import BeautifulSoup
from multiprocessing import Process
import multiprocessing
from shares012 import *
from table1 import Ui_Form
from table2 import *
from pymongo import MongoClient
import time
import mul_process_package#打包多进程需要的模块


class MyWindow(QtWidgets.QWidget):#提示窗口
    def __init__(self):
        super(MyWindow, self).__init__()
        self.msg()
    def msg(self):
        reply = QMessageBox.information(self,  # 使用infomation信息框
                                        "提示",
                                        "全部下载完成",
                                        QMessageBox.Yes | QMessageBox.No)

class Ui_MainWindow(QtWidgets.QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(100, 320, 611, 121))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(270, 40, 221, 81))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(530, 520, 291, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(430, 500, 371, 21))
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 130, 221, 91))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(270, 230, 221, 80))
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.dd = 0 #电池条的百分比

    def makerrc(self):#创建图片保存的文件夹
        images = os.listdir('./sh/images/'+self.a)
        #qss = os.listdir('./sh/data')
        f = open('images.qrc', 'w+')
        f.write(u'<RCC>\n  <qresource prefix="newPrefix">\n')

        for item in images:#遍历文件夹中所有的图片文件
            f.write(u'\t\t<file>sh/images/'+self.a +'/'+ item + '</file>\n')

        #for item in qss:
            #f.write(u'<file alias="qss/' + item + '">qss/' + item + '</file>\n')

        f.write(u'</qresource>\n</RCC>')
        f.close()
        #将qrc资源文件转换成py文件
        pipe = subprocess.Popen(r'pyrcc5 -o images.py images.qrc', stdout=subprocess.PIPE, stdin=subprocess.PIPE,
                                stderr=subprocess.PIPE, creationflags=0x08)
    def start(self,dd):
        #开始爬取
        conn = MongoClient('127.0.0.1', 27017)
        db = conn.runoob  # 连接mydb数据库，没有则自动创建
        self.my_set = db.first#第一个表


        self.get()#获取股票代码
    def get(self):

        try:
            header = "Mozilla / 5.0(WindowsNT6.1;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 53.0.2785.104Safari / 537.36Core / 1.53.3427.400QQBrowser / 9.6.12201.400"
            url = "http://quote.eastmoney.com/stocklist.html"
            doc = urllib.request.urlopen(url)
            soup = BeautifulSoup(doc, "lxml")
            #爬取所有股票代码
            #tags=soup.find_all(target="_blank")
            #for tag in tags[84:]:
            #    tag1=tag.get_text()
            #    print(tag1)
            #爬取所有股票网址
            tags = soup.find_all(target="_blank")
        except Exception as err:
            print(err)

        try:#爬取范围
            for tag in tags[84:134]:#84开始，只爬取50个
                #0.0329全部股票的增加量
                self.dd = self.dd + 2 #电池每次加2
                self.progressBar.setValue(self.dd)

                #print("第"+str(self.aaa)+"个爬取开始")
                tag1=tag["href"]
                self.name=tag.text#获取股票名字
                print(self.name)
                r = requests.get(tag1, allow_redirects=False)#判断是否404
                if r.status_code == 404:
                    print("网站不存在")
                    continue

                p1 = Process(target=self.download(tag1), args=('process_name',))#多进程开始
                p1.start()

                #self.download(tag1)
            p1.join()#等待进程结束
        except Exception as err:
            print(err)

        #self.makerrc()
        if self.dd >= 100:
            self.dd = 0
            myshow = MyWindow()#电池满了提示

    def download(self,tag1):#下载图片，将爬取记录存到数据库
        header = "Mozilla / 5.0(WindowsNT6.1;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 53.0.2785.104Safari / 537.36Core / 1.53.3427.400QQBrowser / 9.6.12201.400"
        url=tag1
        self.mainnet=tag1
        doc = urllib.request.urlopen(url)#加不了头
        soup = BeautifulSoup(doc, "lxml")
        soup.originalEncoding
        # resp=urllib.request.urlopen(url)
        # data=resp.read()
        # print(data)
        # s=data.decode()
        # bs=BeautifulSoup(s,"lxml")
        tags = soup.find_all("img")


        self.a=time.strftime('%Y-%m-%d', time.localtime(time.time()))#获取时间
        for tag in tags:#遍历所有股票图片网址
            try:
                fn = tag["src"]

                if "imageType=r" in fn:
                    if fn[0] == "/":
                        fn = "http:" + fn
                    id = re.findall(r"=(\d+)&", fn)#通过正则表达式在图片地址中获取股票代码
                    #找到图片网址存入数据库
                    self.my_set.save({"_id":id[0],"name":self.name,"image1":fn,"image2":None,"mainnet":self.mainnet,"date":self.a})
                    #if os.path.exists("D:\\sh\images\\"+self.a+"\\")==False:
                    #    os.mkdir(r"D:\\sh\images\\"+self.a+"\\")
                    #path = "D:\\sh\images\\"+self.a+"\\" + id[0] + "[1].png"
                    self.id = id[0]
                    #request.urlretrieve(fn, path)
                if "KXL" in fn:
                    if fn[0] == "/":
                        fn = "http:" + fn
                    id = re.findall(r"=(\d+)&", fn)
                    #if os.path.exists("D:\\sh\images\\"+self.a+"\\")==False:
                    #    os.mkdir(r"D:\\sh\images\\"+self.a+"\\")
                    self.my_set.update({"image2":None},{"$set":{"image2":fn}})
                    #path = "D:\\sh\images\\"+self.a+"\\" + id[0] + ".png"
                    self.id = id[0]
                    #request.urlretrieve(fn, path)

                    #print("图片下载完成第"+str(self.aaa)+"张")


            except Exception as err:
                print(err)

    def zhongduan(self):
        sys.exit(0)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "爬取今天所有股票数据"))
        self.label.setText(_translate("MainWindow", "该程序的所有数据均来自于东方财富网"))
        self.label_2.setText(_translate("MainWindow", "声明：本软件不得用于商业用途，仅做学习交流与欣赏"))
        self.pushButton_2.setText(_translate("MainWindow", "股票查询"))
        self.pushButton.clicked.connect(self.start)
        self.pushButton_3.setText(_translate("MainWindow", "查看爬取内容"))




if __name__ =='__main__':
    multiprocessing.freeze_support()
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = shares011.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    #继承窗体2，显示股票查询窗体
    Dialog2 = QtWidgets.QMainWindow()
    ui2 = Ui_secondWindow()
    ui2.setupUi(Dialog2)
    bttn2 = ui.pushButton_2
    bttn2.clicked.connect(Dialog2.show)
    Dialog33 = QtWidgets.QMainWindow()
    ui33 = Ui_Form1()
    ui33.setupUi1(Dialog33)
    bttn33 = ui2.pushButton_3
    bttn33.clicked.connect(Dialog33.show)
    try:
        #显示股票数据窗体
        Dialog3 = QtWidgets.QMainWindow()
        ui3 = Ui_Form()
        ui3.setupUi(Dialog3)
        bttn3 = ui.pushButton_3
        bttn3.clicked.connect(Dialog3.show)
    except Exception as err:
        print(err)
    sys.exit(app.exec_())





