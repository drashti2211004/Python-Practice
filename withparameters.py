def prime(n):   #paramters
    prime=0
    for i in range(1,n+1):
        if n%i==0:
            prime+=1
    if prime==2:
        print("prime number")
    else:
        print("not a prime number")

n=int(input("enter your number: "))
prime(n)  #argument

def add(a,b):
    print("Addition: ",a+b)

a=int(input("Enter your 1 number: "))
b=int(input("Enter your 2 number: "))
add(a,b)