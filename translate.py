# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'translate.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
import requests, random
from hashlib import md5


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(836, 557)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setStyleSheet("#widget{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(245, 224, 176, 255), stop:0.09 rgba(246, 189, 237, 255), stop:0.14 rgba(194, 207, 246, 255), stop:0.19 rgba(184, 160, 168, 255), stop:0.25 rgba(171, 186, 248, 255), stop:0.32 rgba(243, 248, 224, 255), stop:0.385 rgba(249, 162, 183, 255), stop:0.47 rgba(100, 115, 124, 255), stop:0.58 rgba(251, 205, 202, 255), stop:0.65 rgba(170, 128, 185, 255), stop:0.75 rgba(252, 222, 204, 255), stop:0.805 rgba(206, 122, 218, 255), stop:0.86 rgba(254, 223, 175, 255), stop:0.91 rgba(254, 236, 244, 255), stop:1 rgba(255, 191, 221, 255));}")
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(40, 40, 40, 20)
        self.gridLayout.setHorizontalSpacing(50)
        self.gridLayout.setVerticalSpacing(7)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setMinimumSize(QtCore.QSize(80, 0))
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 2, 1, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 2, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.textEdit = QtWidgets.QTextEdit(self.widget)
        self.textEdit.setWhatsThis("")
        self.textEdit.setStyleSheet("font: 14pt \"Arial\";")
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 1, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_2.setSizeIncrement(QtCore.QSize(0, 0))
        self.pushButton_2.setStyleSheet("border-image: url(:/icons/icons/运行.png);")
        self.pushButton_2.setText("")
        self.pushButton_2.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 1, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.textEdit_2 = QtWidgets.QTextEdit(self.widget)
        self.textEdit_2.setWhatsThis("")
        self.textEdit_2.setStyleSheet("font: 14pt \"Arial\";")
        self.textEdit_2.setPlaceholderText("")
        self.textEdit_2.setObjectName("textEdit_2")
        self.gridLayout.addWidget(self.textEdit_2, 1, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        self.label.setBaseSize(QtCore.QSize(0, 0))
        self.label.setStyleSheet("font: 22pt \"Arial\";")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 836, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menuyunxing = QtWidgets.QMenu(self.menubar)
        self.menuyunxing.setSeparatorsCollapsible(False)
        self.menuyunxing.setToolTipsVisible(False)
        self.menuyunxing.setObjectName("menuyunxing")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionxinjian = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/问价.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionxinjian.setIcon(icon)
        self.actionxinjian.setObjectName("actionxinjian")
        self.actiondakai = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/打开文件.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actiondakai.setIcon(icon1)
        self.actiondakai.setObjectName("actiondakai")
        self.actiontuichu = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/退出.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actiontuichu.setIcon(icon2)
        self.actiontuichu.setObjectName("actiontuichu")
        self.actionbaocun = QtWidgets.QAction(MainWindow)
        self.actionbaocun.setEnabled(True)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/存储.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionbaocun.setIcon(icon3)
        self.actionbaocun.setObjectName("actionbaocun")
        self.actionlcw = QtWidgets.QAction(MainWindow)
        self.actionlcw.setObjectName("actionlcw")
        self.actionfanyi = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/icons/运行.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionfanyi.setIcon(icon4)
        self.actionfanyi.setObjectName("actionfanyi")
        self.actionwenjian = QtWidgets.QAction(MainWindow)
        self.actionwenjian.setObjectName("actionwenjian")
        self.menu.addAction(self.actionxinjian)
        self.menu.addAction(self.actiondakai)
        self.menu.addSeparator()
        self.menu.addAction(self.actionbaocun)
        self.menu.addAction(self.actionlcw)
        self.menu.addSeparator()
        self.menu.addAction(self.actiontuichu)
        self.menuyunxing.addAction(self.actionfanyi)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menuyunxing.menuAction())
        self.toolBar.addAction(self.actionxinjian)
        self.toolBar.addAction(self.actiondakai)
        self.toolBar.addAction(self.actionbaocun)
        self.toolBar.addAction(self.actiontuichu)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionfanyi)

        self.retranslateUi(MainWindow)
        self.actiontuichu.triggered.connect(MainWindow.close)
        self.pushButton.clicked.connect(self.textEdit.clear)
        self.pushButton.clicked.connect(self.textEdit_2.clear)
        self.pushButton_3.pressed.connect(self.textEdit_2.selectAll)
        self.pushButton_3.released.connect(self.textEdit_2.copy)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.textEdit, self.textEdit_2)
        MainWindow.setTabOrder(self.textEdit_2, self.pushButton_2)
        MainWindow.setTabOrder(self.pushButton_2, self.pushButton)
        MainWindow.setTabOrder(self.pushButton, self.pushButton_4)
        MainWindow.setTabOrder(self.pushButton_4, self.pushButton_3)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "清空"))
        self.pushButton_4.setText(_translate("MainWindow", "交换"))
        self.pushButton_3.setText(_translate("MainWindow", "复制"))
        self.textEdit.setToolTip(_translate("MainWindow", "<html><head/><body><p></p></body></html>"))
        self.textEdit.setPlaceholderText(_translate("MainWindow", "请输入要翻译的内容："))
        self.textEdit_2.setToolTip(_translate("MainWindow", "<html><head/><body><p></p></body></html>"))
        self.label.setText(_translate("MainWindow", "英汉互译"))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.menuyunxing.setTitle(_translate("MainWindow", "运行"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionxinjian.setText(_translate("MainWindow", "新建(&N)"))
        self.actionxinjian.setToolTip(_translate("MainWindow", "新建"))
        self.actionxinjian.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actiondakai.setText(_translate("MainWindow", "打开(&O)"))
        self.actiondakai.setToolTip(_translate("MainWindow", "打开"))
        self.actiondakai.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actiontuichu.setText(_translate("MainWindow", "退出(&Q)"))
        self.actiontuichu.setToolTip(_translate("MainWindow", "退出"))
        self.actionbaocun.setText(_translate("MainWindow", "保存(&S)"))
        self.actionbaocun.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionlcw.setText(_translate("MainWindow", "另存为(&A)"))
        self.actionfanyi.setText(_translate("MainWindow", "翻译(&F)"))
        self.actionwenjian.setText(_translate("MainWindow", "wenjian"))


import resources_rc


class main(QtWidgets.QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_4.clicked.connect(self.exchange)
        self.ui.pushButton_2.clicked.connect(self.baidu_transAPI)
        self.ui.actionfanyi.triggered.connect(self.baidu_transAPI)
        self.show()

    # 拖动
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton and self.isMaximized() == False:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, mouse_event):
        if QtCore.Qt.LeftButton and self.m_flag:
            self.move(mouse_event.globalPos() - self.m_Position)  # 更改窗口位置
            mouse_event.accept()

    def mouseReleaseEvent(self, mouse_event):
        self.m_flag = False
        self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))

    def exchange(self):
        tmp = self.ui.textEdit_2.toPlainText()
        self.ui.textEdit_2.setText(self.ui.textEdit.toPlainText())
        self.ui.textEdit.setText(tmp)

    def baidu_transAPI(self):
        # Set your own appid/appkey.
        appid = ''  # 这里百度写申请的appid
        appkey = ''  # 这里百度写申请的appkey

        # For list of language codes, please refer to `https://api.fanyi.baidu.com/doc/21`
        from_lang = 'auto'
        to_lang = 'auto'

        endpoint = 'http://api.fanyi.baidu.com'
        path = '/api/trans/vip/translate'
        url = endpoint + path

        query = self.ui.textEdit.toPlainText()

        # Generate salt and sign
        def make_md5(s, encoding='utf-8'):
            return md5(s.encode(encoding)).hexdigest()

        salt = random.randint(32768, 65536)
        sign = make_md5(appid + query + str(salt) + appkey)

        # Build request
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        payload = {'appid': appid, 'q': query, 'from': from_lang, 'to': to_lang, 'salt': salt, 'sign': sign}

        # Send request
        r = requests.post(url, params=payload, headers=headers)
        result = r.json()
        trans_text = []
        for i in range(len(result['trans_result'])):
            trans_text.append(result['trans_result'][i]['dst'] + '\n')
        self.ui.textEdit_2.setText(''.join(trans_text))
