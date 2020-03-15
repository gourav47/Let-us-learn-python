def f1(playername,*points):
    print(playername,end=' ')
    s=0
    for x in points:
        s=s+x
    print("Total points is:",s)
f1(playername="Ajay",10,20,30,56)

#the above line will throw error because after keyword argument psoition argument is invalid.

