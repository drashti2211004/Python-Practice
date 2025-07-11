import random

otp = random.randint(1001,9999)

d={}
while True:
    menu = """
    press 1 for Signup
    press 2 for Login
    press 3 for Forgot-Password
    press 4 for Exit
    """
    print(menu)

    choice = int(input("Enter your Choice: "))

    if choice==1:
        print("******************** Welcome to Login *********************")

        name = input("Enter Name: ")
        email = input("Enter your Email: ")
        mobile = int(input("Enter Your Mobile Number: "))
        password = int(input("Enter Password: "))
        cpassword = int(input("Enter Confirm Password: "))

        if password==cpassword:
            d['email']=email
            d['mobile']=mobile
            d['password']=password

            print("signup Successfully!!")
        else:
            print("password & confirm password does not match!!")

    elif choice==2:
        print("******************** Welcome to Login *********************")
        email = input("enter Email: ")
        password = int(input("enter your Password: "))

        if d['email']==email:
            if d['password']==password:
                print("Login sucessfully!!")

            else:
                print("Password does not match!!")
        else:
            print("Email does not match!!")

    elif choice==3:
        print("******************** Welcome to Forgot-Password *********************")
        mobile=int(input("Enter Mobil number: "))

        if d['mobile']==mobile:
            print("your otp is:",otp)

            uotp = int(input("Enter your otp: "))

            if otp==uotp:
                password=int(input("Enter NEw Password: "))
                d['password']=password
                print("password update successfully!!")
            else:
                print("Invaild otp: ")
        else:
            print("Mobile number does not exits!!")
    
    elif choice==4:
        print("Thank You!!")
        break
    
    else:
        print("Invaild choices!!")
        break





   
