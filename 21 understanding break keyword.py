'''Game program to enter even number in three chance'''
#idea is to understand the concept of break

chance=1
while chance<=3:
    x=int(input("Enter an Even Number: "))
    if x%2==0:
        break
    chance+=1
if chance==4:
    print("You lost")
else:
    print("you Win")

'''as per the code's logic, 3 chance will be given to the player to enter the
correct even number, if the 3 chance is exceeded then the player looses'''
'''we can see that the chance will run only three times, however what if the
player gives the right answer in first attempt, in that case we need to apply
break in the middle of the execution of the loop, this is the scenario where
the role of 'break' keyword comes'''
