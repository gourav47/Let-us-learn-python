'''python script to find greatest among three numbers'''
x=int(input('Enter the first number: '))
y=int(input('Enter the Second number: '))
z=int(input('Enter the third number: '))
if x>y and x>z:
    print('%d is largest'%x)
elif y>x and y>z:
    print('%d is largest'%y)
else:
    print('%d is largest'%z)
