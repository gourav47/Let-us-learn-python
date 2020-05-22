''''python script to count the occurrence of a character'''
s=input("Enter a string: ")
t=input("Enter the character you want to search the occurence for: ")
count=0
for e in s:
    if e in t:
        count+=1
print("Number of occurence is: ",count)
