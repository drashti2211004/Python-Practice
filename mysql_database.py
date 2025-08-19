from crud_operations import *

mydb = pymysql.connect(host="localhost",user="root",passwd="",database="signup")
mycursor = mydb.cursor()

while True:
    menu = """
        press 1 for insert data
        press 2 for update data
        press 3 for delete data
        press 4 for fetch data
        press 5 for exit
        """
    
    print(menu)
    choice = int(input("enter choice : "))

    if choice == 1:
        name = input("enter name :  ")
        subject = input("enter subject : ")

        query = "insert into data (name,subject) values ('%s','%s')"
        args = (name,subject)

        mycursor.execute(query % args)
        mydb.commit()
        print("data inserted!!")

    elif choice == 2:
        id = int(input("enter id : "))
        name = input("enter name :  ")
        subject = input("enter subject : ")

        query = "update data set name='%s' ,subject='%s' where id='%s'"
        args = (name,subject,id)

        mycursor.execute(query % args)
        mydb.commit()
        print("data updated!!")

    elif choice == 3:
        id = int(input("enter id : "))

        query = "delete from data where id='%s'"
        args = (id)

        mycursor.execute(query % args)
        mydb.commit()
        print("data deleted!!")


    elif choice == 4:
        #id = int(input("enter id : "))

        query = "select * from data "
        #args = (id)

        mycursor.execute(query)

        mydata = mycursor.fetchall()

        print(mydata)



    elif choice == 5:
        print("thank you!!")
        break
    else:
        print("invalid choice!!")
        break