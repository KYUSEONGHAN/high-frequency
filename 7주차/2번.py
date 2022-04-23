# 2. Resistor impedance analysis using a pi-network model
# f : frequency between 1GHz and 5GHz
# 1) Calculate S-parameters. (S11, S12, S22)
# 2) From S-parameters, find Z3(=1/Y3), Y1, and Y2.
# 3) From Z3, Y1, and Y2, find C1, L, R, and C2.
from cmath import *

def solve(C1: float, C2: float, L: float, R: float, z0: float, j: complex, f: float):
    y0 = 1 / z0
    w = 2 * pi * f
    y1 = j * w * C1
    y2 = j * w * C2
    y3 = 1 / ((j * w * L) + R)
    y1i = y1 + y3 * (y2 + y0) / (y3 + y2 + y0)
    y2i = y2 + y3 * (y1 + y0) / (y3 + y1 + y0)
    s11 = (y0 - y1i) / (y0 + y1i)
    s22 = (y0 - y2i) / (y0 + y2i)
    s12 = (1 + s22) * y3 / (y3 + y1 + y0)
    S11 = polar(s11)
    S12 = polar(s12)
    S22 = polar(s22)

    d = (1 + s11) * (1 + s22) - s12 * s12
    y11 = y0 * ((1 - s11) * (1 + s22) + s12 * s12) / d
    y12 = -2 * y0 * s12 / d
    y22 = y0 * ((1 + s11) * (1 - s22) + s12 * s12) / d
    y1 = y11 + y12
    y2 = y22 + y12
    y3 = -y12
    z3 = 1 / y3
    CC1 = y1 / (j * w)
    CC2 = y2 / (j * w)
    LL = (z3 - R) / (j * w)
    RR = z3 - j * w * LL

    print('mag(S11),phase(S11)(deg)=', S11[0], S11[1] * 180 / pi)
    print('mag(S12),phase(S12)(deg)=', S12[0], S12[1] * 180 / pi)
    print('mag(S22),phase(S22)(deg)=', S22[0], S22[1] * 180 / pi)
    print('Y1,Y2,Z3=', y1, y2, z3)
    print('C1(F),C2(F),L(H),R(ohm)=', CC1, CC2, LL, RR)


if __name__ == '__main__':
    C1, C2, L, R = map(float, input().split())
    z0 = float(input())
    j = complex(0, 1)
    f = float(input())

    solve(C1, C2, L, R, z0, j, f)
    """
    c1 = 463e-12
    c2 = 1852e-12
    l = 5e-6
    r = 100
    z0 = 50
    f = 3.7e6 
    """