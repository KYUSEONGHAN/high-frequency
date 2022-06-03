from math import pi, sqrt, sin, asin, cos

ur1, er1 = map(float, input('ur1,er1=').split())
ur2, er2 = map(float, input('ur2,er2=').split())

for i in range(0, 93, 3):
    thetai = float(i) * pi / 180
    thetar = thetai
    n1, n2 = sqrt(ur1 * er1), sqrt(ur2 * er2)
    temp = n1 / n2 * sin(thetai)

    if temp <= 1.0:
        thetat = asin(temp)
    else:
        thetat = pi / 2

eta1, eta2 = sqrt(ur1 / er1), sqrt(ur2 / er2)
r = (eta2 * cos(thetat) - eta1 * cos(thetai)) / (eta2 * cos(thetat) + eta1 * cos(thetai))
t = 1 + r

print('Theta_i, Theta_r, Theta_t, R, T={0:6.1f}{1:6.1f}{2:6.1f}{3:8.3f}{4:8.3f}'. format(thetai * 180 / pi, thetar * 180 / pi, thetat * 180 / pi, r, t))