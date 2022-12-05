import sys
import serial
import math
import winsound
import time

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
        pixmap2 = QPixmap('wasd.png')

        lbl_img1 = QLabel(self)
        pixmap1 = pixmap1.scaledToWidth(500)
        lbl_img1.setPixmap(pixmap1)
        lbl_img1.move(1030, 400)

        lbl_img2 = QLabel(self)
        lbl_img2.setPixmap(pixmap2)
        lbl_img2.move(2100, 0)

        self.lbl = QLabel(self)
        self.lbl.move(60, 40)

        self.qle = QLineEdit(self)
        self.qle.move(1150, 1050)

        btn1 = QPushButton('INPUT', self)
        btn1.move(1100, 1100)
        btn1.setStyleSheet('color:white; background:black')
        btn1.resize(350, 150)
        btn1.setFont(font2)
        btn1.clicked.connect(self.button_second)

        self.setWindowTitle('WASD')
        self.resize(2500, 1400)
        self.show()

    def button_second(self):
        text = self.qle.text()
        self.hide()
        self.second = secondwindow(text)
        self.second.exec()
        self.show()

class secondwindow(QDialog,QWidget):
    def __init__(self, text):
        super(secondwindow, self).__init__()
        self.initUI(text)

    def initUI(self, text):

        self.max_distance = int(text)

        label1 = QLabel("Green Limit:", self)
        label1.move(160, 750)
        label2 = QLabel("Yellow Limit:", self)
        label2.move(940, 750)
        label3 = QLabel("Red Limit:", self)
        label3.move(1770, 750)
        self.label4 = QLabel(str(self.max_distance*0.7) + "m", self)
        self.label4.move(550, 750)
        self.label5 = QLabel(str(self.max_distance*0.8) + "m", self)
        self.label5.move(1350, 750)
        self.label6 = QLabel(str(self.max_distance*0.9) + "m", self)
        self.label6.move(2100, 750)
        label7 = QLabel("Latitude:", self)
        label7.move(250, 300)
        self.label8 = QLabel("0.000000", self)
        self.label8.move(600, 300)
        label9 = QLabel("Longitude:", self)
        label9.move(200, 400)
        self.label10 = QLabel("0.000000", self)
        self.label10.move(600, 400)
        label11 = QLabel("Altitude:", self)
        label11.move(250, 500)
        self.label12 = QLabel("0.000000", self)
        self.label12.move(600, 500)
        label13 = QLabel("Latitude:", self)
        label13.move(1500, 300)
        self.label14 = QLabel("0.000000", self)
        self.label14.move(1950, 300)
        label15 = QLabel("Longitude:", self)
        label15.move(1450, 400)
        self.label16 = QLabel("0.000000", self)
        self.label16.move(1950, 400)
        label17 = QLabel("Altitude:", self)
        label17.move(1500, 500)
        self.label18 = QLabel("0.000000", self)
        self.label18.move(1950, 500)
        label19 = QLabel("DISTANCE:", self)
        label19.move(800, 900)
        self.label20 = QLabel("0.000000m", self)
        self.label20.move(1300, 900)
        label21 = QLabel("USER", self)
        label21.move(450,180)
        label22 = QLabel("VEHICLE", self)
        label22.move(1650, 180)


        font1 = label1.font()
        font2 = label1.font()
        font3 = label21.font()
        font1.setPointSize(25)
        font2.setPointSize(35)
        font3.setPointSize(40)
        font3.setFamily('Calibri Bold')
        font3.setBold(True)
        label1.setFont(font1)
        label2.setFont(font1)
        label3.setFont(font1)
        self.label4.setFont(font1)
        self.label5.setFont(font1)
        self.label6.setFont(font1)
        label7.setFont(font1)
        self.label8.setFont(font1)
        label9.setFont(font1)
        self.label10.setFont(font1)
        label11.setFont(font1)
        self.label12.setFont(font1)
        label13.setFont(font1)
        self.label14.setFont(font1)
        label15.setFont(font1)
        self.label16.setFont(font1)
        label17.setFont(font1)
        self.label18.setFont(font1)
        label19.setFont(font2)
        self.label20.setFont(font2)
        label21.setFont(font3)
        label22.setFont(font3)

        pixmap2 = QPixmap('wasd.png')
        lbl_img2 = QLabel(self)
        lbl_img2.setPixmap(pixmap2)
        lbl_img2.move(2100, 0)

        self.btn2 = QPushButton('START', self)
        self.btn2.move(1050, 1100)
        self.btn2.setStyleSheet('color:white; background:black')
        self.btn2.resize(350, 150)
        self.btn2.setFont(font2)
        self.btn2.clicked.connect(self.GPS)

        self.setWindowTitle('WASD')
        self.resize(2500, 1400)
        self.show()

    def GPS(self):
        arduino = serial.Serial('COM4', 9600)

        l1 = 35.15415
        lo1 = 128.0929
        al1 = 61.20000

        self.btn2.setText("STOP")

        self.label8.setText(str(l1))
        self.label8.repaint()
        self.label10.setText(str(lo1))
        self.label10.repaint()
        self.label12.setText(str(al1))
        self.label12.repaint()

        while (True):
            if (arduino.readable()):
                a = arduino.readline()
                res = a.decode('utf-8')

                print(res)
                gps = res.split(" ")

                print("Latitude : " + gps[0] + " Longitude :" + gps[1] + " Altitude :" + gps[2] + "\n")
                l2 = float(gps[0])
                lo2 = float(gps[1])
                al2 = float(61.20000)

                self.label14.setText(str(l2))
                self.label14.repaint()
                self.label16.setText(str(lo2))
                self.label16.repaint()
                self.label18.setText(str(al2))
                self.label18.repaint()

                a = abs(lo1 - lo2)
                b = abs(l1 - l2)
                c = abs(al1 - al2)
                X = (math.cos(l1) * 6400 * 2 * math.pi / 360) * a
                Y = 111 * b
                C = X * X + Y * Y
                D = math.sqrt(C) * 1000
                E = D * D + c * c
                F = math.sqrt(E)
                G = f'{F:.3f}'

                self.label20.setText(str(G) + 'm')
                self.label20.repaint()

                if (F >= float(self.max_distance) * 0.7 and F < float(self.max_distance) * 0.8):
                    winsound.Beep(500, 1200)
                elif (F >= float(self.max_distance) * 0.8 and F < float(self.max_distance) * 0.9):
                    winsound.Beep(500, 700)
                elif (F >= float(self.max_distance) * 0.9 and F < float(self.max_distance)):
                    winsound.Beep(500, 500)
                elif(F > float(self.max_distance)):
                    winsound.Beep(1000, 2000)


                time.sleep(0.1)

if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())
