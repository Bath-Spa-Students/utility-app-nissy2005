# BATHSPA VENDING MACHINE

class VendingMachine:
    def __init__(self):
        # Define the items available in the vending machine
        self.items = {
            "1": {"name": "Pepsi", "price": 1.25},
            "2": {"name": "Mountain Dew", "price": 1.25},
                          "3" : {"name" : "Sprite", "price": 1.25 },
                          "4" : {"name" : "Fanta", "price": 1.25 },
                          "5" : {"name" : "Mango Fresh Juice", "price": 5 },
                          "6" : {"name" : "Water", "price": 0.75 },
                          "7" : {"name" : "Wafers", "price": 3.50 },
                          "8" : {"name" : "Snickers", "price": 2.50 },
                           "9" : {"name" : "m$ms", "price": 2.25 },
                           "10" : {"name" : "ChupaChups Lollipop", "price": 1.25 },
                           "11" : {"name" : "Twix", "price": 2.25 },
                           "12" : {"name" : "Bounty", "price": 2.25 },
                           "13" : {"name" : "Maltesers", "price": 2.50 },
                           "14" : {"name" : "CupCake", "price": 4.00 },
                           "15" : {"name" : "Doritos", "price": 1.25 },
                           "16" : {"name" : "Lays", "price": 2.25 },
                           "17" : {"name" : "Bugles", "price": 2.25 },
                           "18" : {"name" : "Oman Chips", "price": 2.25 },
                           "19" : {"name" : "Cheetos", "price": 4.25 },
                           "20" : {"name" : "Sohar Chips", "price": 2.25 },
            "21": {"name": "Exit", "price": 0}
        }
        # Initialize the balance and selected items
        self.balance = 0
        self.selected_item = None

    def display_menu(self):
        print("\nWelcome to the Vending Machine!")
        for key, item in self.items.items():
            print(f"{key}. {item['name']} - ${item['price']:.2f}")


    def user_choice(self):
        while True:
            code = input("Enter the number of your choice: ")
            if code in self.items:
                return code
            else:
                print("Invalid choice. Please select a valid option.")

    def payment_process(self):
        while True:
            try:
                amount_inserted = float(input("Insert money (in dollars): $"))
                if amount_inserted >= 0:
                    return amount_inserted
                else:
                    print("Invalid amount.")
            except ValueError:
                print("Invalid input. Please enter a valid amount.")

    def dispense_item(self):
        item = self.items[self.selected_item]
        print(f"Dispensing {item['name']}. Enjoy your purchase!")

    def run_vending_machine(self):
        while True:
            self.display_menu()
            self.selected_item = self.user_choice()

            if self.selected_item == "21":
                print("Thank you for using our vending machine. Have a Nice Day!")
                break

            selected_item_info = self.items[self.selected_item]
            print(f"Selected item: {selected_item_info['name']} - ${selected_item_info['price']:.2f}")

            self.balance = self.payment_process()

            if self.balance >= selected_item_info['price']:
                change = self.balance - selected_item_info['price']
                print(f"Your change is: ${change:.2f}")
                self.dispense_item()
                self.balance = 0  # Reset balance after purchase
            else:
                print("Due to insufficient amount, transaction is cancelled.")

# Create an instance of the VendingMachine class and run the vending machine
if __name__ == "__main__":
    vending_machine = VendingMachine()
    vending_machine.run_vending_machine()
