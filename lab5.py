# To show the usages of various Operators available in python
#5a
#arithmetic operators
a=int(input('Enter the first number:'))
b=int(input('Enter the second number:'))
sum=a+b
diff=a-b
prod=a*b
div=a/b
rem1=a%b
rem2=-a%b
rem3=a%-b
rem4=-a%-b
exp=a**b
flr=a//b
print('Sum of {} and {} is {} '.format(a,b,sum))
print('Difference of {} and {} is {} '.format(a,b,diff))
print('Product of {} and {} is {} '.format(a,b,prod))
print('Quotient of {} and {} is {} '.format(a,b,div))
print('Remainder of {} and {} is {} '.format(a,b,rem1))
print('Remainder of -{} and {} is {} '.format(a,b,rem2))
print('Remainder of {} and -{} is {} '.format(a,b,rem3))
print('Remainder of -{} and -{} is {} '.format(a,b,rem4))
print('Exponentiation of {} raised to {} is {} '.format(a,b,exp))
print('Floor function of {} and {} is {} '.format(a,b,flr))


#assignment operators
x=2
print('x=',x)
x+=15
print('x=',x)
x-=5
print('x=',x)
x*=2
print('x=',x)
x/=2
print('x=',x)
x%=2
print('x=',x)
x//=2
print('x=',x)
x**=2
x=10
print('x=',x)
x&=2
print('x=',x)
x|=2
print('x=',x)
x^=1
print('x=',x)
x>>=4
print('x=',x)
x<<=5
print('x=',x)

#logical operators
print(x<100 and x>25)
print(y<30 or y<20)
print(not(z>30))

#identity operators
a=['Hello','World']
b=['Hello','World']
print(a is b)
print(a is not b)

#membership operators
c='World'
print(c in a)
print('Python' not in b)

#bitwise operator
print(y&z)
print(y|z)
print(y^z)
print(~z)
print(y<<z)
print(y>>z)

#5b
rate=12
overtime=0
payoff=0
total=0
for i in range(0,10):
    hours=int(input('Enter the total work hours of employee{}:'.format(i+1)))
    if hours>40:
        overtime=hours-40
        payoff=overtime*rate
        total+=payoff
        print("Overtime payoff of employee {} is {}".format(i+1,payoff))
    else:
        print("Employee {} is not eligible for overtime".format(i+1))
print("Total overtime cost:",total)
