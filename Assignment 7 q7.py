'''python script to check whether the given string is palindrome or not'''

s=input("Enter a string: ")
if s==s[::-1]:
    print("String is pallindrome")
else:
    print("string is not pallindrome")
