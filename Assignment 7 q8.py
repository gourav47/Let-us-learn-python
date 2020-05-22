'''python script to remove duplicate characters from a given string'''
names=[]
n=int(input("How many names you want to enter?: "))
for i in range(n):
    print(i+1,"Enter name: ") #to print it sequentially from 1
    names.append(input())
s=set(names)
names=list(s)
for x in s:
    print(x)
    
