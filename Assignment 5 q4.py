'''python script to print square of numbers from a to b'''
a=int(input("Enter the first number: "))
b=int(input("Enter second number: "))
if a>b:
    a,b=b,a
for i in range(a,b+1):
    print(i**2,end=' ')
