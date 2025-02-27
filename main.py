from car import Car
from bike import Bike
from utils import show_vehicle_info

# Creating instances
car1 = Car("Toyota", "Corolla", 2020, 50, 5)
bike1 = Bike("Yamaha", "R1", 2019, 30, 998)

# Display vehicle details
show_vehicle_info(car1)
show_vehicle_info(bike1)

# Calculate rental costs
print(f"\nRental cost for {car1.brand} {car1.model} for 3 days: ${car1.calculate_rental_cost(3)}")
print(f"Rental cost for {bike1.brand} {bike1.model} for 5 days: ${bike1.calculate_rental_cost(5)}")

# Updating rental prices
car1.set_rental_price(55)
print(f"\nUpdated rental price for {car1.brand} {car1.model}: ${car1.get_rental_price()}/day")
