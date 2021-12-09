class Car:
    def __init__(self, model, price, color):
        self.model = model
        self.price = price
        self.color = color

    def drive(self, speed):
        if speed > 100:
            return "SPEEDING VIOLATION"
        else:
            return "DRIVE CAREFULLY"