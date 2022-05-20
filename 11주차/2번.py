# 2. Problem 2: Poynting's theorem
# 1) 문제
# A planewave:
#  εr, tanδe : medium's dielectric constant and dielectric loss tangent
#  μr, tanδm : medium's relative permittivity and magnetic loss tangent
#  f : frequency(Hz)
#  E : electric field strength(V/m)
# Calculate:
#  Pr : radiated power (planewave power) per unit area(W/m^2)
#  PL : loss power per unit volume(W/m^3)
#  Wm : stored magnetic energy per volume(J/m^3)
#  We : stored electric energy per volume(J/m^3)

# MW-11-Python-Ex2: Planewave
# Input:
# er, ur: medium's dielectric constant and relative permittivity
# f: frequency(Hz)
# E: electric field strength(V/m)
# Output:
# k: propagation constant(/m)
# L: wavelenth(m)
# eta: intrinsic impedance(ohm)
# H: magnetic field(A/m)
# P: planewave power density(W/m^2)
from math import *

e0 = 8.854e-12
u0 = 4 * pi * 1e-7

# from math import *

# e0=8.854e-12; u0=4*pi*1e-7

# while True:
#  er,ur=map(float,input('Medium dielectric constant and relative permittivity: er,ur=').split())
#  f=float(input('Frequency: f(Hz)='))
#  E=float(input('Electric field strength: E(V/m)='))
#  w=2*pi*f;
#  e=e0*er;
#  u=u0*ur
#  k=w*sqrt(u*e);
#  L=2*pi/k;
#  eta=sqrt(u/e);
#  H=E/eta;
#  P=0.5*E*H
#  print('Propagation constant: k(/m)=',k)
#  print('Wavelength: lambda(m)=',L)
#  print('Intrinsic impedance: eta(ohm)=',eta)
#  print('Magnetic field strength: H(A/m)=',H)
#  print('Planewave power density: P(W/m^2)=',P)

def solve():
    er, tane = map(float, input().split())
    ur, tanm = map(float, input().split())
    f = float(input())
    E = float(input())
    j = float(input())

    w = 2 * pi * f
    e = e0 * er
    u = u0 * ur
    k = w * sqrt(u * e)
    L = w * pi / k
    eta = sqrt(u/e)
    H = E / eta
    P = 0.5 * E * H

    pr = 0.5 * E * H
    pl = 0.5 * j * E
    wm = 0.25 * ur * H * H
    we = 0.25 * er * E * E

    print('Pr=', pr)
    print('Pl=', pl)
    print('Wm=', wm)
    print('We=', we)

if __name__ == '__main__':
    solve()