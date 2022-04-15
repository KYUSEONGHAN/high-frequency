# 2. Resistor impedance analysis using a pi-network model
# f : frequency between 1GHz and 5GHz
# 1) Calculate S-parameters. (S11, S12, S22)
# 2) From S-parameters, find Z3(=1/Y3), Y1, and Y2.
# 3) From Z3, Y1, and Y2, find C1, L, R, and C2.
import math, cmath

# 전역변수 선언
rad = math.pi / 180

def solve():
    r, x = rr / z0, xx / z0

    if r <= 1:
        cs, Lp = C, L
        f = 0.8 * f0 - 0.02 * f0

        print('Cs=', cs)
        print('Lp=', Lp)

        for _ in range(n):
            f = f + 0.02 * f0
            w = 2 * math.pi * f
            z = complex(rr, xx) + complex(0, -1 / (w * cs))
            y = 1 / z + complex(0, -1 / (w * Lp))
            z = 1 / y
            gamma = (z - z0) / (z + z0)

            print('f(Hz)=', f, ', mag(S11)(dB)=', 20 * math.log1p(abs(gamma)), 'phase(S11)(deg)=', cmath.phase(gamma) / rad)


if __name__ == '__main__':
    z0 = float(input('Z0 (ohm) (real) = '))
    L, C, rr, xx = map(float, input('L,C,R,L2 = ').split())
    f0 = float(input('f0 (Hz) = '))
    n = int(input('S11 Calculation Times'))

    solve()