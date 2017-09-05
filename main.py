from urllib3 import ProxyManager, make_headers

import time
from PyQt5.QtCore import QFile, QIODevice, Qt, QTextStream, QUrl
from PyQt5.QtWidgets import (QAction, QApplication, QLineEdit, QMainWindow,
        QSizePolicy, QStyle, QTextEdit)
from PyQt5.QtNetwork import QNetworkProxyFactory, QNetworkRequest,QNetworkProxy
from PyQt5.QtWebKitWidgets import QWebPage, QWebView


class MainWindow(QWebView):
        def __init__(self):
                super().__init__()
                self.f = open('proxi.txt', 'r')
                self.initUI()

        def initUI(self):
                self.setGeometry(100, 100, 1050, 550)
                self.setWindowTitle('Safari')
                self.load(QUrl('https://2ip.ru'))
                self.loadFinished.connect(self.newsite)
                self.show()

        def newsite(self):
            if(self.request()):
                QNetworkProxy.setApplicationProxy(QNetworkProxy(QNetworkProxy.HttpProxy, self.proxi_ip, self.proxi_port))
            else:
                self.request()
          #self.load(QUrl('https://youtu.be/5-a_fzNAB3A'))
            self.load(QUrl('https://2ip.ru'))

        def request(self):
            self.proxi()
            print(self.stroka2)
            self.prm = ProxyManager(str(self.stroka2))
            print(self.stroka2)
            try:
                r = self.prm.request('GET', 'https://www.yandex.ru/')
            except:
                return False
            return True

        def proxi(self):
            self.stroka = self.f.readline()
            self.stroka2 = 'http://' + self.stroka
            self.stroka2 = self.stroka2[:len(self.stroka2)-1]
            print(self.stroka)
            self.massiv = self.stroka.split(':')
            self.proxi_ip = str(self.massiv[0])
            self.proxi_port = int((self.massiv[1])[:len(self.massiv[1]) - 1])
            print(self.proxi_ip)
            print(self.proxi_port)

if __name__ == '__main__':

        import sys

        app = QApplication(sys.argv)
  #      QNetworkProxy.setApplicationProxy(QNetworkProxy(QNetworkProxy.HttpProxy, "5.135.195.166", 3128))
        #print(s[0])
        #QNetworkProxy.setApplicationProxy(QNetworkProxy(QNetworkProxy.HttpProxy, "14.141.93.162", 8080))
        #browser.load(QUrl('https://html5test.com'))
        browser = MainWindow()
   #     browser.load(QUrl('https://2ip.ru'))
        sys.exit(app.exec_())

