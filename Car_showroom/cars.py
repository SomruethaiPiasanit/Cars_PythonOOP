class Car:

    # class attribute
    suv = "SUV Car"
    sedan = "Sedan Car"
    hatchback = "Hatchback Car"

    # instance attribute
    def __init__(self, name, price, color, year):
        self.name = name
        self.price = price
        self.color = color
        self.year = year


# instantiate the Parrot class
toyota = Car("Toyota", "1000000", "Red", 2016)
mazda = Car("Mazda", "1100000", "Black", 2018)
honda = Car("Honda", "900000", "White", 2019)

# access the class attributes
print("Toyota is a {}".format(toyota.__class__.hatchback))
print("Mazda is a {}".format(mazda.__class__.sedan))
print("Honda is also {}".format(honda.__class__.sedan))

# access the instance attributes
print("{} price {} Baht".format(toyota.name, honda.price))
print("{} price {} Baht".format(mazda.name, mazda.price))
print("{} price {} Baht".format(honda.name, honda.price))
