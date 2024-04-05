class Car:
    def __init__(self, make, model, year, maxSpeed=100, speed=0):
        self.make = make
        self.model = model
        self.year = year
        self.maxSpeed = maxSpeed
        self.speed = speed
    def accelerate(self, amount):
        if amount + self.speed > self.maxSpeed:
            print(f"too fast")
        else:
            self.speed += amount
            print(f"{self.speed}")
    def brake(self, amount):
        if self.speed - amount >= 0:
            self.speed -= amount
            print(f"new speed is {self.speed}")
        else:
            print(f"too slow")
    def get_speed(self):
        return self.speed