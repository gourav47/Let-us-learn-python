'''create tuples with homogenous elements from a tuple containing heterogeneous elements'''
t=eval(input("Enter the tuple elements:"))
l=list(t)
for i in l:
    if type(i) is str:
        l.remove(i)
t=tuple(l)
print("Elements excluding string type is:",t)
