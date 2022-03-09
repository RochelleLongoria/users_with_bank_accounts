class BankAccount:
    Rate = 0
    Bal = 0
    
    def __init__(self, int_rate, balance): 
        self.Rate = int_rate
        self.Bal = balance
        
    def deposit(self, amount):
        self.Bal = self.Bal + amount
    def withdraw(self, amount): 
        self.Bal = self.Bal - amount
    def display_account_info(self):
        print(self.Bal)
    def yield_interest(self):
        print(self.Rate)


class User:
    account

    def __init__(self, rate, bal):
    self.account = BankAccount(rate, bal)

    def make_deposit(self, amount):
        self.account.deposit(amount)

    def display_user_balance(self):
        self.account.display_account_info()

    def make_withdraw(self, amount):
        self.account.withdraw(amount)   


Roch = User(10,8000)
Roch.make_deposit(1005)
Roche.make_withdraw(88)
Nico = User(7, 245)
Nico.make_withdraw(136)
Nico.make_deposit(355)