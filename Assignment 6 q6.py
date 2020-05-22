'''python script to print indices of all occurrences of a given element in list'''

l=[eval (x) for x in input("Enter list elements").split(',')]

#eval funtion converts ths string into int type
element=eval(input("Enter element value"))
index=0
while index<len(l):
    if l[index]==element:
        print(index,end=' ')
    index+=1
