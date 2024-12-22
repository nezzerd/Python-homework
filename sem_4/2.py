class BankAccount:
    def __init__(self, initial_balance=0, interest_rate=0):
        self.__balance = initial_balance
        self.__interest_rate = interest_rate
        self.__transactions = []

    def deposit(self, cash):
        self.__balance += cash
        self.__transactions.append(f"Депозит: {cash}")
        print(f"Депозит: {cash} успешно внесен.")

    def withdraw(self, cash):
        if self.__balance >= cash:
            self.__balance -= cash
            self.__transactions.append(f"Снятие: {cash}")
            print(f"Снято: {cash}")
        else:
            print("Недостаточно средств.")

    def get_balance(self):
        return self.__balance

    def add_interest(self):
        interest = self.__balance * (self.__interest_rate / 100)
        self.__balance += interest
        self.__transactions.append(f"Добавлены проценты: {interest:.2f}")
        print(f"Проценты добавлены: {interest:.2f}")

    def history(self):
        print("История транзакций:")
        for transaction in self.__transactions:
            print(transaction)


account = BankAccount(100, 5)
account.deposit(50)
account.withdraw(20)
account.add_interest()
print(account.get_balance())
account.history()
