'''Write a python script to find greatest number in the list of integers given
by user'''
#input list
l=[int(e) for e in input("Enter numbers seperated by comma: ").split(',')]

#finding maximum value in the list
m=max(l)

#Display result
print("Greatest number in the list is",m)
