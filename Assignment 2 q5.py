'''python script to check if a year is leap year or not'''
year=int(input('Enter a four digit year: '))
if(year%4==0):
    print('%d is leap year'%year)
else:
    print('%d is a normal year'%year)
