
while True:
    menu="""
    press 1 for prime number
    press 2 for pyramid
    press 3 for factorial
    press 4 for exit
"""
    print(menu)
    choice=int(input("entrr choice: "))

    if choice==1:
        #print("prime number")

        n=int(input("Enter your prime number: "))
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
                    print(n,"is a prime number")
                else:
                    print(n,"not a prime number")

    elif choice==2:
        #print("pyramid")

        for i in range(1,6):
            print(" "*(6-i)," *"*i)      

    elif choice==3:
        #print("factorial")

        n=int(input("enter number: "))
        fac=1
        i=1
        while(i<=n):
            fac*=i
            i=i+1
            print(fac)

    elif choice==4:
        print("Thank you !!")
        break
    else:
        print("Invalid choce !!")
        break
