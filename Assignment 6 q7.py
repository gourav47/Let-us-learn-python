'''print distinct list elements along with their frequency of
occurrence in the list '''
l=[int (x) for x in input("Enter list elements").split(',')]
i=0
for e in l:
    if l.index(e)==i:
        print(e,"-----",l.count(e))
    i+=1
   
    
