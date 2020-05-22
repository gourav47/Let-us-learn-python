'''print the sum of all even numbers and sum of all odd numbers in the list '''

print("Enter list of integers seperated by comma")
list1=[int(x) for x in input().split(',')]
sum_of_even,sum_of_odd=0,0
for e in list1:
    if e%2==0:
        sum_of_even+=e
    else:
        sum_of_odd+=e
print("Sum of all even elements is",sum_of_even)
print("sum of all odd elements is",sum_of_odd)
