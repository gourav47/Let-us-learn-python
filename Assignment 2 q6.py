'''python script to take month value in numeric format and display number of days in it'''
year=int(input('Enter a four digit year: '))
month=int(input("Enter month's numeric value: "))
d1=31
d2=30
d3=28
d4=29
if month==1:
    print('Month is january and has %d days'%d1)
if month==2 and year%4!=0:
    print('Year is non-leap and the monthe is febuary and has %d days'%d3)
if month==3:
    print('Month is March and has %d days'%d1)
if month==4:
    print('Month is April and has %d days'%d2)
if month==5:
    print('Month is May and has %d days'%d1)
if month==6:
    print('Month is june and has %d days'%d2)
if month==7:
    print('Month is july and has %d days'%d1)
if month==8:
    print('Month is August and has %d days'%d1)
if month==9:
    print('Month is september and has %d days'%d2)
if month==10:
    print('Month is october and has %d days'%d1)
if month==11:
    print('Month is november and has %d days'%d2)
if month==12:
    print('Month is december and has %d days'%d1)
elif month==2 and year%4==0:
    print('Year is leap and the month is febuary and has %d days'%d4)
