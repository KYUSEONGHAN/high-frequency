# MW-01-Python-Ex4: RLC series and parallel circuits
pi = 3.141593

while True:
 R = float(input('R(ohm)='))
 L = float(input('L(uH)='))
 C = float(input('C(uF)='))

 f = float(input('f(Hz)='))
 w = 2 * pi * f
 Zs = complex(R, w*L*1e-6-1 / (w*C*1e-6))
 Zp = 1/complex(1/R, w*C*1e-6-1 / (w*L*1e-6))

 print('Z(series)=', Zs)
 print('Z(parallel)=', Zp)
