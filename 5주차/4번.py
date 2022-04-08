from cmath import *

while True:
    rad = 3.141593 / 180
    z0 = float(input('System reference impedance: Z0(ohm)(real)='))
    zs = complex(input('Source impedance: ZS(ohm)(complex)='))
    s11m, s11p = map(float, input('Mag(S11), phase(S11)(deg)=').split())
    s12m, s12p = map(float, input('Mag(S12), phase(S12)(deg)=').split())
    s21m, s21p = map(float, input('Mag(S21), phase(S21)(deg)=').split())
    s22m, s22p = map(float, input('Mag(S22), phase(S22)(deg)=').split())

    s11, s12 = rect(s11m, s11p*rad), rect(s12m, s12p*rad)
    s21, s22 = rect(s21m, s21p*rad), rect(s22m, s22p*rad)

    RCS = (zs-z0) / (zs+z0)
    RCi = s22 + s12 * s21 * RCS / (1 - s11 * RCS)
    Rpol = polar(RCi)

    print('Output reflection coefficient: mag(Gamma_i), phase(Gamma_i)(deg)=', Rpol[0], Rpol[1]/rad)
    zo = (1 + RCi) / (1 - RCi) * z0
    print('Output impedance: ZO(ohm)=', zo)
    zo_opt = zo.conjugate()
    print('Optimum source impedance: Zs_opt(ohm)=', zo_opt)