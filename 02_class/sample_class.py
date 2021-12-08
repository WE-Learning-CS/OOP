class Car:
  def __init__(self, model, color, year):
    self.model = model
    self.color = color
    self.year  = year
    
  def drive(self, speed):
    if speed != 0:
      return f'The speed of the car is {speed}.'
    
  def stop(self):
    return "The car has stopped."
    
first_car  = Car("k5", "black", 2021)
second_car = Car("seltos", "white", 2021)

first_car.drive(100)
second_car.stop()