'''create a power set of a given set'''
print("Enter comma seperated set elements: ")
s1={int(e) for e in input().split(',')}
l1=list(s1)
n=len(s1)
powerset=set()
for i in range(2**n):
    t=tuple({l1[j] for j in range(n) if (i&(1<<j))})
    powerset.add(t)
print(powerset)
