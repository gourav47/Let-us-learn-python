'''union of two sets'''
s1=set(input("Enter the values of first set: ").split(','))
s2=set(input("Enter the values of second set: ").split(','))
print("The union of the sets are: ",(s1.union(s2)),end=' ')

#the above code will give output with commas and single inverted commas
#the below code will give output without commas and single inverted commas

print("Enter comma seperated elements for the firsrt set")
s1={int(e) for e in input().split(',')}
print("Enter comma seperated elements for the second set")
s2={int(e) for e in input().split(',')}
print("union of two sets are: ")
for e in s1.union(s2):
    print(e,end=' ')
    
