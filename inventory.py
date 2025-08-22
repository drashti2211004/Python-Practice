from Inventory_database import * 
 
mydb = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="inventory"
)
mycursor = mydb.cursor()


while True:
    menu = """
        press 1 for manager
        press 2 for customer
        press 3 for exit
        """
    print(menu)
    choice = int(input("enter choice : "))

    if choice ==1:
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
                name = input("Enter friut name: ")         
                price = input("Enter price: ")
                quantity = input("Enter quantity: ") 
                query = "INSERT INTO manager1(name, price, quantity) VALUES (%s, %s, %s)"
                args = (name, price, quantity)

                mycursor.execute(query, args)  
                mydb.commit()
                print("Data inserted successfully!")

            elif choice == 2:
                id = int(input("enter id : "))
                name = input("enter friut name :  ")
                price = input("enter price : ")
                quantity = input("enter quantity : ")


                query = "UPDATE manager1 SET name=%s, price=%s, quantity=%s WHERE id=%s"
                args = (name ,price ,quantity ,id)

                mycursor.execute(query , args)
                mydb.commit()
                #print("data updated!!")
                if mycursor.rowcount == 0:
                    print("No record found with that id. Update failed.")
                else:
                    print("Update data successfully!")


            elif choice == 3:
                id = int(input("enter id : "))

                query = "delete from manager1 where id='%s'"
                args = (id,)

                mycursor.execute(query % args)
                mydb.commit()
                print("data deleted!!")


            elif choice == 4:
                #id = int(input("enter id : "))

                query = "select * from manager1 "
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

    elif choice == 2:
        while True:
            menu = """
                press 1 to view all products
                press 2 to search product by name
                press 3 to search products by price range
                press 4 to check product quantity 
                press 5 to exit
                """
            print(menu)
            choice = int(input("enter choice : "))

            if choice == 1:
                query = "SELECT * FROM manager1"
                mycursor.execute(query)
                products = mycursor.fetchall()
                for product in products:
                    print(product)

            elif choice == 2:
                name = input("Enter friut name to search: ")
                query = "SELECT * FROM manager1 WHERE name =%s"
                args = (name,)
                mycursor.execute(query, args)
                results = mycursor.fetchall()
                if results:
                    for row in results:
                        print(row)
                else:
                    print("No friut found.")




            elif choice == 3:
                min_price = input("Enter minimum price: ")
                max_price = input("Enter maximum price: ")
                query = "SELECT * FROM manager1 WHERE price BETWEEN %s AND %s"
                args = (min_price, max_price)
                mycursor.execute(query, args)
                results = mycursor.fetchall()
                if results:
                    for row in results:
                        print(row)
                else:
                    print("No friut in this price range.")

            elif choice == 4:
                id = int(input("Enter friut ID to check availability: "))
                query = "SELECT name, quantity FROM manager1 WHERE id = %s"
                mycursor.execute(query, (id,))
                result = mycursor.fetchone()
                if result:
                    print(f"friut: {result[0]}, Quantity Available: {result[1]}")
                else:
                    print("friut not found.")

            elif choice == 5:
                print("Thank you !!")
                break

            else:
                print("Invalid choice!")

    elif choice == 3:
                print("thank you!!")
                break
    
    else:
        print("invalid choice!!")
        break

            
