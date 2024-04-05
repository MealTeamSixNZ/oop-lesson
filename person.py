class Person:
    def __init__(self, age, name):
        self.age = age
        self.name = name
    def info(self):
        return(self.name, self.age)
    def greetings(self):
        print(f"Hey {self.name}!")
        
    
class Employee(Person):
    def __init__(self, age, name):
        super().__init__(age, name)
    def greetings(self):
        print(f"Hello {self.name}.")

class Client(Person):
    def __init__(self, age, name):
        super().__init__(age, name)
    def info(self):
        print(f"{self.age} Mr. {self.name}")
    def greetings(self):
        print(f"Pleased to meet you Mr. {self.name}")