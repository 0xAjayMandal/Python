#Method1
num = int(input("Enter a number: "))  
if num > 1:  
    for i in range(2,num):  
        if (num % i) == 0:  
            print(num,"is not a prime number")  
            print(i,"times",num//i,"is",num)  
            break  
    else: 
        print(num,"is a prime number")  
else:  
       print(num,"is not a prime number")
    
  
#Method2
num = int(input('Enter the number'))
if num > 1:
    for i in range(2, (num//2)+1):
        if (num % i) == 0:
            print(num, "is not a prime number")
            print(i,"times",num//i,"is",num)
            break
    else:
         print(num, "is a prime number")
else:
    print(num, "is not a prime number")
    
    
#Method3
import math

num = int(input("Enter a number: "))  

if num > 1:  
    for i in range(2,math.floor(math.sqrt(num))):  
        if (num % i) == 0:  
            print(num,"is not a prime number")  
            print(i,"times",num//i,"is",num)  
            break  
    else:  
        print(num,"is a prime number")  
else:  
       print(num,"is not a prime number")
    
#Range
lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))

print("Prime numbers between",lower,"and",upper,"are: ")
for num in range(lower,upper + 1):
    if num > 1:
        for i in range(2, (num//2)+1):
            if((num % i) == 0):
                break
        else:
            print(num,end=',')
            
#2            
lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))

print("Prime numbers between",lower,"and",upper,"are: ")
for num in range(lower,upper + 1):
    if num > 1:
        for i in range(2, num):
            if((num % i) == 0):
                break
        else:
            print(num,end=',')
            
#Prime nubers upto n
n = int(input("Enter limit: "))

print("Prime numbers upto",n,"are: ")
for num in range(2, n + 1):
    if num > 1:
        for i in range(2, (num//2)+1):
            if((num % i) == 0):
                break
        else:
            print(num,end=',')
            
 #gcd           
def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)
    
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
GCD=gcd(a,b)
print("GCD of {} and {} is:{}".format(a,b,GCD))
