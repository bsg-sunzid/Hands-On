class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self._account_type = "saving"
        self.__balance = balance
    
    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}, new balance {self.__balance}")
    
    def withdraw(self, amount):
        if amount < 0:
            print("Not possible")
        elif amount > self.__balance:
            print("Over amount")
        else:
            self.__balance -= amount
            print(f"withdrawal {amount}, new balance {self.__balance}")
    def get_balance(self):
        return self.__balance

account = BankAccount("BoB", 1000)
print(account.owner)
print(account._account_type)
print(account.get_balance())

account.deposit(50)
account.withdraw(20)