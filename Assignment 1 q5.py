'''program to calculate the square of a number'''

#normal method

n=float(input('Enter the number:'))
s=(n*n)
print("The square of the number is: ",s)

#using exponent

n=float(input('Enter the number: '))
s=n**2 
print('Square of the number is: ',s)

#using pow of math module

from math import *
n=float(input('Enter the number: '))
s=pow(n,2)
print('Square of the number is: ',s)

        
