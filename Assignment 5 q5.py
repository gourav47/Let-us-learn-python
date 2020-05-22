'''python script to print sequence of numbers with given step and boundary value'''
a=int(input("Enter Starting value"))
b=int(input("Enter end value"))
s=int(input("Enter step size"))
if a>b and s<0 or a<b and s>0:
    for i in range(a,b+1,s):
        print(i,end=' ')
else:
    print("Wrong Number")
