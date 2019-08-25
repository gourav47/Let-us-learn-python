'''Command line argument'''
from sys import argv
print(argv)

'''using for loop'''
for x in argv:
    print(x)

'''type of x'''

for x in argv:
    print(x, type(x))


'''perform sum operation with the arguments passed'''
#command line argument
from sys import argv
y=0
s=0
for x in argv:
    if y==0:
        y=1
    else:
        s=s+int(x)
print("Sum is: ",s)
   
