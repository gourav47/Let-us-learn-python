'''compare two tuples, whether they contain the same element in any order or not'''
t1=eval(input("Enter the first tuple: "))
t2=eval(input("Enter the second tuple: "))
if t1==t2:
    print("Tuples are same and are in same order")
else:
    print("t2 is in t1" if all(e in t1 for e in t2) else "t1 is in t2" if all(e in t2 for e in t1) else "Tuples are not same")
