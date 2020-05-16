##f=open('file1.txt','w')
##text=input("Enter some text: ")
##f.write(text)
##f.close()

###writline function####
##f=open('file2.txt','w')   #it will create a text file named as  file2
##l=["Bhopal\n","Delhi\n","Indore"]
##f.writelines(l)         #this will print the contents of list
##f.close()


### Read operations  ####

##f=open('file2.txt','r')
###s0=f.read()
##s1=f.read(5)
##s2=f.read(5)
###print(s0)
##print(s1)
##print(s2)
##f.close()

## Read Operations without Read command ###

##f=open('file2.txt','r')
##for line in f:
##    print(line)
##f.close

## Readlline ##

##f=open('file2.txt','r')
##s1=f.readline()   
##print(s1)
##s1=f.readline()   
##print(s1)
##s1=f.readline()   
##print(s1)
##s1=f.readline()   
##print(s1)
##
##f.close()
## loop to understand for end of file ##

##f=open('file2.txt','r')
##while True:
##    s1=f.readline()
##    if s1=='':
##        break
##        s1=f.readline()
##    print(s1)
##print("out of while loop")
##f.close()

### readlines ###
##f=open('file2.txt','r')
##s=f.readlines()
##print(s)
##f.close()

### program to search the city name ###
f=open('file2.txt','r')
s=f.readlines()
x=input("Enter city name:")
x+='\n'
for e in s:
    if e==x:
        print("Matched city is: ",e)
    else:
        print("Match not found")
f.close()
