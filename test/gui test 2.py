import sys
import io
import serial
import math
import winsound
import folium

from PyQt5 import QtWidgets, QtWebEngineWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QLabel, QPushButton, QLineEdit, QDialog, \
    QTableWidgetItem
from PyQt5.QtGui import QPixmap
from PyQt5.uic.properties import QtGui

text = float(0)
class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label1 = QLabel("W A S D", self)
        label1.move(1030, 200)
        label2 = QLabel("WARNING ALERT SYSTEM for DISTANCE", self)
        label2.move(1030, 340)
        label3 = QLabel("Insert the Max Distance of your Aircraft", self)
        label3.move(1030, 1010)

        font1 = label1.font()
        font1.setPointSize(50)
        font2 = label2.font()
        font2.setPointSize(20)
        font3 = label2.font()
        font3.setPointSize(10)

        label1.setFont(font1)
        label2.setFont(font3)
        label3.setFont(font3)

        pixmap1 = QPixmap('airplane.png')
        pixmap2 = QPixmap('wasd2.png')

        lbl_img1 = QLabel(self)
        pixmap1 = pixmap1.scaledToWidth(500)
        lbl_img1.setPixmap(pixmap1)
        lbl_img1.move(1030, 400)

        lbl_img2 = QLabel(self)
        lbl_img2.setPixmap(pixmap2)
        lbl_img2.move(2100, 100)

        self.lbl = QLabel(self)
        self.lbl.move(60, 40)

        self.qle = QLineEdit(self)
        self.qle.move(1150, 1050)

        btn1 = QPushButton('START', self)
        btn1.move(1100, 1100)
        btn1.setStyleSheet('color:white; background:black')
        btn1.resize(350, 150)
        btn1.setFont(font2)
        btn1.clicked.connect(self.button_second)

        self.setWindowTitle('WASD')
        self.resize(2500, 1400)
        self.center()
        self.show()

    def button_second(self):
        self.hide()
        self.second = secondwindow()
        self.second.exec()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

class secondwindow(QDialog,QWidget):
    def __init__(self):
        super(secondwindow, self).__init__()
        self.initUI()

    def initUI(self):

        label1 = QLabel("Green Limit:", self)
        label1.move(1610,600)
        label2 = QLabel("Yellow Limit:", self)
        label2.move(1590, 700)
        label3 = QLabel("Red Limit:", self)
        label3.move(1670, 800)
        label4 = QLabel("700m", self)
        label4.move(2000, 600)
        label5 = QLabel("800m", self)
        label5.move(2000, 700)
        label6 = QLabel("900m", self)
        label6.move(2000, 800)
        label7 = QLabel("DISTANCE:", self)
        label7.move(1400, 1050)
        label8 = QLabel("0.000000m", self)
        label8.move(1900, 1050)
        label9 = QLabel("Altitude:", self)
        label9.move(1600, 400)
        label10 = QLabel("0.000000m", self)
        label10.move(1860, 400)

        font1 = label1.font()
        font2 = label1.font()
        font1.setPointSize(25)
        font1.setFamily('Times New Roman')
        font2.setPointSize(35)
        font2.setFamily('Times New Roman')
        label1.setFont(font1)
        label2.setFont(font1)
        label3.setFont(font1)
        label4.setFont(font1)
        label5.setFont(font1)
        label6.setFont(font1)
        label7.setFont(font2)
        label8.setFont(font2)
        label9.setFont(font1)
        label10.setFont(font1)

        pixmap2 = QPixmap('wasd2.png')
        lbl_img2 = QLabel(self)
        lbl_img2.setPixmap(pixmap2)
        lbl_img2.move(2100, 100)

        pixmap2 = QPixmap('map.png')
        lbl_img2 = QLabel(self)
        lbl_img2.setPixmap(pixmap2)
        lbl_img2.move(50, 50)

        self.setWindowTitle('WASD')
        self.resize(2500, 1400)
        self.show()

if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())
