#program 1
x = 'abcd'
for i in range(len(x)):
    x[i].upper()
print (x)

'''program 2:
x = 'abcd'
for i in range(len(x)):
    i[x].upper()
print (x)'''

#program 3:
x = 'abcd'
for i in range(len(x)):
    x = 'e'
    print(x)

#program 4:
x = 'abcd'
for i in range(len(x)):
    print(x,end='')
    x = 'a'
