from urllib3 import ProxyManager, make_headers
import sys
import time

from PyQt5 import QtWidgets
from PyQt5.QtCore import QFile, QIODevice, Qt, QTextStream, QTimer, QUrl, QEvent, QObject
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
             #   self.showFullScreen()
                self.i = 0
                self.prox = 0
                self.a = 0
                self.setWindowTitle('Safari')
            #    QNetworkProxy.setApplicationProxy(QNetworkProxy(QNetworkProxy.HttpProxy, "173.192.21.89", 25))
             #   QNetworkProxy.setApplicationProxy(QNetworkProxy(QNetworkProxy.HttpProxy, "88.159.123.151", 80))
            #    QNetworkProxy.setApplicationProxy(QNetworkProxy(QNetworkProxy.HttpProxy, "138.197.137.90", 3128))
              #  QNetworkProxy.setApplicationProxy(QNetworkProxy(QNetworkProxy.HttpProxy, "94.177.175.232", 3128))
               # self.load(QUrl('https://www.youtube.com/watch?v=-oV8nNeLpjY&list=PLmahvFaEUuOmzu6t8rZ4SUz3ECAC2jQf5'))
               # self.load(QUrl('https://youtu.be/-KqdN1uScHc'))
                #self.load(QUrl('https://vk.com/video447929742_456239017'))
                self.load(QUrl('https://www.youtube.com'))
                self.show()
                self.loadFinished.connect(self.prow)
        def prow(self):
            if self.a == 0:
                self.a = 1
                self.fin()

        def fin(self):
            print('Вход в цикл программы')
            self.i = 0
            while self.i<500:
                time.sleep(0.1)
                QtWidgets.qApp.processEvents()
                self.i = self.i + 1


            if self.prox == 0:
                QNetworkProxy.setApplicationProxy(QNetworkProxy(QNetworkProxy.HttpProxy, "138.197.137.90", 3128))
            elif self.prox == 1:
                QNetworkProxy.setApplicationProxy(QNetworkProxy(QNetworkProxy.HttpProxy, "35.185.80.76", 3128))
            elif self.prox == 2:
                QNetworkProxy.setApplicationProxy(QNetworkProxy(QNetworkProxy.HttpProxy, "212.237.15.178", 80))
            elif self.prox == 3:
                QNetworkProxy.setApplicationProxy(QNetworkProxy(QNetworkProxy.HttpProxy, "104.236.27.71", 80))
            elif self.prox == 4:
                QNetworkProxy.setApplicationProxy(QNetworkProxy(QNetworkProxy.HttpProxy, "144.217.100.67", 80))
            elif self.prox == 5:
                QNetworkProxy.setApplicationProxy(QNetworkProxy(QNetworkProxy.HttpProxy, "94.177.175.232", 80))
            elif self.prox == 6:
                QNetworkProxy.setApplicationProxy(QNetworkProxy(QNetworkProxy.HttpProxy, "149.56.42.236", 80))
            elif self.prox == 7:
                QNetworkProxy.setApplicationProxy(QNetworkProxy(QNetworkProxy.HttpProxy, "35.185.80.76", 3128))
            elif self.prox == 8:
                QNetworkProxy.setApplicationProxy(QNetworkProxy(QNetworkProxy.HttpProxy, "162.243.140.150", 8000))
            elif self.prox == 9:
                QNetworkProxy.setApplicationProxy(QNetworkProxy(QNetworkProxy.HttpProxy, "177.67.84.157", 8080))
            elif self.prox == 10:
                QNetworkProxy.setApplicationProxy(QNetworkProxy(QNetworkProxy.HttpProxy, "192.208.184.134", 8080))
            elif self.prox == 11:
                QNetworkProxy.setApplicationProxy(QNetworkProxy(QNetworkProxy.HttpProxy, "151.80.152.121", 8080))
            elif self.prox == 12:
                QNetworkProxy.setApplicationProxy(QNetworkProxy(QNetworkProxy.HttpProxy, "212.237.15.178", 8080))
            else:
                self.prox = -1
            print('Использованное proxi -', self.prox)
            print('Загрузка сайта')
            self.a = 0
            self.load(QUrl('https://youtu.be/-KqdN1uScHc'))
            self.prox = self.prox + 1
            print('Загрузился типо')

                #       def mouseReleaseEvent(self, e):
 #           print("xlixk")

                
        def finished(self):
                self.fin = self.fin + 1
                print("Load Finish")
                self.loading()

        def loading(self):
            QtWidgets.qApp.processEvents()
            if (self.fin > 0):
                self.fin = 0
                self.newsite()


        def newsite(self):
            while not self.request():
                QtWidgets.qApp.processEvents()
                print('Proxy bad')
            QtWidgets.qApp.processEvents()
            QNetworkProxy.setApplicationProxy(QNetworkProxy(QNetworkProxy.HttpProxy, self.proxi_ip, self.proxi_port))
            self.load(QUrl('https://vk.com/id447929742?z=video447929742_456239017%2F2819f4855e1e422801%2Fpl_wall_447929742'))
            return True


        def request(self):
            QtWidgets.qApp.processEvents()
            self.proxi()
            print(self.stroka2)
            self.prm = ProxyManager(str(self.stroka2))
            print(self.stroka2)
            try:
                QtWidgets.qApp.processEvents()
                r = self.prm.request('GET', 'https://www.yandex.ru/')
            except:
                return False
            return True

        def proxi(self):
            self.stroka = self.f.readline()
            self.stroka2 = 'http://' + self.stroka
            self.stroka2 = self.stroka2[:len(self.stroka2)-1]
            print(self.stroka)
            QtWidgets.qApp.processEvents()
            self.massiv = self.stroka.split(':')
            self.proxi_ip = str(self.massiv[0])
            self.proxi_port = int((self.massiv[1])[:len(self.massiv[1]) - 1])
            QtWidgets.qApp.processEvents()
            print(self.proxi_ip)
            print(self.proxi_port)

if __name__ == '__main__':
        app = QApplication(sys.argv)

        browser = MainWindow()

        sys.exit(app.exec_())

