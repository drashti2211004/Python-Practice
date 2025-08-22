# print("drashti Patel")
# print("drashti")


class Inventory():
    def _init_(self):
        
        self.items = {
            'banana': {'price': 100, 'quantity': 0},
            'mango': {'price': 210, 'quantity': 0},
            'apple': {'price': 70, 'quantity': 0}
        }


    def manager_update(self):
        print("\n--- Manager Stock Update ---")
        name = input("Enter product name: ")
        quantity = int(input("Enter quantity to add/update: "))
        price = int(input("Enter new price: "))

        if name in self.items:
            self.items[name]['quantity'] += quantity
            self.items[name]['price'] = price
        else:
            self.items[name] = {'price': price, 'quantity': quantity}

        print(f"{name} stock updated successfully!")

    # User buys product
    def user_buy(self):
        print("\n--- User Buy Product ---")
        name = input("Enter product name: ")
        if name not in self.items:
            print("Product not available!")
            return

        quantity = int(input("Enter quantity to buy: "))

        if quantity > self.items[name]['quantity']:
            print("Not enough stock!")
        else:
            self.items[name]['quantity'] -= quantity
            total_price = self.items[name]['price'] * quantity
            print(f"You bought {quantity} {name}(s) for {total_price}.")
            percentage = (quantity / self.items[name]['quantity'] ) * 100
            # High demand price increase
            if percentage >= 80:
                self.items[name]['price'] *= 1.10
                print(f"High demand! {name} price increased by 10%.")

   
    def display_inventory(self):
        print("\n-- Current Inventory ---")
        for name, details in self.items.items():
            print(f"{name}: ${details['price']} | Stock: {details['quantity']}")



obj = Inventory()

while True :
    print("press 1 for manager login!!")
    print("press 2 for user login!! ")
    print("press 3 for display inventory!!")
    print("press 4 for exit!!")


    choice = int(input("enter choice :"))
    if choice == 1 :
        
        while True :
            menu = """
                    press 1 for update stock
                    press 2 for display inventory
                    press 3 for exit

                    """
            

            print(menu)
            choice1 =int(input("enter choice : "))
            if choice1 == 1 :
                obj.manager_update()

            elif choice1 == 2 :
                obj.display_inventory()

            elif choice == 3:
                obj.display_inventory()
                
            else :
                print("invalid choice!!")
                break            



    elif choice == 2 :
        obj.user_buy()

    elif choice == 3:
        print(obj.display_inventory())

    elif choice == 4:
        print("thank you!!")
        break

    else:
        print("invalid choice!!")
        break