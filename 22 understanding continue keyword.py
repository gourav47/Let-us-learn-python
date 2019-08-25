'''Program to understand the continue keyword'''
x=1
while x<=24:
    if x%5==0:
        x=x+1 #if we dont put this then it will print only till 4
        continue
    print(x, end=' ')
    x=x+1

#what if we use break insted of continue

x=1
while x<=24:
    if x%5==0:
        break
    print(x, end=' ')
    x=x+1

'''if we use continue then the control goes back to the while condition loop,
whereas in break it goes out of the loop'''
