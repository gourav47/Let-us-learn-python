'''0 1 1  2 3 5 8 13 .....'''
#Fibonacci Series
def fibonacci(n):
    a,b,c=0,1,0
    while True:
        if c>n:
            return
        yield a
        a,b=b,a+b
        c+=1
#yield follwed by value ('a'in this program) returns the nnext value and yield pauses the fuction
#and get resumed after next method is called and stops at yield only.
#when return is executed here it raises an exception whic is StopIteration.
#so, in this progrm insted of writing return we can use raise StopIteration
