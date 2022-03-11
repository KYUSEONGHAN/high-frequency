# MW-01-Python-Ex4: RLC series and parallel circuits
pi = 3.141593

while True:
 R = float(input('R(ohm)='))
 L = float(input('L(uH)='))
 C = float(input('C(uF)='))
 f = float(input('f(Hz)='))

 w = 2 * pi * f
 Zs = complex(R, w*L*1e-6-1 / (w*C*1e-6))      # 직렬회로 임피던스
 Zp = 1/complex(1/R, w*C*1e-6-1 / (w*L*1e-6))  # 병렬회로 임피던스

 print('Z(series)=', Zs)
 print('Z(parallel)=', Zp)

 """ output
 R(ohm)=100
 L(uH)=20
 C(uF)=50
 f(Hz)=1e6
 Z(series)= (100+125.66053690148915j)
 Z(parallel)= (1.0132629437904996e-07-0.0031831791384774404j)
 R(ohm)=
 """
