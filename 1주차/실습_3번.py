# MW-01-Python-Ex3: Complex calulation
from cmath import *  # Use the complex math library in Python

while True:
 z1 = complex(input('z1='))
 z2 = complex(input('z2='))

 z3 = z1 * z2
 z4 = z1 / z2
 zp3 = polar(z3)
 zp4 = polar(z4)
 z3arg = zp3[1] * 180 / 3.14159
 z4arg = zp4[1] * 180 / 3.14159

 print('z3=', z3, 'z3(polar)=', zp3, 'arg(z3)(deg)=', z3arg)
 print('z4=', z4, 'z4(polar)=', zp4, 'arg(z4)(deg)=', z4arg)

 """ output
 z1=1+2j
 z2=3+4j
 z3= (-5+10j) z3(polar)= (11.180339887498949, 2.0344439357957027) arg(z3)(deg)= 116.56514963544781
 z4= (0.44+0.08j) z4(polar)= (0.4472135954999579, 0.17985349979247828) arg(z4)(deg)= 10.304855172904833
 z1=
 """