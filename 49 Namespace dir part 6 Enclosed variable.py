y=10
def outer():
    z=4     #non-local variable, it has scope both inside and outer function but is not global,hence named as enclose variable
    def inner():
        x=4
        print("x:",x)
        print("inside the function z:",z)
    inner()
    print("z:",z)
outer()

#similar to global keyword we can modify the value of enclosed variable by using nonlocal

y=10
def outer():
    z=4     #non-local variable, it has scope both inside and outer function but is not global,hence named as enclose variable
    def inner():
        x=4
        nonlocal z
        z=z+1
        print("x:",x)
        print("inside the function z:",z)
    inner()
    print("z:",z)
outer()

