##Recursion in Lambda##

s=lambda a:1 if a==0 else a*s(a-1)
print("Factorial is",s(5))

#using normal function##

def fact():
    if(a==1):
        return 1
    else:
        return (a*fact(a-1))
    
r=fact(5)
print(r)
