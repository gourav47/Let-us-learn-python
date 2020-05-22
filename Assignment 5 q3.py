'''python script to print all Armstrong numbers under 1000''' 
for x in range(1,1001):
    n=x
    s=0
    while x:
        r=x%10
        s=s+r**3
        x=x//10
    if s==n:
        print(n)

'''python script to check whether the inout provided by the user is Armstrong
or not needs clear concept of Functions, hence we will do the same program after
gaining knowledge about functions'''
