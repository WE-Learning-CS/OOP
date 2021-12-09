class Event(list):
    def __call__(self, *args, **kargs):
        for f in self:
            f(*args, **kargs)

class Child():
    anger = Event()
    happy = Event()
    def bad(self):
        self.anger('hungry')
        self.anger('sleepy')
        self.anger('thirsty')
    def good(self):
        self.happy("good")

class Father():
    def care(self, situation):
        print('care %s' % situation)

c = Child()
f = Father()
c.anger.append(f.care)
c.happy.append(f.care)
c.bad()
c.good()