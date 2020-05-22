'''print first n prime numbers'''
n=int(input("Enter a natural number: "))
x=2
while n:
    for i in range(2,x):
        if x%i==0:
            break
    else:
        print(x,end=" ")
        n=n-1
    x=x+1
