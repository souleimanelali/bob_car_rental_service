class Vehicle:
    def __init__(self, brand, model, year, rental_price_per_day):
        self.brand = brand
        self.model = model
        self.year = year
        self.__rental_price_per_day = rental_price_per_day  # Private attribute

    def display_info(self):
        print(f"{self.brand} {self.model}, Year: {self.year}, Rental Price: ${self.__rental_price_per_day}/day")

    def calculate_rental_cost(self, days):
        return days * self.__rental_price_per_day

    def get_rental_price(self):
        return self.__rental_price_per_day

    def set_rental_price(self, new_price):
        if new_price > 0:
            self.__rental_price_per_day = new_price
        else:
            print("Invalid price. It must be greater than zero.")
