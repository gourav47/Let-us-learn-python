def f1(playername,*points):
    print(playername,end=' ')
    s=0
    for x in points:
        s=s+x
    print("Total points is:",s)
f1("Ajay",10,20,30,56)
f1("Amit",11,13,57,15)
f1("Anurag")



