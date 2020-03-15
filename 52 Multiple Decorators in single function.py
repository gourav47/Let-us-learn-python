def upper_d(func):
    def inner():
        str1=func()
        return str1.upper()
    return inner

def split_d(func):
    def wrapper():
        str2=func()
        return str2.split()
    return wrapper

@split_d
@upper_d
def ordinary():
    return "good morning"

print(ordinary())
