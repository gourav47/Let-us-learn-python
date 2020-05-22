'''python script to check nature of roots of a given quadratic equation'''

from math import *
from fractions import Fraction
print ('quadratic equation:(a*x^2)+b*x+c')
a=Fraction(input('a: '))
b=Fraction(input('b: '))
c=Fraction(input('c: '))
d=(b**2-4*a*c)
if d>0:
    Number_roots = 2
    x1=((-b+sqrt(d))/(2*a))
    x2=((-b-sqrt(d))/(2*a))
    print('Nature of roots: Real and Distinct,Roots: %f and %f'%(x1,x2))
elif d==0:
          Number_roots =1
          x=(-b)/(2*a)
          print('Nature of roots: Real and Equal,Roots: %f'%x)
else:
          Number_Roots = 0
          print('No Roots')
          
