'''python script to calculate the area of a circle, radius is taken from the user'''

r=float(input('Enter the radius of the circle:'))
area=(r**2)*3.142
print('area of the circle is: ',area)

'''another way to write the program using the module math'''

from math import pi
r=float(input('Enter the radius of the circle:'))
area=pi*r**2
print('area of a circle is: ', area)

'''another way to find the area of the circle'''

from math import *
r=float(input('Enter the radius of the circle:'))
print('The area of the circle with radius' +str(r) +' is: '+str(pi*r**2))
