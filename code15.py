class BankAccount:
    
    # 1. Class Attribute: Shared across ALL bank accounts
    bank_name = "Python National Bank"
    
    # 2. Constructor / Instance Attributes (Unique to each account)
    def __init__(self, owner_name, initial_balance=0.0):
        self.owner = owner_name
        self.balance = initial_balance
        print(f"Account created for {self.owner} at {self.bank_name}.")

    # 3. Instance Methods (Actions the object can take)
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"[{self.owner}] Deposited ₹{amount}. New balance: ₹{self.balance}")
        else:
            print("Deposit amount must be greater than zero.")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"[{self.owner}] Transaction failed: Insufficient funds!")
        elif amount <= 0:
            print("Withdrawal amount must be greater than zero.")
        else:
            self.balance -= amount
            print(f"[{self.owner}] Withdrew ₹{amount}. Remaining balance: ₹{self.balance}")

    # 4. Magic Method (Dunder Method)
    # This determines what gets returned when you print() the object directly
    def __str__(self):
        return f"🏦 {self.bank_name} | Owner: {self.owner} | Balance: ₹{self.balance}"


print("--- Opening Accounts ---")
# Create two separate account objects
account1 = BankAccount("Rohan", 5000)
account2 = BankAccount("Priya", 10000)

print("\n--- Performing Transactions ---")
# Rohan deposits money
account1.deposit(2000)

# Priya tries to withdraw too much, then withdraws a valid amount
account2.withdraw(15000)
account2.withdraw(3000)

print("\n--- Viewing Account Summaries ---")
# Thanks to the __str__ method, we can just print the objects directly!
print(account1)
print(account2)