'''Program to understand the pass keyword'''
'''if we are running a statement and we want that if the codition of 'if' is
executed then no operations is needed to be performed then there comes the role of
pass keyword'''
'''Now the issue is if we code this in C/C++/Java then we can simply put the curly
brackets and print the next statement, however this is not possible in python
as python understands indentation, lets see how we can do that'''

x=0
if x==0:
print("Hello") '''print statement doesnot depend on if condition, but there is
                  no indentation for if block, hence it will throw error as
                  expected and indented block as shown below'''

'''so for that reason we will use the keyword pass, lets see how it goes through
after using the pass keyword'''

#hence we will use pass keyword when we need to make empty block.
#it will be treated as there is nothing in the block and the program will be passed

x=0
if x==0:
    pass
print("Hello")
