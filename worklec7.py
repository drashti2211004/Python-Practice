
while True:
    menu="""
    press 1 for prime number
    press 2 for pyramid
    press 3 for factorial
    press 4 for factorial with fun and with return
    press 5 for exit
"""
    print(menu)
    choice=int(input("entrr choice: "))

    if choice==1:
        #with parameters(prime number)

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

    elif choice==2:
        #withoutparamter(pyramid)

        def pyramid():
            for i in range(1,6):
                print(" "*(6-i)," *"*i)    
        pyramid()  

    elif choice==3:
        #function without and return type(factorial)

        def fun1():
            n=int(input("Enter Number: "))
            fac=1
            
            for i in range(1,n+1):
                fac*=i

            return fac
        print(fun1())

    elif choice==4:
        #function with and return type(factorial)

        def fan(n):
            fac=1
            
            for i in range (1,n+1):
                fac*=i
            return fac
        n=int(input("eneter your number: "))
        print(fan(n))


    elif choice==4:
        print("Thank you !!")
        break
    else:
        print("Invalid choce !!")
        break
