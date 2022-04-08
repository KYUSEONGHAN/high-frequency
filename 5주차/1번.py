from cmath import *

while True:
    rad = 3.141593 / 180
    Ism, Isp = map(float, input('Is(Irms): mag(Is), phase(Is)(deg)=').split())
    ys = complex(input('Ys(ohm)(complex)='))
    yL = complex(input('YL(ohm)(complex)='))

    zL, zs, Is = 1 / yL, 1 / ys, rect(Ism, Isp)
    vs = Is * ys
    i = vs / (zs + zL)
    v = i * zL
    ipol, vpol = polar(i), polar(v)
    pL, pg, ps = v * i.conjugate(), (zs * i) * i.conjugate(), vs * i.conjugate()

    print('RMS load current I:  I_mag(A), I_phase(deg)=', ipol[0], ipol[1] / rad)
    print('RMS load voltage V: V_mag(V), I_phase(deg)=', vpol[0], vpol[1] / rad)
    print('Average power dissipaged in YL: PL(W)=', pL.real)
    print('Average power dissipated in Ys: Pg(W)=', pg.real)
    print('Average power supplied by Is: Ps(W)=', ps.real)