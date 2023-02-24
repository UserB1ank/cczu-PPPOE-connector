import os
import uuid
import win32ras
from PyQt5.QtCore import QUuid


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
    f = open('PPPoEdata.dat', 'w')
    f.write(username)
    f.write('#')
    f.write(password)


def read():
    f = open('PPPoEdata.dat', 'r')
    length = f.readlines()
    data = []
    while length:
        data.append(f.readline())


def connect():
    password = '666888'
    username = fuck()
    # username = userdata[0]
    # password = userdata[1]

    ret = win32ras.Dial(
        None,
        None,
        ("net1", "", "", username, password, ""),
        None
    )
    print(ret)
    if ret[0] != 0 and ret[1] == 0:
        save(username, password)
        print('success')

    else:
        print('failed')

    # print(ret)


if __name__ == '__main__':
    connect()
