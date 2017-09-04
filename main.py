
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
                self.i = 0
                self.initUI()


        def initUI(self):

                self.setGeometry(100, 100, 1050, 550)
                self.setWindowTitle('Safari')
                self.load(QUrl('https://2ip.ru'))
                self.loadFinished.connect(self.newsite)
                self.show()



        def newsite(self):
            self.s = self.f.readline()
            self.a = self.s.split(':')
            self.str1 = str(self.a[0])
            self.int1 = int(str(self.a[1])[:(len(str(self.a[1])) - 1)])
            print(self.str1)
            print(self.int1)
            QNetworkProxy.setApplicationProxy(0                                )
            QNetworkProxy.setApplicationProxy(QNetworkProxy(QNetworkProxy.HttpProxy, "93.91.112.185", 80 ))

   #         QNetworkProxy.setApplicationProxy(QNetworkProxy(QNetworkProxy.HttpProxy, self.s[:(len(self.s)-1)], self.q[:(len(self.q) - 1)]))
            self.load(QUrl('https://youtu.be/5-a_fzNAB3A'))








 #       def finishLoading(self):

                #self.view.load(QUrl('https://google.com'))



if __name__ == '__main__':

        import sys

        app = QApplication(sys.argv)



        #print(s[0])

        #QNetworkProxy.setApplicationProxy(QNetworkProxy(QNetworkProxy.HttpProxy, "14.141.93.162", 8080))

        #browser.load(QUrl('https://html5test.com'))
        browser = MainWindow()
   #     browser.load(QUrl('https://2ip.ru'))


        sys.exit(app.exec_())

