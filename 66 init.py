class test:
    i=10
    def __init__(self,x,y):
        self.a=x      #a and b is an instance variable
        self.b=y

t1=test(10,20)  #instantiation (object created so __init__ function will be called.
t2=test(3,4)
t3=test(100,50)
print(t1.a,t1.b)
print(t2.a,t2.b)
print(t3.a,t3.b)
