#To find sun and average of natural number up to n where n is provided by user
num = int(input("Enter the number of terms: "))
num1 = num
if num < 0:
     print("Please enter a positive number")
else:
    sum = 0
    while(num > 0):
        sum += num
        num -= 1
    print("The sum of first {} natural numbers is:{} ".format(num1,sum))
    print("The average of first {} natural numbers is:{}".format(num1,sum/num1))
    
    
#To find the factorial of a number(Iterative method)
def fact_iter(n):
    f=1
    i=1
    while(i<=n):
        f=f*i
        i=i+1
    return f


n=int(input("Enter the number:"))
if(n<0):
    print("Invaid input")
elif(n==0):
    print("Factorial of 0 is 1")
else:
    f=fact_iter(n)
    print("Factorial of {} is: {}".format(n,f))

#To find the factorial of a number(Recursive method)
def fact_rec(n):
    if(n==0 or n==1):
        return 1;
    else:
        return(n*fact_rec(n-1))
    
n=int(input("Enter the number:"))
if(n<0):
    print("Invaid input")
else:
    f=fact_rec(n)
    print("Factorial of {} is: {}".format(n,f))
    
    
    
#To genearte N terms of fibonacci series(Iterative method)
def Fibonacci_itr():
    nterms = int(input("Enter the number of terms:"))
    # first two terms
    n1 = 0
    n2 = 1
    count = 0
    # check if the number of terms is valid
    if nterms <= 0:
        print("Please enter a positive integer")
    elif nterms == 1:
        print("Fibonacci sequence upto",nterms,":")
        print(n1)
    else:
        print("Fibonacci sequence upto",nterms,":")
    while count < nterms:
        print(n1,end=' , ')
        nth = n1 + n2
        # update values
        n1 = n2
        n2 = nth
        count += 1

print(Fibonacci_itr())


#To genearte N terms of fibonacci series(Recursive method 1)
def Fibonacci_rec(q):
    if q==1:
        return 0;
    elif q == 2:
        return 1;
    else:
        return Fibonacci_rec(q-1)+Fibonacci_rec(q-2)
    
m = int(input("Enter the number of terms :"))
for Num in range(1,m+1):
    print(Fibonacci_rec(Num),end=' ')
  
 #To genearte N terms of fibonacci series(Recursive method 2)
def Fibonacci_rec(q):
    if q == 1:
        return 0
    elif q == 2:
        return 1
    else:
        return Fibonacci_rec(q-1) + Fibonacci_rec(q-2)
    
m = int(input("Enter the number of terms :"))
print(Fibonacci_rec(m),end=' ')
        
 #sum
def sum_avg(n):
    sum=0
    i=1
    while(i<=n):
        sum=sum+i
        i=i+1
    print(sum)
    avg=sum/n
    print(avg)
    
n=int(input("Enter the limit"))
sum_avg(n)





#upperlimit
n=int(input("Enter upper limit of range: "))
sieve=set(range(2,n+1))
while sieve:
    prime=min(sieve)
    print(prime,end="\t")
    sieve-=set(range(prime,n+1,prime))
 
print()
