'''check for co-prime numbers'''
print("Enter tow numbers: ")
l,u=int(input()),int(input())
h=min(l,u)
while h>=1:
    if l%h==0 and u%h==0:
        if h==1:
            print("Co-Prime Numbers")
        else:
            print("Not a co-prime numbers")
        break
    h-=1
        
