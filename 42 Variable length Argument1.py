def avg(*n):
    s=0
    for x in n:
        s=s+x
    if len(n)!=0:
        return s/len(n)
    else:
        return "No Elements"
x=avg()
print("Average is:",x)
