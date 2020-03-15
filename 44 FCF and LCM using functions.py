def LCM(a,b):
    L=max(a,b)
    while L<=a*b:
        if L%a==0 and L%b==0:
            return L
        L+=1
x=LCM(4,6)
print("LCM is:",x)

def HCF(c,d):
    H=min(c,d)
    while H>=1:
        if c%H==0 and d%H==0:
            return H
        H-=1
y=HCF(4,6)
print("HCF is:",y)
    
