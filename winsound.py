import winsound

D = 100
max_distance = 100

def winsound():
    if (D >= float(max_distance)*0.7 and D < float(max_distance)*0.8):
        winsound.Beep(500, 1200)
    elif (D >= float(max_distance)*0.8 and D < float(max_distance)*0.9):
        winsound.Beep(500, 700)
    elif (D >= float(max_distance)*0.9):
        winsound.Beep(500, 500)

