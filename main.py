import sys
import config

import win32ras
from PyQt5.QtCore import QUuid
from PyQt5.QtWidgets import (QApplication, QLabel, QVBoxLayout, QPushButton, QLineEdit, QWidget, QDesktopWidget,
                             QHBoxLayout)


def UserInput():
    phone = input()
    password = input()
    return phone, password


def fuck():
    phone = '17826311903'
    # userdata = UserInput()
    # phone = userdata[0]
    # password = userdata[1]
    uid = QUuid.createUuid().toString().replace('-', '').replace('{', '').replace('}', '')
    check = 0
    for i in range(3):
        check = check + ord(phone[i]) + ord(uid[i])
    str_check = (check * 177 + 5166) % 10000
    account = uid + str(str_check) + "01" + phone
    # print(account)
    return account


def save(username, password):
    try:
        f = open('PPPoEdata.dat', 'w')
        f.write(username)
        f.write('#')
        f.write(password)
        return True
    except IOError:
        return IOError


def read():
    try:
        f = open('PPPoEdata.dat', 'r')
        data = f.readline()
        data = data.split("#")
        username = data[0]
        password = data[1]
        return username, password
    except IOError:
        return IOError


def connect():
    password = '666888'
    username = fuck()
    # username = userdata[0]
    # password = userdata[1]

    # ret = win32ras.Dial(
    #     None,
    #     None,
    #     ("net1", "", "", username, password, ""),
    #     None
    # )
    RASFILE = config.rascfg
    win32ras.SetEntryDialParams(RASFILE, ("pyras", "", "", username, password, ""), True)
    session = win32ras.Dial(None, RASFILE, ("pyras", "", "", username, password, ""), None)

    # print(ret)
    # if ret[0] != 0 and ret[1] == 0:
    #     save(username, password)
    #     print('success')
    #     return True
    # else:
    #     print('failed')
    #     return False


class Client(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        # 设置窗口标题
        self.setWindowTitle('宽带连接助手(作者:UserB1ank)')

        # 设置窗口大小位置
        self.setMaximumSize(350, 300)
        self.setMinimumSize(350, 300)

        # 创建垂直布局
        vbox = QVBoxLayout(self)
        # 窗口居中
        self.center()
        # 创建用户名输入框
        hbox1 = QHBoxLayout()
        self.label_un = QLabel('用户名', self)
        self.un_edit = QLineEdit()
        hbox1.addWidget(self.label_un)
        hbox1.addWidget(self.un_edit)
        hbox1.setContentsMargins(70, 0, 70, 0)
        vbox.addLayout(hbox1)

        # 创建密码输入框
        hbox2 = QHBoxLayout()
        self.label_pwd = QLabel('密码', self)
        self.pwd_edit = QLineEdit()
        self.pwd_edit.setEchoMode(QLineEdit.Password)
        hbox2.addWidget(self.label_pwd)
        hbox2.addWidget(self.pwd_edit)
        hbox2.setContentsMargins(70, 0, 70, 0)
        hbox2.setSpacing(20)
        vbox.addLayout(hbox2)

        # 创建按钮组件
        hbox3 = QHBoxLayout()
        self.BTNConnect = QPushButton('连接', self)
        self.BTNDisConnect = QPushButton('断开连接', self)
        self.BTNDisConnect.hide()
        hbox3.addWidget(self.BTNConnect)
        hbox3.addWidget(self.BTNDisConnect)
        hbox3.setContentsMargins(100, 0, 100, 0)
        vbox.addLayout(hbox3)

        self.setLayout(vbox)

    def center(self):
        # 获取屏幕信息
        screen = QDesktopWidget().screenGeometry()
        # 计算屏幕中心点
        x = (screen.width() - self.width()) / 2
        y = (screen.height() - self.height()) / 2
        # 移动位置
        self.move(int(x), int(y))


if __name__ == '__main__':
    connect()
    # app = QApplication(sys.argv)
    # widget = Client()
    # widget.show()
    # sys.exit(app.exec())
