import serial
import math
import winsound
import time
arduino = serial.Serial('COM4',9600,timeout = 0.1)

l1 = 35.15408
lo1 = 128.09300
al1 = 61.20000

range = 10.0

while(True):
    if(arduino.readable()):
        a = arduino.readline()
        res = a.decode('utf-8')

        print(res)
        gps = res.split(" ")

        print("Latitude : "+ gps[0] + " Longitude :"+gps[1]+" Altitude :"+gps[2]+"\n")
        l2 = float(gps[0])
        lo2 = float(gps[1])

        a = lo1-lo2
        b = l1-l2
        X = (math.cos(l1)*6400*2*math.pi/360)*abs(a)
        Y = 111*abs(b)
        c = X*X + Y*Y
        D = math.sqrt(c)*1000

        print(D)

        if(D>=range):
            winsound.Beep(500, 1000)
