'''Arrange three words in dictionary order'''
print('Enter three city names: ')
a,b,c=input(),input(),input()
if a<b<c:
    print(a,b,c)
elif a<c<b:
    print(a,c,b)
elif b<a<c:
    print(b,a,c)
elif b<c<a:
    print(b,c,a)
elif c<b<a:
    print(c,b,a)
else:
    print(c,a,b)

'''Another simple way without using conditional operator'''

print('Enter three city names:')
a,b,c=input(),input(),input()
x=min(a,b,c)
print(x)
if x==a:
    print(min(b,c),max(b,c))
elif x==b:
    print(min(a,c),max(a,c))
else:
    print(min(a,b),max(a,b))

'''Single line pragram'''
[x for x in sorted(input('Enter comma seperated city names: ').split(',')) if print(x,end=' ')]

    
