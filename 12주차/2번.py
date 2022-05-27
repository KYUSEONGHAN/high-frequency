from math import *

def solve():
    w, t = map(float, input('input w, t = ').split())
    x, y = map(float, input('input x, y= ').split())

    Ex = cos(w * t * e*x)
    Ey = cos(w * t + e*y)

    Ex *= abs(Ex)
    Ey *= abs(Ey)

    E = sqrt(Ex ** 2 + Ey ** 2)

    print('min(E)=', E * -1)
    print('max(E)=', E)
    print('axial ratio (AR)=', gamma(E))
    print('gamma (ellipse angle, angle between major axis with + x axis)=', Ex)

if __name__ == '__main__':
    solve()