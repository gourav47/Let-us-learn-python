'''count distinct elements in a list using set'''
print("Enter comma seperated list elements:")
l=[int(e) for e in input().split(',')]
s=set(l)
print("Total distinct elements in the list",l, "are: ",len(s),"and those elements are",s)
