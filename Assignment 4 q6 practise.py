'''print first N odd natural numbers '''
n=int(input("Enter a number: "))
if n%2==0:
    for x in range(n-1,0,-2):
        print(x,end=' ')
else:
    for x in range(n-2,0,-2):
        print(x,end=' ')
