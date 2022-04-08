from cmath import *

while True:
    z0 = float(input('transmission line characteristic impedance Z0 (ohm)='))
    z = float(input('series impedance Z(ohm)='))

    s11, s12 = z / (2 * z0 + z), (z0 + z) / (2 * z0 + z)
    s21, s22 = s12, s11

    s11P, s12P = polar(s11), polar(s12)
    s21P, s22P = polar(s21), polar(s22)

    print('Mag(s11), Phase(s11)=', s11P[0], s11P[1])
    print('Mag(s12), Phase(s12)=', s12P[0], s12P[1])
    print('Mag(s21), Phase(s21)=', s21P[0], s21P[1])
    print('Mag(s22), Phase(s22)=', s22P[0], s22P[1])