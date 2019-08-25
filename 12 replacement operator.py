x=10
y=3.5
z='Gaurav'
print('Hello, ',z,'x=',x,'y=',y)

'''with the above code we can see that there is a iregular space between hello
and gaurav which is taken by default by the seperator, let us see the work of
replacement operator'''

x=10
y=3.5
z='Gaurav'
print('Hello,{2} x={0} y={1}'.format(x,y,z))

'''The above code  uses the indexing format as 0,1 and 2 which is needed to be
specified in curly brackets to print the output in correct format, now what if
we dont mention anything in curly brackets'''

x=10
y=3.5
z='Gaurav'
print('Hello, {} x={} y={}'.format(x,y,z))

'''The result will be printed in the format which is specified, that is in first
curly bracket x's value will come and in the second curly bracket y's value will come and
then at last z's value will come'''

''' we can change the format also in our way like as follow'''
x=10
y=3.5
z='Gaurav'
print('Hello, {} x={} y={}'.format(z,x,y))

'''now suppose we mention the variable in the curly braces itself, then in that
case we need to define the values in format itself, if we define there then
what ever we have initialised earlier will not be taken into consideration by
interpreter'''
x=10
y=3.5
z='Gaurav'
print('Hello, {z} x={x} y={y}'.format(z='GauraV',x=1,y=2))

