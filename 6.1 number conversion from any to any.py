'''any number to any number system conversion'''

x=45
print(bin(x)) #bin function to convert decimnal to binary.

y=0o334
print(bin(y)) #bin function to convert octal to binary.

z=0x21c
print(bin(z)) #bin function to convert hexadecimal to binary.

w=0x21c
print(oct(w)) #oct function to convert hexadecimal to octal.

v=0b1000011100
print(oct(v)) #oct function to convert binary to octal.

u=540
print(hex(u)) #hex function to convert decimal to hexadecimal.

t=0b1000011100
print(hex(t)) #hex function to convert binary to hexadecimal.

s=0o1034
print(hex(s)) #hex function to convert octal to hexadecimal.

'''python by default print any numnber in decimal format, hence we dont need to
use function to convert into decimal'''

'''now suppose if we want to  print the exact octal or hexa format then we need to do slicing
using the indexing concept'''

r=oct(s)
print(r[2::])

