'''calculate the average of tuple values. Assuming values are of int type only'''
'''n=int(input("Enter the number of values you want to enter: "))'''
t=eval(input("Enter the values: "))
s=0
for e in t:
    s+=e
avg=s/len(t)
print("Average of tuple values is",avg)

