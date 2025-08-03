class myclass1():
    def fun1(self):
        n = int(input("Enter Number:"))
        if n==0:
            print("Not even or Not odd")

        elif n%2 == 0:
            print("Even")

        else:
            print("odd")

class myclass2(myclass1):
    def fun2(self):
        n = int(input("Enter Age:"))
        if n>100:
            print("Invalid Age")

        elif n>=18:
            print("valid for vote")

        else:
            print("not valid age")

class myclass3():
    def fun3(self):
        n=int(input("enter number: "))
        fac=1
        i=1
        while(i<=n):
            fac*=i
            i=i+1
            print(fac)


class myclass4(myclass2,myclass3):
    def fun4(self):
        for i in range(1,6):
            print(" "*(6-i)," *"*i)
        for i in range(5,0,-1):
            print(" "*(6-i)," *"*i)

            
obj = myclass4()

while True:
    menu="""
    press 1 for odd..even..
    press 2 for if..loop..
    press 3 for factorial
    press 4 for diamond
    press 5 for exit
"""
    print(menu)
    choice=int(input("enter choice: "))



    if choice==1:
        #print("****odd__even number****")
        obj.fun1()

    elif choice==2:
        #print("**** if...loop ****")
        obj.fun2()
        
    elif choice==3:
        #print("factorial")
        obj.fun3()

    elif choice==4:
        obj.fun4()

    elif choice==5:
        print("Thank you !!")
        break

    else:
        print("Invalid choce !!")
        break
