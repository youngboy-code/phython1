class Car:
    def __init__(self, make, model, year):
        self.__make = make
        self.__model = model
        self.__year = year
        self.__mileage = 0

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def get_mileage(self):
        return self.__mileage

    def drive(self, miles):
        self.__mileage += miles


# Usage:
my_car = Car("Toyota", "Camry", 2020)
print(my_car.get_make())  # Output: Toyo
print(my_car.get_mileage())  # Output: 0

my_car.drive(100)
print(my_car.get_mileage())  # Output: 100https://github.com/logout