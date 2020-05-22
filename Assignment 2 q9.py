'''python script to accept one complex number from the user and display the
greater number between real and imaginary part.'''


c=complex(input('Enter a complex number'))
if c.real>c.imag:
    print('%d is greater'%(c.real))
elif c.real<c.imag:
    print('%d is greater'%(c.imag))
else:
    print('Both are equal')
    
    
