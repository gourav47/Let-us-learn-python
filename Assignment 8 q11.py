'''check whether a tuple is a subset of another tuple or not'''
t1=eval(input("Enter the first tuple: "))
t2=eval(input("Enter the second tuple: "))
print("t2 is a subset of t1" if all(e in t1 for e in t2) else "t1 is subset of t2" if all(e in t2 for e in t1) else "none of the tuple is the subset of anyother tuple")
