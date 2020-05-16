### program to search the city name and change the content###

So with this logic codes comes as :
f=open('file2.txt','r+')
x="Indore\n"
s=f.readline()
while True:
    if s==x:
        f.seek(-len(s),1)
        f.write("INDORE\n")
        break
    s=f.readline()
f.close()



##correct logic ##

f=open('file3.txt','r+')
x="Indore\n"
s=f.readline()
l=0
while True:
    if s=='':
        break
    l+=len(s)
    if s==x:
        f.seek(l-len(s),0)
        f.write("INDORE")
        break
    s=f.readline()
f.close()
