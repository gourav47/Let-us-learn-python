'''Variable length argument'''
def avg(*n):
    s=0
    for x in n:
        s=s+x
    return s/len(n)
x=avg(10,20,30,40,50,60)
print("Average is:",x)

def avg2(*n):
    print(n,type(n))
avg2(10,20,30)

def avg(*n):
    s=0
    for x in n:
        s=s+x
    return s/len(n)
x=avg()
print("Average is:",x)
