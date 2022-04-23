# 1. Resistor equivalent circuit
# Port 2 (RT2) is short-circuited (i.e., connected to the ground).
# Z: impedance between RT1 and the ground.
# Frequency is swept from 1MHz to 10GHz.
# Find the frequency where |Im(Z) | > 10 Ω.
from cmath import *

def solve(L1: float, L2: float, L3: float, R: float, C1: float, C2: float, C3: float) -> bool:
    f1, f2 = map(float, input().split())
    n = int(input())

    F1, F2 = log10(f2), log10(f1)
    dF = (F2 - F1) / n

    for i in range(n + 1):
        F = F1 + i * dF
        f = 10 ** F
        w = 2 * pi * f
        Z1 = j * w * L3
        Z2 = 1 / (j * w * C1 + 1 / (j * w * L1 + R))
        Z3 = 1 / ((1 / j * w * L2) + j * w * C2)
        Zs = Z2 + Z3
        Zb = 1 / ((1 / Zs) + (j * w * C3))
        Z = Zb + Z1

        if abs(Z.imag) > 10:
            print(f, F, Z, abs(Z))

    return False

if __name__ == '__main__':
    j = complex(0, 1)
    L1, L2, L3, R, C1, C2, C3 = map(float, input().split())

    solve(L1, L2, L3, R, C1, C2, C3)
    """
    l1 = 1.5e-9
    l2 = 2e-9
    l3 = 2.5e-9
    r = 100
    c1 = 3e-12 
    c2 = 4e-12
    c3 = 5e-12
    """