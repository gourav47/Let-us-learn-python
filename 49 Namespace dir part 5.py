y=10
def inner():
    x=4
    global y
    y=y+1
    print("x:",x)
    print("inside the function y:",y)
print("y:",y)
inner()

#if the same code is written but print("y:",y) is given after inner function is called then the outputwill differ as:

y=10
def inner():
    x=4
    global y
    y=y+1
    print("x:",x)
    print("inside the function y:",y)
inner()
print("y:",y)
