'''
Carson Harbin
Programming Exercise 9
This program creates a class that is a template to be called in the main function and filled in with bank information.
'''


class BankAcct:
    def __init__(self, name, account_number, amount, interest_rate):
        self.name = name
        self.account_number = account_number
        self.amount = amount
        self.interest_rate = interest_rate

    def adjust_interest_rate(self, new_rate):
        self.interest_rate = new_rate

    def deposit(self, amount):
        if amount > 0:
            self.amount += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.amount:
            self.amount -= amount
            return True
        return False

    def get_balance(self):
        return self.amount

    def calculate_interest(self, days):
        return self.amount * (self.interest_rate / 100) * (days / 365)

    def __str__(self):
        return f"Account Holder: {self.name}\nAccount Number: {self.account_number}\nBalance: ${self.amount:.2f}\nInterest Rate: {self.interest_rate:.2f}%"


def test_bank_acct():
    acct = BankAcct("Carson Harbin", "12345678", 1000.0, 2.5)
    print(acct)

    acct.deposit(500)
    print("After deposit of $500:", acct.get_balance())

    acct.withdraw(300)
    print("After withdrawal of $300:", acct.get_balance())

    interest = acct.calculate_interest(30)
    print(f"Interest for 30 days: ${interest:.2f}")

    acct.adjust_interest_rate(3.0)
    print("After adjusting interest rate:", acct)

    interest = acct.calculate_interest(30)
    print(f"New interest for 30 days: ${interest:.2f}")


if __name__ == "__main__":
    test_bank_acct()
