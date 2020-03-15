x = "abcdef"
i = "a"
while i in x:
    x = x[:-1]
    print(i, end = " ")
#2nd program
    x = "abcdef"
i = "a"
while i in x[:-1]:
    print(i, end = " ")
