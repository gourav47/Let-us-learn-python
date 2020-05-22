'''print N odd natural numbers in reverse order'''
n=int(input("Enter a number: "))
for i in range(2*n-1,1,-2):
    print(i,end=' ')

'''Another way of coding'''
n=int(input("Enter a number: "))
for i in range(1,n+1):
    print(2*n-2*i+1,end=' ')
