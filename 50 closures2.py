def outer():
    x=3
    def inner():
        y=3
        result=x+y
        return result
    return inner()
a=outer()
print(a)

#2nd example

def outer():
    msg="hello"
    def inner():
        print(msg)
    return inner
a=outer()
a()
