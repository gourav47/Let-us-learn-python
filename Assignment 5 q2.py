'''python script to print a table of user’s choice'''
n=int(input('Enter a number for which the mutiple table is needed: '))
i=int(input('Enter a number till which the number table is neede: '))
for x in range(n,(n*(i+1)),n):
    print(x,end=' ')
    
