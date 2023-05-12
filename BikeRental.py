import csv

class color:
  PURPLE = '\033[95m'
  CYAN = '\033[96m'
  DARKCYAN = '\033[36m'
  BLUE = '\033[94m'
  GREEN = '\033[92m'
  YELLOW = '\033[93m'
  RED = '\033[91m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'
  ITALICS = '\033[3m'
  END = '\033[0m'

class BikeRental:
    def __init__(self):
        self.stock = self.read_price_from_stock()

    def read_price_from_stock(self):
        with open("stock_bikes.csv", "r") as file:
            reader = csv.reader(file)
            stock = {}
            for row in reader:
                item = row[0]
                qty = int(row[1])
                stock[item] = qty
            return stock

    def stock_to_file(self):
        with open("stock_bikes.csv", "w", newline='') as file:
            writer = csv.writer(file)
            for item, qty in self.stock.items():
                writer.writerow([item, qty])

    def rental(self, rental_type, qty):
        if rental_type not in self.stock:
            print(color.RED+ '\nSorry, this rental does not exist.'+color.END)
            return

        if qty > self.stock[rental_type]:
            print(color.RED+'\nSorry, we do not have enough bikes'+color.END)
            return

        if rental_type == 'per hour':
            cost = 5 * qty
            self.stock[rental_type] -= qty
        elif rental_type == 'per day':
            cost = 20 * qty
            self.stock[rental_type] -= qty
        elif rental_type == 'per week':
            cost = 60 * qty
            self.stock[rental_type] -= qty
        self.stock_to_file()
        print(color.BLUE+ '\nThe total cost is: '+color.END, cost)
        return cost


    def returning_bike(self):
        returning_type = input(color.PURPLE + "\nPlease select the type of bikes you would like to return\n"
                            "\nOption 1) per hour bike rental \n"
                            "\nOption 2) per hour bike rental\n"
                            "\nOption 3) per hour bike rental" + color.END)
        if returning_type == '1':
            returning_type = 'per hour bike rental'
        elif returning_type == '2':
            returning_type = 'per day bike rental'
        elif returning_type == '3':
            returning_type = 'per week bike rental'
        else:
            print(color.RED+'\nSorry. This is an invalid bike rental'+color.END)
            return

        qty = int(input("\nPlease enter how many bikes you would like to return at the shop?: " ))
        cost =None
        if returning_type not in self.stock:
            print(color.RED+'\nSorry. This is an invalid bike rental'+color.END)
            return
        if returning_type == 'per hour':
            cost = 5 * qty
        elif returning_type == 'per day':
            cost = 20 * qty
        elif returning_type == 'per week':
            cost = 60 * qty
        self.stock_to_file()

        self.stock[returning_type] += qty
        self.stock_to_file()
        if cost is not None :
            cost = self.fam_rental(qty, cost)
            print(color.BLUE+f"You rented {qty} bikes, cost you ${cost}"+color.BLUE)
            return self.stock

    def display_stock(self):
        print(color.GREEN+'\nThe current stock at the Bike Shop:\n'+color.END)
        for item, qty in self.stock.items():
            print(item, ':', qty)

    def fam_rental(self, rental_qty, rental_cost):
        if rental_qty >= 3:
            cost = rental_cost * 0.7
        else:
            cost = rental_cost

        print(color.BLUE+'The total for the discounted rental is: $'+color.END, cost)
        return cost

    def receipt(self):
        print(color.BOLD+color.ITALICS+color.PURPLE+"\nHELLO! WELCOME TO THE BIKE SHOP"+color.END)
        rental_type = input("Please select what type of bikes would you like to rent?\n"
                        "\nPlease enter option 1) for hourly bikes rental\n"
                        "\nPlease enter option 2) for daily bikes rental\n"
                        "\nPlease enter option 3) for weekly bikes rental ")
        qty = int(input("\nPlease enter how many bikes you would like to rent: "))

        if rental_type == '1':
            rental_type = 'per hour'
        elif rental_type == '2':
            rental_type = 'per day'
        elif rental_type == '3':
            rental_type = 'per week'
        else:
            print('Sorry, this retantal does not exist.')
            return

        cost = self.rental(rental_type, qty)
        if cost is not None:
            cost = self.fam_rental(qty, cost)
            print(color.BLUE+f"You rented {qty} bikes, cost you ${cost}"+color.END)


def main():
    bool = True
    bike_shop = BikeRental()
    while bool:
        customer_input = int(input("\nHello. Please select what would you like to do today?\n"
                                   "\nPlease enter option 1) for displaying bikes\n"
                                   "\nPlease enter option 2) for renting bikes\n"
                                   "\nPlease enter option 3) for returning bikes\n"
                                   "\nPlease enter option 4) to exit the bike rental service: "))
        if customer_input == 1:
            bike_shop.display_stock()
        elif customer_input == 2:
            bike_shop.receipt()
        elif customer_input == 3:
            print(color.BLUE +"\nReturning bike"+color.END)
            bike_shop.stock = bike_shop.returning_bike()

        elif customer_input == 4:
            bool = False

if __name__ == '__main__':
    main()
