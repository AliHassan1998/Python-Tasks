# Banking System with Magic Methods
class Account:
    total_accounts = 0
    all_accounts = []

    def __init__(self, name, acc_id, balance):
        self.name = name
        self.acc_id = acc_id
        self.balance = balance
        Account.total_accounts += 1
        Account.all_accounts.append(self)

    def deposit(self, amount):
        if self.validate_balance(amount):
            self.balance += amount
            return self.balance
        else:
            print("Error: Oops! The depositing amount can't be negative.")
            return None

    def withdraw(self, amount):
        if self.validate_balance(amount):
            if amount <= self.balance:
                self.balance -= amount
                return self.balance
            else:
                print("Error: Oops! Not enough balance in the account.")
                return None
        else:
            print("Error: Oops! The withdrawing amount can't be negative.")
            return None

    def __str__(self):
        return (f"Account's Details: \nAccount Holder's Name: {self.name} \n"
                f"Account ID: {self.acc_id} \nAccount Balance: {self.balance}")

    def __repr__(self):
        return f"Account('{self.name}', '{self.acc_id}', {self.balance})"

    def __eq__(self, other):
        if isinstance(other, Account):
            return self.acc_id == other.acc_id
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Account):
            return self.balance < other.balance
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, Account):
            return Account(self.name + " & " + other.name, self.acc_id + other.acc_id, self.balance + other.balance)
        return NotImplemented

    def __len__(self):
        return len(self.name)

    def __call__(self, amount):
        return self.deposit(amount)

    @classmethod
    def from_string(cls, string):
        name, acc_id, balance = string.strip().split(",")
        return cls(name, acc_id, float(balance))

    @staticmethod
    def validate_balance(balance):
        if balance >= 0:
            return True
        else:
            return False

    @classmethod
    def display_all_accounts(cls):
        if cls.all_accounts:
            print("All Account's Details: ")
            print("--" * 30)
            for no, account in enumerate(cls.all_accounts, start=1):
                print(f"Account: {no}: ")
                print(account)
                print("--" * 30)
        else:
            print("Oops! There are no accounts to display.")


class SavingsAccount(Account):
    total_savings_accounts = 0
    all_savings_accounts = []

    def __init__(self, name, acc_id, balance, interest_rate):
        super().__init__(name, acc_id, balance)
        self.interest_rate = interest_rate
        SavingsAccount.total_savings_accounts += 1
        SavingsAccount.all_savings_accounts.append(self)

    def __str__(self):
        return str(super().__str__() + f" \nAccount Interest Rate: {self.interest_rate}"
                                       f"").replace("Account", "Savings Account")

    def __call__(self, amount=None):
        if amount is None:
            self.balance = self.balance + ((self.interest_rate / 100) * self.balance)
            return self.balance
        else:
            self.deposit(amount)
            return self.balance

    def __repr__(self):
        return f"SavingsAccount('{self.name}', '{self.acc_id}', {self.balance}, {self.interest_rate})"

    def __add__(self, other):
        if isinstance(other, SavingsAccount):
            return SavingsAccount(self.name + " & " + other.name, self.acc_id + other.acc_id, self.balance + other.balance,
                                  (self.interest_rate + other.interest_rate) / 2)
        return NotImplemented

    @classmethod
    def from_string(cls, string):
        name, acc_id, balance, interest_rate = string.strip().split(",")
        return cls(name, acc_id, float(balance), float(interest_rate))

    @classmethod
    def display_all_savings_accounts(cls):
        if cls.all_savings_accounts:
            print("All Savings Account's Details: ")
            print("--" * 30)
            for no, savings_account in enumerate(cls.all_savings_accounts, start=1):
                print(f"Account: {no}: ")
                print(savings_account)
                print("--" * 30)
        else:
            print("Oops! There are no accounts to display.")


if __name__ == "__main__":
    account1 = Account("Ali", "AZ101", 12000.00)
    account2 = Account.from_string("Hassan,BY202,23000.00")
    savings_account1 = SavingsAccount("Sohail", "CX303", 34000.00, 2.5)
    savings_account2 = SavingsAccount.from_string("Abbas,DW404,45000.00,3.5")
    print(SavingsAccount.total_savings_accounts)
    print(account1)
    print(account2)
    print(savings_account1)
    print(savings_account2)
    print(repr(account1))
    print(repr(account2))
    print(repr(savings_account1))
    print(repr(savings_account2))
    print(account1.deposit(500))
    print(savings_account1.deposit(1000))
    account2.deposit(-500)
    savings_account2.deposit(-1000)
    print(account1.withdraw(500))
    print(savings_account1.withdraw(1000))
    account2.withdraw(-500)
    savings_account2.withdraw(46000)
    print(account1 == savings_account2)
    print(account2 < savings_account1)
    print(len(account1))
    print(len(savings_account1))
    print(account1(500))
    print(savings_account1())
    print(savings_account1(1000))
    Account.display_all_accounts()
    print(f"Total accounts are: {Account.total_accounts} out of which Savings accounts are: "
          f"{SavingsAccount.total_savings_accounts}.")
    SavingsAccount.display_all_savings_accounts()
    account3 = account1 + account2
    print(account3)
    savings_account3 = savings_account1 + savings_account2
    print(savings_account3)
