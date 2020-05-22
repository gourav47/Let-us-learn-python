'''print N even natural numbers in reverse order'''
n=int(input("Enter a number: "))
for i in range(2*n,0,-2):
    print(i,end=' ')
