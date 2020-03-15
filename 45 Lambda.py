s=lambda a,b:a+b
r=s(10,20)
print("sum is",r)

####second way####

r=(lambda a,b:a+b)(10,20)
print("sum is",r)

##Maximum of two numbers##
t=(lambda a,b:max(a,b))(10,20)
print("greater number is",t)

##Other way####
print("Enter two numbers")
r=(lambda a,b:a if a>b else b)(int(input()),int(input()))
print("Greater number is",r)
