# import system.os
class Car():
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.meter = 0

    def put_info(self):
        print("brand: " + self.brand + ", " +
              "model: "+self.model + ", "+"made in " + str(self.year))

    def fill_gas_tank(self):
        print("is filling the gas tank now")
        print('done')


class ElecCar(Car):
    """ ElecCar """

    def __init__(self, brand, model, year):
        # Car.__init__(self, brand, model, year)
        super().__init__(brand, model, year)

    def fill_gas_tank(self):
        print("ElecCar need to be charged")


my_car = ElecCar('tesla', 'S', '2020')
my_car.put_info()
my_car.fill_gas_tank()
print("There is gas car")
his_car = Car('BMW', 'T', '2019')
his_car.fill_gas_tank()
