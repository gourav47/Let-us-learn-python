def f1(**k):
    print("Person Information")
    for key,value in k.items():
        print(key,"-",value)
f1(name="Sameer",age=22)
f1(name="Rahukl",marks=87,age=23)
f1(name="Ajay",empid=125,salry=35000.0)
