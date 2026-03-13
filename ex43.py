

class bankAccount():
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def withdraw(self, amount):

        self.balance = self.balance-amount

    def deposit(self, amount):

        self.balance = self.balance+amount