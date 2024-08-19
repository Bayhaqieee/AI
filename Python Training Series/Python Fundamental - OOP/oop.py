class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = []
        self.expenses = []

    def add_income(self, amount, description):
        self.incomes.append({"amount": amount, "description": description})

    def add_expense(self, amount, description):
        self.expenses.append({"amount": amount, "description": description})

    def total_income(self):
        return sum(income['amount'] for income in self.incomes)

    def total_expense(self):
        return sum(expense['amount'] for expense in self.expenses)

    def account_balance(self):
        return self.total_income() - self.total_expense()

    def account_info(self):
        return (f"Account Holder: {self.firstname} {self.lastname}\n"
                f"Total Income: ${self.total_income()}\n"
                f"Total Expenses: ${self.total_expense()}\n"
                f"Account Balance: ${self.account_balance()}\n")

account = PersonAccount("John", "Doe")

account.add_income(10000, "Salary")
account.add_income(500, "Freelance")

account.add_expense(1500, "Rent")
account.add_expense(200, "Groceries")
account.add_expense(4000, "Bills")

print(account.account_info())
