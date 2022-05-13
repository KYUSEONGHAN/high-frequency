# 2. Problem 2: Inductor equivalent circuit
# 1) 문제
# Inductor Model 1: An ideal inductor, L = 220nH
#  Z1: Impedance across terminals 1 and 2
# Inductor Model 2: A real inductor
# Rp=20kohm, Cp=0.059pF, Cs=4.7pF, Ls=16nH, Rs=1.95ohm
# Z2: Impedance across Port 1 and the ground with Port 2 connected to the ground
# Calculate the self-resonance frequency fr of Inductor Model 2.
# Calculate the impedances (Z1, Z2) of Inductor Model 1 and Inductor Model 2.
# Input:
# - Inductor Model 1: L given above
# - Inductor Model 2: Rp, Cp, Cs, Ls, Rs given above
# - Frequency range: start f1 Hz, end f2 Hz, n frequency points in log axis. f1 = 0.1 fr, f2 = 10 fr
# Output:
# Calculate Z1 and Z2 vs f and write the following.
# f(Hz), log10[f(Hz)], Z1, abs(Z1), Z2, abs(Z2)
# 결과분석
# - f = 0.1 fr에서 abs(Z1)과 abs(Z2) 비교
# - f = 10 fr에서 abs(Z1)과 abs(Z2) 비교
# 1. Problem 1: Inductor equivalent circuit
# 1) 문제
# Inductor Model 1: An ideal inductor, L = 220 nH
#  Z1: Impedance across terminals 1 and 2
# Inductor Model 2: A real inductor
# Z2: Impedance across terminals 1 and 2
# Calculate the self-resonance frequency fr of Inductor Model 2.
# Calculate the impedances (Z1, Z2) of Inductor Model 1 and Inductor Model 2.
# Input:
# - Inductor Model 1: L given above
# - Inductor Model 2: L2, L1, R, C given above
# - Frequency range: start f1 Hz, end f2 Hz, n frequency points in log axis. f1 = 0.1 fr, f2 = 10 fr
# Output:
# Calculate Z1 and Z2 vs f and write the following.
# f(Hz), log10[f(Hz)], Z1, abs(Z1), Z2, abs(Z2)
# 결과분석
# - f = 0.1 fr에서 abs(Z1)과 abs(Z2) 비교
# - f = 10 fr에서 abs(Z1)과 abs(Z2) 비교
# MW-10-Python-Example-1: Inductor equivalent circuit models
# Input:
# Inductor Model 1 (impedance z1): L
# Inductor Model 2 (impedance z2): C in parallel with (R in series with L)
# Output:
# fr: self-resonance frequency(Hz)
# f(Hz), log10[f(Hz)], z1, abs(z1), z2, abs(z2)
from math import *

def solve():
    n = int(input('Number of f in log10(f) axis: n='))

    if n == 0:
        return -1

    F2 = log10(f2)
    F1 = log10(f1)
    dF = (F2 - F1) / n

    for k in range(n + 1):
        F = F1 + k * dF
        f = 10 ** F
        w = 2 * pi * f

        z1 = j * w * Ls + Rs
        z2 = 1 / (j * w * Cs + (1 / j * w * Ls + Rs))

        print(f, F, z1, abs(z1), z2, abs(z2))


if __name__ == '__main__':
    L = float(input('Inductor Model 1: L = '))
    Rp, Cp, Cs, Ls, Rs = map(float, input('Inductor Model 2: Rp, Cp, Cs, Ls, RS)=').split())
    j = complex(0, 1)
    f1, f2 = map(float, input('f1,f2(Hz)=').split())  # f1 = 0.1fr, f2 = 10fr

    solve()