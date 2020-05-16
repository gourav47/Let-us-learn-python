x=int(input("Enter first number:"))
y=int(input("Enter second number"))
try:
    z=x/y
    print("Division result:",z)
except ZeroDivisionError:
    print("Invalid attempt of division")

print("Helllo this is last line")


s=int(input("Enter first number:"))
t=int(input("Enter second number")
try:
    z=s/t
    print("Division result:",z)
except TypeError:
    print("Invalid attempt of division")
finally:
    print("In Finally")
print("Helllo this is last line")

s=int(input("Enter first number:"))
t=int(input("Enter second number"))
try:
    z=s/t
    print("Division result:",z)
except (TypeError,ValueError, ZeroDivisionError):
    print("Invalid attempt of division")
except:
    print("Default Exception")
finally:
    print("In Finally")
print("Helllo this is last line")
