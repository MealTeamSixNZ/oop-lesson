from abc import ABC, abstractmethod

class VehicleABS(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(VehicleABS):
    def start(self):
        print("The car engine starts with a key.")

class Motorcycle(VehicleABS):
    def start(self):
        print("The motorcylce starts with the ignition button.")
        