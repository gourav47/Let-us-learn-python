'''program to understand the concept of list part 1: '''
l=[]
l.append(10)
l.append(20)
l.append(30)

'''the above statement l.append is the basic way to store the value in empty
list by using the function append'''

print(l)

#above way is one method to print the list, there are other ways also

print(l[0],l[1],l[2])

#above way is via indexing method.

'''The difference between normal print method and indexing print method is that
normal print method will show the oputput in square bracket with a comma and space,
however in indexing method it is printed normally with a space in between.'''

for x in l:
    print(x)

#above method is the iterable method.

'''in this case it will print each value in different lines'''

'''This program gives the basic idea how we can create a list and how to store
values in it and print in different ways.'''

l=[10,20,30]
print(l[0],l[1],l[2])
for x in l:
    print(x)

