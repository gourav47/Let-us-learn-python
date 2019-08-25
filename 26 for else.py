#program to print the prime numbers between a and b
a=int(input("Enter smaller number: "))
b=int(input("Enter greater number: "))
s=range(a,b)
for x in s:
    for num in range(2,x):
        if x%num==0:
            break
    else:
        print(x,"is prime in range")
        break

'''if the last break is not used then the program will print all the prime-
numbers in the range of a and b, however if it is used then it will print
the immediate prime number after the first number a'''
        
	
