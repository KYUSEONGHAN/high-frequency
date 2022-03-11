# EM-01-Python-Ex2: R, L, G, C from Z0, γ and f
# Input: Z0 = 79+3.8e-3j, gamma=6.2e-4+3.4j, f=100e6
# Output:
import cmath

pi = 3.14159265

while True:
 Z0 = complex(input('Z0(ohm)='))
 gamma = complex(input('gamma(per meter)='))
 f = float(input('f(Hz)='))
 w = 2 * pi * f
 temp = gamma * Z0
 R = temp.real
 L = temp.imag / w
 temp = gamma / Z0
 G = temp.real
 C = temp.imag/w

 print('R(ohm/m)=', R)
 print('L(H/m)=', L)
 print('G(S/m)=', G)
 print('C(F/m)=', C)



""" output
Z0(ohm)=79+3.8e-3j
gamma(per meter)=6.2e-4+3.4j
f(Hz)=100e6
R(ohm/m)= 0.03606
L(H/m)= 4.27490181383e-07
G(S/m)= 9.918282303601987e-06
C(F/m)= 6.849706343446908e-11
Z0(ohm)=
"""