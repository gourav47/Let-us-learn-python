print("initially:",dir())			#this will print the built in variable
num=20
def f1():
    n=10
    print("inside the function:",dir())	##this will print only n variable name as it is inside a function
f1()
print("Outside the function:",dir())	#this will print the builtins and function name
