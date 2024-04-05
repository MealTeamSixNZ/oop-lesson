class Bird:
    def intro(self):
        print("There are many types of birds.")
    def flight(self):
        print("Most of the birds can fly but some cannot.")
    
class Sparrow(Bird):
    def intro(self):
        print("This is Sammy the Sparrow.")
    def flight(self):
        print("Sparrows can fly.")
    
class Ostrich(Bird):
    def flight(self):
        print("Ostriches cannot fly.")