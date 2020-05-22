'''count the elements of the set'''
print("Enter comma seperated set elements: ")
s1={int(e) for e in input().split(',')}
print("Total elements in the set are",len(s1))
