'''python script to count vowels in a given string'''
s=input("Enter the string: ")
l=len(s)
v="aeiouAEIOU"
count=0
for e in s:
    if e in v:  #we cannot write v in e, as that will check compleate aeiouAEIOU in the string
        count+=1
print("Total vowels:",count)

