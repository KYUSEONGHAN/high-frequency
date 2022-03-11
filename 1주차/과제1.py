# MW-01-Python-Ex1
# Transmission Line: Z0, gamma from R, L, G, C, f
# Sample values: RG-59 coaxial cable
# Input: R=36e-3 ohm/m, L=430e-9 H/m, G=10e-6 S/m, C=69e-12 F/m, f=100e6 Hz
# Output:
# Z0=(78.94228228730861+0.0038450155279376556j)
# gamma=(0.0006227261020735598+3.4224620530010226j)
import cmath

pi = 3.14159265

while True:
 R = float(input('R(ohm/m)='))
 L = float(input('L(H/m)='))
 G = float(input('G(S/m)='))
 C = float(input('C(F/m)='))

 while True:
    f = float(input('f(Hz)=(negative to stop)'))
    if f < 0:
        break

 Z = complex(R, 2*pi*f*L); Y = complex(G,2*pi*f*C)
 Z0 = cmath.sqrt(Z/Y); gamma = cmath.sqrt(Z*Y)

 print('Z0(ohm)=', Z0)
 print('gamma(per meter)=', gamma)