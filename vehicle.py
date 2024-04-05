class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    def running(self):
        print(f"{self.make} {self.model} is running")

class Car(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model)
        self.year = year
    def running(self):
        print(f"{self.year} {self.make} {self.model} is running")
        