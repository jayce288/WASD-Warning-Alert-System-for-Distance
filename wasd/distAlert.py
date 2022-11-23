import winsound

D = 100
max_distance = 100

//거리별로 70,80,90%에 해당하는 구역에 도달할시 3단계을 알람을 단계별로 울리게 하였다.
def distAlert():
    if (D >= float(max_distance)*0.7 and D < float(max_distance)*0.8):
        winsound.Beep(500, 1200)
    elif (D >= float(max_distance)*0.8 and D < float(max_distance)*0.9):
        winsound.Beep(500, 700)
    elif (D >= float(max_distance)*0.9) and D < float(max_distance)):
        winsound.Beep(500, 500)
    
