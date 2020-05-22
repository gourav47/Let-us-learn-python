'''python script to count words in a given string'''
s=input("Enter a string: ")
print("Total words is", s.count(' ')+1)

#the above program is not robust
'''because if a user types one word and give 4 spaces and the type the
second word and gives 5 spaces, in that scenario program will not show
actual results, we need to make a robust program'''


s=input("Enter the string: ").strip() #strip function will remove the spaces from front and back
print("total words: ", len([i for i in range(0,len(s)) if s[i]==' '  and s[i+1]!=' '])+1)
