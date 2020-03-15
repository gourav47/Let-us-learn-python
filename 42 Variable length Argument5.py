def f1(*points,playername):
    print(playername,end=' ')
    s=0
    for x in points:
        s=s+x
    print("Total points is:",s)
f1(10,20,30,56,playername="Ajay")

