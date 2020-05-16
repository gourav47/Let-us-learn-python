x=int(input("Enter first number"))
y=int(input("Enter second number"))
if y==0:
    raise ZeroDivisionError("Denominator cannot be zero")
z=x/y
print("Division is:",z)

x=int(input("Enter first number"))
y=int(input("Enter second number"))
try:
    if y==0:
        raise ZeroDivisionError("Denominator cannot be zero")
    z=x/y
    print("Division is:",z)
except ZeroDivisionError:
    print("you cannot divide by zero")
