import serial
arduino = serial.Serial('COM4',9600)

while(True):
    if(arduino.readable()):
        a = arduino.readline()
        res = a.decode('utf-8')
        print(res)
        gps = res.split(" ")

        print("Latitude : "+ gps[0] + " Longitude :"+gps[1]+" Altitude :"+gps[2]+"\n")
