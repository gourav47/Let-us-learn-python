#1st Priority
x=5
def function():
    x=10
    def inner():
        x=15  # local scope will be printed as per the scope priority
        print("x:",x)
    inner()
function()

#2nd priority
x=5
def function():
    x=10      # enclosed scope will be printed 2nd as per the scope priority
    def inner():
        #x=15  
        print("x:",x)
    inner()
function()

#3rd priority
x=5            #global scope will be printed 2nd as per the scope priority
def function():
    #x=10      
    def inner():
        #x=15  
        print("x:",x)
    inner()
function()
