def function1():
    print("I am function1")

def function2(func):
    print("I am function 2 now i will call function1")
    func()

function2(function1)
