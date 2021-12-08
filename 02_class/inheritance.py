from sample_class import Car

class Truck(Car):
    def __init__(self, name):
        self.name = name

    def load(self, baggage):
        return f"Loaded {baggage} into the truck."

truck = Truck("Poter")
truck.drive(100)  # The speed of the car is 100.
truck.stop()      # The car has stopped.
truck.load("box") # Loaded box into the truck.