#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets
import urllib
import requests
from urllib import request
import subprocess, os
import re
from bs4 import BeautifulSoup
from pymongo import MongoClient#芒果数据库
import time
import images#资源文件载入
from imp import reload
import importlib#模块重载
from table2 import *
class Ui_secondWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1202, 889)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(370, 30, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(540, 30, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(710, 30, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 248, 1191, 201))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_17 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_17.setStyleSheet("font: 75 16pt \"Aharoni\";")
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 0, 4, 1, 1)
        self.label_004 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_004.setStyleSheet("font: 75 24pt \"Aharoni\";")
        self.label_004.setObjectName("label_004")
        self.gridLayout.addWidget(self.label_004, 0, 7, 1, 1)
        self.label_008 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_008.setStyleSheet("font: 75 24pt \"Aharoni\";")
        self.label_008.setObjectName("label_008")
        self.gridLayout.addWidget(self.label_008, 4, 1, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_23.setStyleSheet("font: 75 16pt \"Aharoni\";")
        self.label_23.setObjectName("label_23")
        self.gridLayout.addWidget(self.label_23, 4, 2, 1, 1)
        self.label_009 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_009.setStyleSheet("font: 75 24pt \"Aharoni\";")
        self.label_009.setObjectName("label_009")
        self.gridLayout.addWidget(self.label_009, 4, 3, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_25.setStyleSheet("font: 75 16pt \"Aharoni\";")
        self.label_25.setObjectName("label_25")
        self.gridLayout.addWidget(self.label_25, 4, 4, 1, 1)
        self.label_0010 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_0010.setStyleSheet("font: 75 24pt \"Aharoni\";")
        self.label_0010.setObjectName("label_0010")
        self.gridLayout.addWidget(self.label_0010, 4, 5, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_27.setStyleSheet("font: 75 16pt \"Aharoni\";")
        self.label_27.setObjectName("label_27")
        self.gridLayout.addWidget(self.label_27, 4, 6, 1, 1)
        self.label_0011 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_0011.setStyleSheet("font: 75 24pt \"Aharoni\";")
        self.label_0011.setObjectName("label_0011")
        self.gridLayout.addWidget(self.label_0011, 4, 7, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_11.setStyleSheet("font: 75 16pt \"Aharoni\";")
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 4, 10, 1, 1)
        self.label_007 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_007.setStyleSheet("font: 75 24pt \"Aharoni\";")
        self.label_007.setObjectName("label_007")
        self.gridLayout.addWidget(self.label_007, 0, 13, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_13.setStyleSheet("font: 75 16pt \"Aharoni\";")
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 4, 12, 1, 1)
        self.label_0014 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_0014.setStyleSheet("font: 75 24pt \"Aharoni\";")
        self.label_0014.setObjectName("label_0014")
        self.gridLayout.addWidget(self.label_0014, 4, 13, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_16.setStyleSheet("font: 75 16pt \"Aharoni\";")
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 0, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setStyleSheet("font: 75 16pt \"Aharoni\";")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 8, 1, 1)
        self.label_0013 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_0013.setStyleSheet("font: 75 24pt \"Aharoni\";")
        self.label_0013.setObjectName("label_0013")
        self.gridLayout.addWidget(self.label_0013, 4, 11, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_8.setStyleSheet("font: 75 16pt \"Aharoni\";")
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 0, 12, 1, 1)
        self.label_002 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_002.setStyleSheet("font: 75 24pt \"Aharoni\";")
        self.label_002.setObjectName("label_002")
        self.gridLayout.addWidget(self.label_002, 0, 3, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_18.setStyleSheet("font: 75 16pt \"Aharoni\";")
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 0, 6, 1, 1)
        self.label_005 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_005.setStyleSheet("font: 75 24pt \"Aharoni\";")
        self.label_005.setObjectName("label_005")
        self.gridLayout.addWidget(self.label_005, 0, 9, 1, 1)
        self.label_0012 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_0012.setStyleSheet("font: 75 24pt \"Aharoni\";")
        self.label_0012.setObjectName("label_0012")
        self.gridLayout.addWidget(self.label_0012, 4, 9, 1, 1)
        self.label_006 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_006.setStyleSheet("font: 75 24pt \"Aharoni\";")
        self.label_006.setObjectName("label_006")
        self.gridLayout.addWidget(self.label_006, 0, 11, 1, 1)
        self.label_001 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_001.setMinimumSize(QtCore.QSize(70, 96))
        self.label_001.setStyleSheet("font: 75 20pt \"Aharoni\";")
        self.label_001.setObjectName("label_001")
        self.gridLayout.addWidget(self.label_001, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setStyleSheet("font: 75 16pt \"Aharoni\";")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 4, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setStyleSheet("font: 75 16pt \"Aharoni\";")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 8, 1, 1)
        self.label_003 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_003.setStyleSheet("font: 75 24pt \"Aharoni\";")
        self.label_003.setObjectName("label_003")
        self.gridLayout.addWidget(self.label_003, 0, 5, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setStyleSheet("font: 75 16pt \"Aharoni\";")
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 10, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setStyleSheet("font: 75 16pt \"Aharoni\";")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(160, 30, 141, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label_29 = QtWidgets.QLabel(self.centralwidget)
        self.label_29.setGeometry(QtCore.QRect(20, 30, 131, 31))
        self.label_29.setStyleSheet("font: 75 10pt \"Aharoni\";")
        self.label_29.setObjectName("label_29")
        self.name = QtWidgets.QLabel(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(50, 100, 201, 111))
        self.name.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 75 30pt \"Aharoni\";")
        self.name.setObjectName("name")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(420, 130, 121, 51))
        self.label_5.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 75 25pt \"Aharoni\";")
        self.label_5.setObjectName("label_5")
        self.label_444 = QtWidgets.QLabel(self.centralwidget)
        self.label_444.setGeometry(QtCore.QRect(780, 100, 201, 51))
        self.label_444.setStyleSheet("font: 75 20pt \"Aharoni\";")
        self.label_444.setObjectName("label_444")
        self.label_555 = QtWidgets.QLabel(self.centralwidget)
        self.label_555.setGeometry(QtCore.QRect(780, 160, 221, 71))
        self.label_555.setStyleSheet("font: 75 20pt \"Aharoni\";")
        self.label_555.setObjectName("label_555")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(631, 110, 141, 31))
        self.label_10.setStyleSheet("font: 75 16pt \"Aharoni\";")
        self.label_10.setObjectName("label_10")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(660, 170, 121, 41))
        self.label_12.setStyleSheet("font: 75 16pt \"Aharoni\";")
        self.label_12.setObjectName("label_12")
        self.label_333 = QtWidgets.QLabel(self.centralwidget)
        self.label_333.setGeometry(QtCore.QRect(300, 130, 131, 51))
        self.label_333.setStyleSheet("font: 75 14pt \"Aharoni\";")
        self.label_333.setObjectName("label_333")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 450, 551, 401))
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(600, 450, 631, 401))
        self.label_9.setObjectName("label_9")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1202, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.a = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        self.b = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    def labelset(self):#将爬取的信息显示
        datalist = self.data.split(',')
        self.label_5.setText(datalist[3])
        self.label_444.setText(datalist[4])
        self.label_555.setText(datalist[5])
        self.name.setText(datalist[2])
        self.name1=datalist[2]
        self.label_001.setText(datalist[6])
        self.label_002.setText(datalist[8])
        self.label_003.setText(datalist[10])
        self.label_004.setText(datalist[12])
        self.label_005.setText(datalist[14])
        self.label_006.setText(datalist[16])
        self.label_007.setText(datalist[20].replace('")',''))
        self.label_008.setText(datalist[7])
        self.label_009.setText(datalist[9])
        self.label_0010.setText(datalist[11])
        self.label_0011.setText(datalist[13])
        self.label_0012.setText(datalist[15])
        self.label_0013.setText(datalist[17])
        self.label_0014.setText(datalist[19])
    def chaxun(self):#显示图片
        try:
            self.get()
            self.download()
            self.makerrc()
            self.dm = self.lineEdit.text()

            header="Mozilla / 5.0(WindowsNT6.1;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 53.0.2785.104Safari / 537.36Core / 1.53.3427.400QQBrowser / 9.6.12201.400"
            url="http://nufm.dfcfw.com/EM_Finance2014NumericApplication/JS.aspx?" \
                "cb=jQuery132142696879330691995_1508060826368&type=CT&cmd=" + self.id + "&sty=FPFB&st=z&js=((x))&token=4f1862fc3b5e77c150a2b985b12db0fd&_=1508060846579"
            #print(url)

            return_data = requests.get(url,header)
            self.data=return_data.text
            #print(return_data.text)
            self.labelset()
            conn = MongoClient('127.0.0.1', 27017)
            db = conn.runoob  # 连接mydb数据库，没有则自动创建
            self.my_set = db.second#第二个表，查询记录的
            self.my_set.save({"id": self.dm, "name": self.name1, "date": self.b})

        except Exception as err:
            print(err)
    def chakan(self):
        try:
            self.get()

            import images
            self.label_7.setPixmap(QtGui.QPixmap(""))
            self.label_7.setPixmap(QtGui.QPixmap(""))
            #显示图片
            self.label_7.setPixmap(QtGui.QPixmap(":/newPrefix/sh/images/"+self.a+"/" + self.id + ".png"))
            self.label_9.setPixmap(QtGui.QPixmap(":/newPrefix/sh/images/" + self.a + "/" + self.id + "[1].png"))
        except Exception as err:
            print(err)
    def makerrc(self):#创建图片保存的文件夹
        try:
            print(self.a)
            images = os.listdir('./sh/images/'+self.a)
            #qss = os.listdir('./sh/data')
            f = open('images.qrc', 'w+')
            f.write(u'<RCC>\n  <qresource prefix="newPrefix">\n')

            for item in images:
                f.write(u'\t\t<file>sh/images/'+self.a +'/'+ item + '</file>\n')

            #for item in qss:
                #f.write(u'<file alias="qss/' + item + '">qss/' + item + '</file>\n')

            f.write(u'  </qresource>\n</RCC>')
            f.close()

            pipe = subprocess.Popen(r'pyrcc5 -o images.py images.qrc', stdout=subprocess.PIPE, stdin=subprocess.PIPE,
                                    stderr=subprocess.PIPE, creationflags=0x08)
        except Exception as err:
            print(err)

    def download(self):#下载图片
        try:

            conn = MongoClient('127.0.0.1', 27017)
            db = conn.runoob  # 连接mydb数据库，没有则自动创建
            my_set = db.first
            for i in my_set.find({"_id":self.id}):#获取数据库中的图片网址
                im1 = i.get('image1')
                im2 = i.get('image2')
            header = "Mozilla / 5.0(WindowsNT6.1;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 53.0.2785.104Safari / 537.36Core / 1.53.3427.400QQBrowser / 9.6.12201.400"

            '''if os.path.exists("D:\\sh\images\\"+self.a+"\\")==False:
                os.mkdir(r"D:\\sh\images\\"+self.a+"\\")
            path2 = "D:\\sh\images\\"+self.a+"\\" + self.id + "[1].png"
            path1 = "D:\\sh\images\\"+self.a+"\\" + self.id + ".png"
            '''
            if os.path.exists("./sh/images/" + self.a ) == False:
                os.mkdir(r"./sh/images/" + self.a)
            path2 = "./sh/images/" + self.a +"/"+ self.id + "[1].png"
            path1 = "./sh/images/" + self.a +"/"+ self.id + ".png"
            request.urlretrieve(im1, path1)
            request.urlretrieve(im2, path2)
        except Exception as err:
            print(err)







    def get(self):#爬取股票的代码
        try:
            self.dm = self.lineEdit.text()
            url = "http://quote.eastmoney.com/sz" + self.dm + ".html"
            r = requests.get(url, allow_redirects=False)
            if r.status_code==404:
                url = "http://quote.eastmoney.com/sh" + self.dm + ".html"
            doc = urllib.request.urlopen(url)
            soup = BeautifulSoup(doc, "lxml")
            soup.originalEncoding
            tags = soup.find_all("img")
        except Exception as err:
            print(err)
        for tag in tags:
            fn = tag["src"]
            if "KXL" in fn:
                if fn[0] == "/":
                    fn = "http:" + fn
                id = re.findall(r"=(\d+)&", fn)
                self.id = id[0]
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "查询"))
        self.pushButton.clicked.connect(self.chaxun)
        self.pushButton_2.setText(_translate("MainWindow", "查看走势"))
        self.pushButton_2.clicked.connect(self.chakan)
        self.pushButton_3.setText(_translate("MainWindow", "查询记录"))


        self.label_17.setText(_translate("MainWindow", "涨停:"))
        self.label_004.setText(_translate("MainWindow", "-"))
        self.label_008.setText(_translate("MainWindow", "-"))
        self.label_23.setText(_translate("MainWindow", "最低:"))
        self.label_009.setText(_translate("MainWindow", "-"))
        self.label_25.setText(_translate("MainWindow", "跌停:"))
        self.label_0010.setText(_translate("MainWindow", "-"))
        self.label_27.setText(_translate("MainWindow", "量比:"))
        self.label_0011.setText(_translate("MainWindow", "-"))
        self.label_11.setText(_translate("MainWindow", "均价:"))
        self.label_007.setText(_translate("MainWindow", "-"))
        self.label_13.setText(_translate("MainWindow", "内盘:"))
        self.label_0014.setText(_translate("MainWindow", "-"))
        self.label_16.setText(_translate("MainWindow", "最高:"))
        self.label_3.setText(_translate("MainWindow", "成交量:"))
        self.label_0013.setText(_translate("MainWindow", "-"))
        self.label_8.setText(_translate("MainWindow", "外盘:"))
        self.label_002.setText(_translate("MainWindow", "-"))
        self.label_18.setText(_translate("MainWindow", "换手:"))
        self.label_005.setText(_translate("MainWindow", "-"))
        self.label_0012.setText(_translate("MainWindow", "-"))
        self.label_006.setText(_translate("MainWindow", "-"))
        self.label_001.setText(_translate("MainWindow", "-"))
        self.label.setText(_translate("MainWindow", "昨收:"))
        self.label_4.setText(_translate("MainWindow", "成交额:"))
        self.label_003.setText(_translate("MainWindow", "-"))
        self.label_6.setText(_translate("MainWindow", "振幅:"))
        self.label_2.setText(_translate("MainWindow", "今开:"))
        self.label_29.setText(_translate("MainWindow", "股票公司代码："))
        self.name.setText(_translate("MainWindow", "股票名字"))
        self.label_5.setText(_translate("MainWindow", "-"))
        self.label_444.setText(_translate("MainWindow", "-"))
        self.label_555.setText(_translate("MainWindow", "-"))
        self.label_10.setText(_translate("MainWindow", "价格变化："))
        self.label_12.setText(_translate("MainWindow", "涨跌幅："))
        self.label_333.setText(_translate("MainWindow", "股票单价："))



import sys
import shares012
from PyQt5.QtWidgets import QApplication, QMainWindow
if __name__ =='__main__':

    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = shares012.Ui_secondWindow()
    ui.setupUi(MainWindow)
    try:
        Dialog33 = QtWidgets.QMainWindow()
        ui33 = Ui_Form1()
        ui33.setupUi1(Dialog33)
        bttn33 = ui.pushButton_3
        bttn33.clicked.connect(Dialog33.show)
    except Exception as err:
        print(err)
    MainWindow.show()


    sys.exit(app.exec_())
