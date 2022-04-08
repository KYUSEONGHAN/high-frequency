import cmath

while True:
    rad = 3.141593 / 180
    s11m, s11p = map(float, input('Mag(S11), phase(S11)(deg)=').split())
    s12m, s12p = map(float, input('Mag(S12), phase(S12)(deg)=').split())
    s21m, s21p = map(float, input('Mag(S21), phase(S21)(deg)=').split())
    s22m, s22p = map(float, input('Mag(S22), phase(S22)(deg)=').split())

    s11, s12 = cmath.rect(s11m, s11p * rad), cmath.rect(s12m, s12p * rad)
    s21, s22 = cmath.rect(s21m, s21p * rad), cmath.rect(s22m, s22p * rad)

    a1m, a1p = map(float, input('Mag(A1), phase(A1)(deg)=').split())
    a2m, a2p = map(float, input('Mag(A2), phase(A2)(A2)=').split())

    a1, a2 = cmath.rect(a1m, a1p * rad), cmath.rect(a2m, a2p * rad)

    b1 = (s11 * a1) + (s12 * a2)
    p1i, p1r = (a1 * a1) / 2, (b1 * b1) / 2
    p1 = p1i - p1r

    print('b1 =', b1)
    print('pli =', p1i)
    print('plr =', p1r)
    print('p1 =', p1)
