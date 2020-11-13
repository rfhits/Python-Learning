class dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title()+" is sitted")

    def roll(self):
        print(self.name.title() + " is now rolling over")

    def minus_age(self):
        self.age = self.age - 1


dog1 = dog('abc', 11)
# dog1.sit()
dog1.minus_age()
print(dog1.age)
