y=10   #Global Variable
print("outside functiony=",y)
def f1():
    y=5   #local variable
    print("Inside function local y=",y)
    print("Inside function Global y=",globals()['y'])

f1()
print("outside function y=",y)
