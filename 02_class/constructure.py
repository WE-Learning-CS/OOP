class Coffee:
  def setdata(self, water, shot):
    self.water = water
    self.shot = shot
    
  def customize(self, ingredient):
    return self.water + self.shot + self.ingredient


latte = Coffee()
latte.customize('milk') # AttributeError: 'Coffee' object has no attribute 'water'

class Coffee2:
    def __init__(self, water, shot):
        self.water = water
        self.shot = shot

    def customize(self, ingredient):
        return self.water + self.shot + self.ingredient

latte2 = Coffee2() # TypeError: __init__() missing 2 required positional arguments: 'water' and 'shot'
latee3 = Coffee2(200, 2)