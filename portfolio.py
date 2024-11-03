from datetime import datetime
def getDate(): 
    return datetime.now().strftime("%B %d, %Y")
class ItemToPurchase:
    def __init__(self, name="none", price=0, quantity=0, description="none"):
        self.name = name
        self.price = round(price, 2)
        self.quantity = quantity
        self.description = description
    
    def get_total(self):
        return self.price * self.quantity

class ShoppingCart:
    def __init__(self, customer_name="none", current_date=getDate()):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = list()


    def add_item(self, item):
        self.cart_items.append(item)

    def remove_item(self, item_name):
        found = False
        for x in self.cart_items:
            if x.name == item_name:
                self.cart_items.remove(x)
                found = True
                break
        if not found:
            print("Item not found in cart. Nothing removed.")

    def modify_item(self, item_to_modify):
        found = False
        for x in self.cart_items:
            if x.name == item_to_modify.name:
                if item_to_modify.description != "none":
                    x.description = item_to_modify.description
                if item_to_modify.price != 0:
                    x.price = item_to_modify.price
                if item_to_modify.quantity != 0:
                    x.quantity = item_to_modify.quantity
                found = True
                break
        if not found:
            print("Item not found in cart. Nothing modified.")
    def get_num_items_in_cart(self):
        total = sum(x.quantity for x in self.cart_items)
        return total
    def get_cost_of_cart(self):

        total = sum(round(x.price * x.quantity, 2) for x in self.cart_items)
        return total
    
    def print_total(self):
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
        else:
            total_cost = self.get_cost_of_cart()
            print(f"Total: ${total_cost}")
    def print_descriptions(self):
        for x in self.cart_items:
            print(f"{x.name}: {x.description}")
    

def print_menu(cart):
    while True:
        try: 
            print("\nMENU")
            print("a - Add item to cart")
            print("r - Remove item from cart")
            print("c - Change item quantity")
            print("i - Output items' descriptions")
            print("o - Output shopping cart")
            print("q - Quit")
            choice = input("Choose an option: ").lower()

            if choice == 'a':
                name = str(input("enter the item name: "))
                description = str(input("enter the item description: "))
                price = float(input("enter the item price: "))
                quantity = int(input("enter the item quantity: "))
                item = ItemToPurchase(name, price, quantity, description)
                cart.add_item(item)
            elif choice == 'r':
                name = input("enter name of item to remove: ")
                cart.remove_item(name)
            elif choice == 'c':
                name = str(input("enter the item name to modify: "))
                price = 0
                quantity = int(input("enter the new quantity (enter 0 to keep current quantity): "))
                description = "none"
                item = ItemToPurchase(name, price, quantity, description)
                cart.modify_item(item)
            elif choice == 'i':
                print("Item Descriptions")
                cart.print_descriptions()
            elif choice == 'o':
                
                print(f"{cart.customer_name}'s Shopping Cart - {cart.current_date}")
                print(str("Number of Items: " + str(cart.get_num_items_in_cart())))
                for x in cart.cart_items: 
                    print(f'{x.name} {x.quantity} @ ${x.price} = ${x.get_total()}')
                cart.print_total()

            elif choice == 'q':
                print("Quitting menu.")
                return 
            else:
                print("Invalid option. Please choose again.")
        except KeyboardInterrupt:
            return 
        except Exception as e:
            print(str(e)) 
            pass 
            



def main():
    customer_name = input("Enter customer name: ")
    customer_date = input("enter todays date")
    print("Customer Name: " + customer_name)
    print("Today's Date" + customer_date)
    date = getDate() # like anyone could really figure out the date
    cart = ShoppingCart(customer_name, date)
    print_menu(cart)

if __name__ == "__main__":
    main()

        