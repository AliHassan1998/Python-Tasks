# “Bank Account System” with Operator Overloading
class BankAccount:
    total_accounts = 0
    all_accounts = []

    def __init__(self, account_holder, balance, account_type, transactions=None):
        if BankAccount.validate_account_holder(account_holder):
            self.account_holder = account_holder
        else:
            raise TypeError("Error: Bank Account Holder Name must be a non-empty string.")
        if BankAccount.validate_amount(balance):
            self.balance = balance
        else:
            raise ValueError("Error: Bank Account Balance must be a non-negative float.")
        if BankAccount.validate_account_type(account_type):
            self.account_type = account_type
        else:
            raise TypeError("Error: Bank Account Type must be a non-empty string.")
        if transactions is None:
            self.transactions = {}
        else:
            self.transactions = transactions
        BankAccount.total_accounts += 1
        BankAccount.all_accounts.append(self)

    @staticmethod
    def validate_account_holder(account_holder):
        if account_holder and isinstance(account_holder, str):
            return True
        else:
            return False

    @staticmethod
    def validate_amount(amount):
        if amount >= 0.0 and isinstance(amount, float):
            return True
        else:
            return False

    @staticmethod
    def validate_account_type(account_type):
        if account_type and isinstance(account_type, str):
            return True
        else:
            return False

    def __str__(self):
        return f"Bank Account's Details: \nBank Account Holder: {self.account_holder} \n" \
               f"Bank Account Balance: ${self.balance} \nBank Account Type: {self.account_type}"

    def __repr__(self):
        return f"BankAccount('{self.account_holder}', {self.balance}, '{self.account_type}')"

    def __add__(self, other):
        if isinstance(other, BankAccount):
            return BankAccount(f"{self.account_holder} & {other.account_holder}", self.balance + other.balance, "Joint")
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, BankAccount):
            return self.balance == other.balance and self.account_type.lower() == other.account_type.lower()
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, BankAccount):
            return self.balance > other.balance
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, BankAccount):
            return self.balance < other.balance
        return NotImplemented

    def __len__(self):
        return len(self.account_holder.replace(" ", ""))

    def __call__(self, amount):
        if BankAccount.validate_amount(amount):
            self.balance += amount
            self.transactions["Deposit"] = amount
            return f"Account Balance after Deposit: {self.balance}"
        else:
            raise ValueError("Error: Depositing Amount must be a non-negative float.")

    def withdraw(self, amount):
        if amount <= self.balance:
            if BankAccount.validate_amount(amount):
                self.balance -= amount
                self.transactions["Withdraw"] = amount
                return f"Account Balance after Withdraw: {self.balance}"
            else:
                raise ValueError("Error: Withdrawing Amount must be a non-negative float.")
        else:
            return f"Oops! Not Enough Balance in Account."

    def display_all_transactions(self):
        if self.transactions:
            print("All Transaction's Details: ")
            print("--" * 30)
            for no, (key, value) in enumerate(self.transactions.items(), start=1):
                print(f"Transaction {no}: ")
                print(f"{key}: {value}")
                print("--" * 30)
            else:
                print(f"Current Balance: {self.balance}")
        else:
            print("Oops! There are no transactions to be displayed.")

    @classmethod
    def from_string(cls, string):
        try:
            account_holder, balance, account_type = string.strip().split(",")
            return BankAccount(account_holder.strip(), float(balance.strip()), account_type.strip())
        except Exception as e:
            print(f"Oops! An error occurred: {e}")

    @classmethod
    def display_all_accounts(cls):
        if cls.all_accounts:
            print("All Bank Account's Details: ")
            print("--" * 30)
            for no, account in enumerate(cls.all_accounts, start=1):
                print(f"Account {no}: ")
                print(account)
                print("--" * 30)
        else:
            print("Oops! There are no Accounts to display.")


if __name__ == "__main__":
    account1 = BankAccount("Ali", 12000.0, "Saving")
    account2 = BankAccount("Hassan", 14000.0, "Current")
    account3 = BankAccount.from_string("Sohail,16000.0,Checking")
    account4 = BankAccount.from_string("Abbas,12000.0,Saving")
    BankAccount.display_all_accounts()
    print(repr(account1))
    print(repr(account3))
    account5 = account1 + account2
    print(account5)
    print(account1 == account4)
    print(account2 < account3)
    print(account1 > account3)
    print(len(account4))
    print(f"Total Number of Bank Accounts are: {BankAccount.total_accounts}")
    print(account1(12000.0))
    print(account1.withdraw(22000.0))
    account1.display_all_transactions()
