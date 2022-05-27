from math import *

def solve():
    a, b, c, x, y, n, k = map(float, input('input a, b, c, x, y, n, k= ').split())
    E = float(input('input E='))
    j = complex(0, 1)
    er, ur = 1, 1
    z = 0
    Hx = (1 / n) * k * E
    Hy = (3 / n) * (z*j + x) * e * (-j * k * y)
    Hz = y * E / (n*c) * e*(-(a*z)) * e*(-j*b*z)

    print('Hx=', Hx)
    print('Hy=', Hy)
    print('Hz=', Hz)

if __name__ == '__main__':
    solve()