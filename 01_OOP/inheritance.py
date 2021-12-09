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

class Taxi(Car):
    def take_passengers(self, passengers):
        if passengers > 4:
            return "5명 이상 못 탐"
        else:
            return "출발~"

taxi1 = Taxi("기아", "3,000만원", "orange")
print(taxi1.take_passengers(7)) 
# 5명 이상 못 탐

print(taxi1.drive(120))
# SPEEDING VIOLATION