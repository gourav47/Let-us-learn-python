'''check whether the given set is subset of another given set or not.'''
s1={1,2,3,4,5}
s2={1,2,3}
s3={4,5,6,7}
if s2.issubset(s1):
    print("s2 is subset of s1")
elif s3.issubset(s1):
    print("s3 is a subset of s1")
