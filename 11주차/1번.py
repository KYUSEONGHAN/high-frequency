# 1. Problem 1: Lossy torroidal inductor
# 1) 문제
# A torroidal inductor
# S, d : torroid cross sectional area(m^2) and torroid mean ring length(m)
#  μr, tanδ : inductor material relativity permittivity and loss tangent
# I, f : inductor current (A) and frequency(Hz)
# Calculate
# L, R : inductance(H) and series resistance(ohm) of the inductor
# PR, PC : loss power(W) and stored power(W) in the inductor
# MW-11-Python-Ex1: Lossy parallel-plate circular disk capacitor
# Input:
# a,d: disk radius and disk separation(m)
# er,tand: capacitor material dielectric constant and loss tangent
# v,f: applied voltage(V) and frequency(Hz)
# Output:
# C,R: capacitance(F) and parallel resistance(ohm) of the capacitor
# pc,pr: loss power(W) and stored power(W) in the capacitor
from math import *

e0 = 8.854e-12

def solve():
    s, d = map(float, input().split())
    ur, er, tand = map(float, input('Capacitor material: ur, er,tand=').split())
    v, f = map(float, input('Applied voltage and frequency: V(V),f(Hz)=').split())

    w = 2 * pi * f
    R = d / (w * e0 * er * tand * s)
    C = e0 * er * s / d
    L = ur * (s / d)
    pr = 0.5 * v ** 2 / R
    pc = 0.5 * w * C * v ** 2

    print('L(H), R(ohm)={0:14.4e}{1:14.4e}'.format(L, R))
    print('Pr(W), Pc(W)={1:14.4e}{0:14.4e}'.format(pr, pc))

if __name__ == '__main__':
    solve()