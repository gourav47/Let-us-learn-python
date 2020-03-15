def print_str():
    return "goog morning"
print(print_str())

'''Now suppose we want the message in upper case, then we need to decorate it'''
def str_upper(func):  
    def inner():
        str1=func()
        return str1.upper()
    return inner

def print_str():
    return "goog morning"
print(print_str())

d=str_upper(print_str)
print(d())

'''Ways to use decorator for the above program'''
def str_upper(func):  
    def inner():
        str1=func()
        return str1.upper()
    return inner

@str_upper
def print_str():
    return "goog morning"
print(print_str())

'''with parameters'''
def div_decorator(func):
    def inner(x,y):
        if y==0:
            return "give proper input"
        return func(x,y)
    return inner
@div_decorator
def div(a,b):
    return a/b
print(div(4,0))

