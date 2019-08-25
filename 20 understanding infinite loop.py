'''program to understand infinite loop'''
x=5
while x>0:
    print("Hello")
    x=x-1

'''The above program doesnot have infinite loop and will run smooth'''
'''as we can see that x=x-1 is inside the while loop'''
'''so whenever the condition is checked 'x' operation is also getting executed,
however if we keep the "x=x-1" outside the while loop then the operation will
never be executed and the code will stuck in infinite loop as in that case
while x>0 is always true because x is initialised at value 5 and it is less
than 0, hence the value will always be true for while condition and it will be
infinite loop'''
'''lets see that byu doing'''
x=5
while x>0:
    print("Hello")
x=x-1
