def upper_d(func):
    def inner():
        return "first "+func()+" first"
    return inner

def split_d(func):
    def wrapper():
        return "second "+func()+" second"
    return wrapper

@upper_d
@split_d
def ordinary():
    return "good morning"

print(ordinary())
