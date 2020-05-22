'''python script to create a list of first N prime numbers.
Values of N is given by user.'''

n=int(input("Enter a natural number"))
x=2
l=[]
while n:
    if all (x%i!=0 for i in range(2,x)):
        l+=[x]   #to append the prime numbers in the list(compound assignment)
        n-=1
    x+=1
    '''all is a function which checks multiple
conditions, if all the conditions are true then all function will return true
otherwise false'''
