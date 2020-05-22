'''python script to check whether the number is divisible by 5 or not'''
#using modulas operator

x=int(input('Enter a possitive integer number: '))
if (x%5==0):
    print('%d is divisible by 5'%x)
else:
    print('%d is not divisible by 5'%x)

#without using modulas operator

x=int(input('Enter a possitive integer number: '))
y=int(x/5)*5
if(x==y):
    print('%d is divisible by 5'%x)
else:
    print('%d is not divisible by 5'%x)
