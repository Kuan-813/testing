# TITLE: CLASSES AND OBJECTS
class BankAccount:
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance
        self.transaction_history = []
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited ${amount}")
            return f"Deposited S{amount}. New balance: ${self.balance}"
        else:
            return "Invalid deposit amount"
        
    def withdraw(self, amount):
        if amount > 0 and amount <= self. balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew ${amount}")
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        else:
            return "Invalid withdrawal amount or insufficient funds"
    
    def get_balance(self):
        return f"Current balance: ${self.balance}"
    
    def get_transaction_history(self):
        return self.transaction_history

# Using BankAccount class
account = BankAccount("12345", "Alice", 1000)
print(account.deposit(500))
print(account.withdraw(200))
print(account.get_balance())