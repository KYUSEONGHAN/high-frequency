# 1. Example 1: Inductut equivalent circuit
# 1) 문제
# Inductor Model 1: An ideal inductor, L = 3.6 μH
#  Z1: Impedance across terminals 1 and 2
# Inductor Model 2: A real inductor
#  C = 0.7 pF, R = 2 ohm, L = 3.6 uH,
#  Z2: Impedance across terminals 1 and 2
# Calculate the self-resonance frequency fr of Inductor Model 2.
# Calculate the impedances (Z1, Z2) of Inductor Model 1 and Inductor Model 2.
# Input:
# - Inductor Model 1: L given above
# - Inductor Model 2: R, C, L given above
# - Frequency range: start f1 Hz, end f2 Hz, n frequency points in log axis. f1 = 0.1 fr, f2 = 10 fr
# Output:
# Calculate Z1 and Z2 vs f and write the following.
# f(Hz), log10[f(Hz)], Z1, abs(Z1), Z2, abs(Z2)
# 결과분석
# - f = 0.1 fr에서 abs(Z1)과 abs(Z2) 비교
# - f = 10 fr에서 abs(Z1)과 abs(Z2) 비교
from math import *

C, R, L = map(float, input('Inductor Model 2: C(F),R(ohm),L(H)=').split())
j = complex(0, 1)
f1, f2 = map(float, input('f1,f2(Hz)=').split())

while True:
    n = int(input('Number of f in log10(f) axis: n='))

    if n == 0:
        break

    F2 = log10(f2)
    F1 = log10(f1)
    dF = (F2 - F1) / n

    for k in range(n + 1):
        F = F1 + k * dF
        f = 10 ** F
        w = 2 * pi * f
        z1 = j * w * L
        z2 = 1 / (j * w * C + 1 / (R + j * w * L))
        print(f, F, z1, abs(z1), z2, abs(z2))