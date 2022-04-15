# 1. Resistor equivalent circuit
# Port 2 (RT2) is short-circuited (i.e., connected to the ground).
# Z: impedance between RT1 and the ground.
# Frequency is swept from 1MHz to 10GHz.
# Find the frequency where |Im(Z) | > 10 Ω.
from cmath import *

# 전역변수 선언
j = complex(0, 1)

def solve(f0, z1, zL, z0, LQ):
    fb = float(input('fb='))
    n = int(input('N='))

    df = f0 * fb / n

    for x in range(n + 1):
        f = f0 * (1 - fb / 2) + x * df
        wL = 3e8 / f
        beta = 2 * pi / wL
        zi = z1 * (zL + j * z1 * tan(beta * LQ)) / (z1 + j * zL * tan(beta * LQ))
        s11 = (zi - z0) / (zi + z0)
        s11m = 20 * log10(abs(s11))
        s11p = phase(s11) * 180 / pi

        print(f, s11m, s11p)


if __name__ == '__main__':
    zL, z0 = map(complex, input('ZL,Z0(ohm)=').split())
    z2 = (z0 + zL) / 2
    f0, fb = map(float, input('f0,fb(Hz)=').split())
    z1, LQ = sqrt(z0 * z2), 3e8 / 4 * f0

    print('Z1(ohm), LQ(m)=', z1, LQ)

    solve(f0, z1, zL, z0, LQ)