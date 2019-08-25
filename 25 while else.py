'''Game program to enter even number in three chance'''
#idea is to understand the concept of while-else

i=1
while i<=3:
    x=int(input("Enter an Even Number: "))
    if x%2==0:
        print("You Win")
        break
    i=i+1
else:
    print("you lost")
