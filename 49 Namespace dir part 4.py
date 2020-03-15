y=10            #global variable, can be accessed both inside and outside the function.
def inner():    #this is a global function, this can be called anywhere in code
    x=4         #this is local variable
    y=y+1
    print("x value inside the function",x)
    print("y value Inside the function",y)
print("y:",y)   #this will print the global variable value
inner()
