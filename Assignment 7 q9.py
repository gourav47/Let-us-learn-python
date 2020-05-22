'''python script to find a pattern in a given string'''
s=input("Enter a string:")
p=input("Enter a pattern to search in the string: ")
if p in s:
    print(p,"is in the string",s)
else:
    print(p,"is not in the string",s)
    
