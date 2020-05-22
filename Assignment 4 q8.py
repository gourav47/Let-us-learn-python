'''python script to print prime factors of a given number'''
n=int(input("Enter a number: "))
x=n
p=2
while x>1:
    while x%p==0:
        print(p,end=' ')
        x//=p
    p=p+1
    while True:
        for i in range(2,p):
            if p%i==0:
                p=p+1
                break
        else:
            break
