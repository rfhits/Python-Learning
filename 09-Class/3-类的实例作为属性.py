class Car():

    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def puts_info(self):
        print("brand: " + self.brand + "\n"
              "made in: " + str(self.year))


class Battery():
    def __init__(self, size=70):
        self.size = size

    def puts_range(self):
        print("this car can run 140 km")


class ElecCar(Car):
    def __init__(self, brand, year):
        super().__init__(brand, year)
        self.battery = Battery(100)


car1 = ElecCar('Telsa', 2020)
# car1.puts_info()
car1.battery.puts_range()
