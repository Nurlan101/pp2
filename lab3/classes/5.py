class Account:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount  #add deposit to the balance
        print(f"Deposit of ${amount} successful. New balance: ${self.balance}")
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal of ${amount} successful. New balance: ${self.balance}")
        else:
            print("Insufficient funds. Withdrawal failed.")

acnt = Account(owner="John Doe", balance=1000)
acnt.deposit(500)
acnt.withdraw(200)  
acnt.withdraw(800)