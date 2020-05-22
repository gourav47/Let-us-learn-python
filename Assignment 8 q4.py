'''reverse a tuple'''
t=eval(input("Enter the tuple values to be reversed: "))
l=list(t)
l.reverse()
t=tuple(l)
print("Reverse of tuple is:",t)
