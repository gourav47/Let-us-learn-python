'''find the  common elements in the set'''
print("Enter comma seperated elements for the first set:")
s1={int(e) for e in input().split(',')}
print("Enter comma seperated elements for the second set:")
s2={int(e) for e in input().split(',')}
print("Common elements are: ")
for e in s1.intersection(s2):
    print(e,end=' ')

'''other way'''
s1=set(input("Enter the values of first set: ").split(','))
s2=set(input("Enter the values of second set: ").split(','))
s3=set(s1.intersection(s2))
print(s3,end=' ')
