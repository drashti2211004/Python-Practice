import random

ac_no = random.randint(100000000001,999999999999)
password = random.randint(1001,9999)

class Bank:
    def ac_register(self):
        name = input("Enter Name: ")
        email = input("Enter Email: ")
        mobile = int(input("Enter Mobile: "))
        balance = 5000

        self.balance = balance
        self.name = name
        print("your account number is :" ,ac_no)
        print("your password number is :", password)

    def deposit(self):
        damount = int(input("Enter Deposit Amount : "))
        print("your Deposited Amount is : ",damount)
        self.balance+=damount

    def withdraw(self):
        wamount = int(input("Enter Withdraw Amount: "))
        print("your withdraw Amount is: ",wamount)


        if wamount>self.balance:
            print("Invaild Amount!!")

        else:
            self.balance-=wamount

    def check_balance(self):
        print(f"{self.name} your account balance is {self.balance}")

obj = Bank()

print("press 1 for Create Account")
print("press 2 for Exit")

choice = int(input("Enter Choice : "))

if choice==1:
    obj.ac_register()

    while True:
        menu = """
        press 1 for Deposit Amount
        press 2 for Withdrew Amount
        press 3 for Check Balance
        press 4 for Exit
        """

        print(menu)
        choice1 = int(input("enter choice: "))

        if choice1==1:
            obj.deposit()

        elif choice1==2:
            obj.withdraw()

        elif choice1==3:
            obj.check_balance()

        elif choice1==4:
            print("Thank You !!")
            break
        
        else:
            print("Invalid chice!!")
            break

else:
    print("Thank You !!")


