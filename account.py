class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance
    def deposit(self, amount):
        self.__balance += amount
        print(f"Added {amount} added to the balance")
    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount
            print(f"Withdrew {amount} from the balance")
    def get_balance(self):
        return self.__balance