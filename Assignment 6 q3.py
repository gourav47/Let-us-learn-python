'''Write a python script to calculate sum of all the integers of the list
given by user.'''

list=[int(e) for e in input("Enter numbers seperated by comma: ").split(',')]
'''print("Enter a list of integers seperated by comma: ")
list=[int(x) for x in input().split(',')]'''
sum=0
for f in list:
    sum+=f
print("sum is",sum)
