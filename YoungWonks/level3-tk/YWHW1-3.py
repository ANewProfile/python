from random import randint

class BankAccount:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds")
    
    def get_balance(self):
        return self.balance


alice = BankAccount(randint(1, 1000000000000000), 'Alice', 1000)
bob = BankAccount(randint(1, 1000000000000000), 'Bob', 2000)

alice.deposit(500)
bob.withdraw(1000)
alice.withdraw(2000)

print(f'Alice: ${alice.get_balance()}')
print(f'Bob: ${bob.get_balance()}')