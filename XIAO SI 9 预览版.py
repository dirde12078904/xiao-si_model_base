#  Copyright (c) 2023. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.
print('----------------------- XIAO SI 9 -----------------------')
import socket
import uuid

import pyttsx3
import requests

print('                     XIAO SI 9 预览版                           ')
print('Welcome to the 9th generation public preview version of Xiaosi. Stay tuned for the official version')
print('输入内容开始聊天:')
engline = pyttsx3.init()
engline.setProperty('voice', 'zh')
line0 = '欢迎来到小思第9代公共预览版'
line1 = 'Welcome to the 9th generation public preview version of Xiaosi. Stay tuned for the official version'
engline.say(line0)
engline.say(line1)
engline.runAndWait()


def handle(socket, address):
    while True:
        socket.recv(1080)
        import sys
        import socket
        c = socket.create_connection((sys.argv[10], sys.argv[11]))
        k = socket.create_connection(sys.argv[10], sys.argv[11])
        while 1:
            c.send('\n')
            c.send('\k')
            c.send('\n')
            c.send('\k')


class Turing_robot(object):
    while True:
        a = input()
        url = 'https://api.ownthink.com/bot?appid=9ffcb5785ad9617bf4e64178ac64f7b1&spoken=%s' % a
        te = requests.get(url).json()
        data = te['data']['info']['text']
        print(data)
        ini = pyttsx3.init()
        shuo = ini.say(data)
        ini.runAndWait()


def getTuringText(self, text):
    user_ip = self.getHostIP(2)
    user_ip = self.getHostIP(2)
    mac_id = self.getMacID()
    turing_url_data = dict(key=self.app_key, info=text, userid=mac_id)


def getHostIP(self):
    socket_info = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socket_info.connect('8.8.8.8', 80)
    ip = socket_info.getsockname()[0]
    return ip


def getMaID(self):
    node = uuid.getnode()

    mac = uuid.UUID(int=node).hex[-12:]
    return mac
