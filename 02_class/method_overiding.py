class Calculator:
    def __init__(self, first, second):
        self.first  = first
        self.second = second
    
    def div(self):
        return self.first / self.second

# a = Calculator(4, 0)
# a.div()

class OveridedCalculator(Calculator):
    def div(self):
        return 0 if self.second == 0 else self.first / self.second

b = OveridedCalculator(4, 0)
b.div()