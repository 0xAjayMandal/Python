#lab1a
a = 10
b = 99.99
c = True
d = "Hello World"
e = [8,4,2,1,"Ajay"]
f = (8,7,5,1,"Ajay")
g = {2,2,8,1,3,3}
h = {"name":"Ajay","Age":22}
print("Value of a =",a)
print("Type of a is : ",type(a))
print("Value of a =",b)
print("Type of a is : ",type(b))
print("Value of a =",c)
print("Type of a is : ",type(c))
print("Value of a =",d)
print("Type of a is : ",type(d))
print("Value of a =",e)
print("Type of a is : ",type(e))
print("Value of a =",f)
print("Type of a is : ",type(f))
print("Value of a =",g)
print("Type of a is : ",type(g))
print("Value of a =",h)
print("Type of a is : ",type(h))

#swap
a = int(input("Enter the first number:"))
b = int(input("Enter the Second number :"))
print("Number before swapping a=",a,"b=",b)

a,b = b,a
print("Number after swapping a=",a,"b=",b)


#lab1b
a = int(input("Enter 1st Number"))
b = int(input("Enter 2nd Number"))
sum = a+b
diff = a-b
prod = a*b
div = a/b
pow = a**b
mod = a%b
flrdiv = a//b

print("Sum of {} and {} is : {}".format(a,b,sum))
print("Difference of {} and {} is : {}".format(a,b,diff))
print("Product of {} and {} is : {}".format(a,b,prod))
print("Division of {} by {} is : {}".format(a,b,div))
print("Power of {} on {} is : {}".format(a,b,pow))
print("Remainder of {} and {} is : {}".format(a,b,mod))
print("FloorDivision of {} by {} is : {}".format(a,b,flrdiv))




#
a,b,c,d = 20,10,10,5

e = (a+b)*c/d
print("Value of (a+b)*c/d is : ",e)

e = ((a+b)*c)/d
print("Value of ((a+b)*c)/d is : ",e)

e = (a+b)*(c/d)
print("Value of (a+b)*(c/d) is : ",e)

e = a+(b*c)/d
print("Value of a+(b*c)/d is : ",e)
