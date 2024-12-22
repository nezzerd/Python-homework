class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance

    def deposit(self, cash):
        self.__balance += cash
        print(f"Депозит: {cash} успешно внесен.")

    def withdraw(self, cash):
        if self.__balance >= cash:
            self.__balance -= cash
            print(f"Снято: {cash}")
        else:
            print("Недостаточно средств.")

    def get_balance(self):
        return self.__balance


account = BankAccount(100)
print(account.get_balance())

account.deposit(50)
print(account.get_balance())

account.withdraw(50)
print(account.get_balance())
