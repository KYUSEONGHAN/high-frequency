from math import *

def solve():
    fR = 1 / (2 * pi * sqrt(LS * (CP)))
    f1, f2 = 0.1 * fR, 10 * fR
    n = int(input('Number of f in log10(f) axis: n='))

    if n == 0:
        return -1

    F1, F2 = log10(f1), log10(f2)
    dF = (F2 - F1) / n
    print('f(Hz), log10(f), z1, abs(z1), z2, abs(z2)')

    for k in range(n + 1):
        F = F1 + k * dF
        f = 10 ** F
        w = 2 * pi * f
        z1 = 1 / (j * w * C)
        z2 = 1 / ((1 / (j * w * C + (1 / RD))) + (1 / j * w * LS) + (1 / RS) + (2 * j * w * CP))

        print(f, F, z1, abs(z1), z2, abs(z2))

if __name__ == '__main__':
    C, RD, RS, LS, CP = map(float, input('Capacitor Model 2: C(F),RD(ohm),RS(ohm),LS(H),CP(F)=').split())
    j = complex(0, 1)

    solve()