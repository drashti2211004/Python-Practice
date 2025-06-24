n=int(input("Enter your number: "))
if n<=0:
    print("enter Positive number")
else:
    if n==1 or n==2 or n==3:
        print("prime")
    else:
        prime=0
        for i in range(1,n+1):
            if(n%1==0):
                prime+=1
        if prime==2:
            print(n,"is prime number")
        else:
            print(n,"not a prime number")