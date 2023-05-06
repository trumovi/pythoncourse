class BankAccount:
    def __init__(self, owner_name, account_number, balance, password):
        self.owner_name = owner_name
        self.account_number = account_number
        self.__balance = balance
        self.__password = password

    def get_balance(self, password):
        if password == self.__password:
            return self.__balance
        else:
            return "Incorrect password"

    def set_balance(self, balance, password):
        if password == self.__password:
            self.__balance = balance
            return "Balance updated"
        else:
            return "Incorrect password"


john = BankAccount("John", 12, 22000, 1111)
print(john.get_balance(1111))
print(john.set_balance(23000, 1111))
