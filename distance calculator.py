import math

l1 = 35.15408
lo1 = 128.09300
al1 = 61.20000

l2 = 35.1524
lo2 = 128.1029
al2 = 1.0

def dis():
    a = abs(lo1 - lo2)
    b = abs(l1 - l2)
    c = abs(al1 - al2)
    X = (math.cos(l1) * 6400 * 2 * math.pi / 360) * abs(a)
    Y = 111 * abs(b)
    C = X * X + Y * Y
    D = math.sqrt(C) * 1000
    E = D * D + c * c
    F = math.sqrt(E)

    return F

print(dis())
