# from account import Account
# from car import Car

# class Main:
#     checking = Account("You", 100)
#     saving = Account("You")
#     saving.deposit(50)
#     saving.withdraw(100)
#     saving.withdraw(25)
#     print(saving.get_balance())
#     honda = Car("Subaru", "WRX", "2000", speed = 50)
#     honda.accelerate(20)
#     honda.accelerate(40)
#     honda.brake(80)
#     honda.brake(70)

# from diary import Diary

# class Main:
#     diary = Diary()
#     print("add entry")
#     diary.add_entry("one")
#     diary.get_entries()
#     diary.unlock()
#     diary.add_entry("two")
#     diary.get_entries()

# from vehicle import Vehicle
# from vehicle import Car

# class Main:
#     my_vehicle = Vehicle("Toyota", "Corolla")
#     my_vehicle.running()
#     my_car = Car("Ford", "Mustang", 2022)
#     my_car.running()

# from bird import Bird, Sparrow, Ostrich

# bird = Bird()
# sparrow = Sparrow()
# ostrich = Ostrich()

# bird.intro()
# bird.flight()
# ostrich.intro()
# ostrich.flight()
# sparrow.intro()
# sparrow.flight()

# from person import Person, Employee, Client

# person = Person("22", "Neo")
# employee = Employee("22", "Thomas")
# client = Client("22", "Anderson")

# person.greetings()
# print(person.info())

# employee.greetings()
# employee.info()

# client.greetings()
# client.info()

from vehicleABS import Car, Motorcycle

car = Car()
motorcycle = Motorcycle()

car.start()
motorcycle.start()
