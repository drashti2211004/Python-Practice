from diff_class import *

obj = Prime()
obj1 = Patten()
obj2 = Table()
obj3 = Reverse()

while True:
    menu = """
    press 1 for Prime
    press 2 for Patten
    press 3 for Table
    press 4 for Revers
    press 5 for exit
    """

    print(menu)

    choice=int(input("Enter your Choice: "))

    if choice == 1:
        obj.prime()

    elif choice == 2:
        obj1.patten()

    elif choice == 3:
        obj2.table()

    elif choice == 4:
        s = input("Enter name: ")
        print(obj3.rev(s))

    elif choice == 5:
        print("Thank you !!")
        break

    else:
        print("Invalid choices...")
        break


