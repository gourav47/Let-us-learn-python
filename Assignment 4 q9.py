'''python script to find the LCM of two numbers'''
print("Enter two numbers: ")
a,b=int(input()), int(input())
L=max(a,b)
while L<=a*b:
    if L%a==0 and L%b==0:
        print("LCM is",L)
        break
    L+=1
   
