'''Write a python script to print the set of first N prime numbers'''
n=int(input("Enter the number till which prime number is needed:"))
x=2
s=set()     #creating an empty set
while n:    #loop statements until n is zero
    if all(x%i!=0 for i in range(2,x)):   #check x for prime numbers
        s.add(x)
        n-=1
    x+=1
print("Set of prime number is: ",s)
