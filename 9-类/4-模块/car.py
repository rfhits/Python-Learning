class Car():
    """
    docstring
    """

    def __init__(self, model, year):
        """
        init a car
        """
        self.model = model
        self.year = year

    def info(self):
        """
        describe the car
        """
        print("model: " + self.model)
        print("year " + str(self.year))


class Battery():
    """
    a battery for car
    """

    def __init__(self, size, capacity):
        self.size = size
        self.capacity = capacity

    def info(self):
        print("this battery's info:")
        print('size: '+str(self.size))
        print('capacity: ' + str(self.capacity))


class ElecCar():
    def __init__(self, year, model):
        """
        init a electric car
        """
        super.__init__(year, model)

        
