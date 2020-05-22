'''print all prime numbers between two numbers'''
l=int(input("Enter first number: "))
u=int(input("Enter second number: "))
if l>u:
    l,u=u,l
if l<1 and u>=2:
    l=2
if l<u<2:
    pass
else:
    for x in range(l+1,u):
        for i in range(2,x):
            if x%i==0:
                break
        else:
            print(x,end=' ')
