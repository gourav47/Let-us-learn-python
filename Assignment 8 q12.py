'''calculate the frequency of elements of tuple'''
t=eval(input("Enter the first tuple: "))
i=0
for e in t:
    if t.index(e)==i:
        print("frequency of",e,"is",t.count(e))
    i+=1
