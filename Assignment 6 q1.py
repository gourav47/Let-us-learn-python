'''Write a python script to sort a list given by user'''


l=[int (e) for e in input("Enter numbers seperated by comma: ").split(',')]
'''input function will return the string value and split function will
sepearate the single string into several small strings on the basis of
comma'''
'''also we need to transfer the string into int, hence we will be using int
'''
print(l)
sorted(l)
print(l)
'''sorted function returns sorted list but there will be no changes in the list'''

l=[int (e) for e in input("Enter numbers seperated by comma: ").split(',')]
print(l)
m=sorted(l)
print(m)

l=[int (e) for e in input("Enter numbers seperated by comma: ").split(',')]
print(l)
l.sort()
print(l)

'''Sorted function can be applied for any sequence whereas sort is used for
list purpose only'''
