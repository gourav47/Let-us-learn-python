'''Write a python script to check whether the given number is even or odd'''

#using modulas operator:

x=int(input('Enter an integer value greater than zero:'))
if (x%2==0):
      print('%d is an even number'%x)
else:
      print('%d is an odd number'%x)

#using bitwise operator:

x=int(input('Enter an integer value greater than zero:'))
if (x&1==1):
      print('%d is an odd number'%x)
else:
      print('%d is an even number'%x)

#Check Even / Odd without using modulus or bitwise operator:

x=int(input('Enter an integer value greater than zero:'))
y=int(x/2)*2
if(x==y):
    print('%d is even'%x)
else:
    print('%d is odd'%x)
