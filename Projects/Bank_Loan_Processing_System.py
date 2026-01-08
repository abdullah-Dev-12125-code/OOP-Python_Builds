class Customer:
    def __init__(self, name, account_number, balance, age):
        self.name = name
        self.age = age
        self.account_number = account_number
        self.balance = balance


class LoanApplication:
    def __init__(self, customer, loan_amount):
        self.customer = customer
        self.loan_amount = loan_amount

    def Apply_for_loan(self):
        if self.loan_amount < 0:
            print("\t\tLOAN APPLICATION SYSTEM")
            print("A negative integer can't be a loan amount")

        elif self.customer.age < 18:
            print("\t\tLOAN APPLICATION SYSTEM")
            print(f"{self.customer.name}, To apply for loan you must be 18 years old")

        elif self.loan_amount >= self.customer.balance * 2:
            print("\t\tLOAN APPLICATION SYSTEM")
            print(f"{self.customer.name}, The loan is a lot more than you own")

        else:
            print("\t\tLOAN APPLICATION SYSTEM")
            print(f"{self.customer.name}, You are applicable for taking loan")


alice = Customer("Alice", 4821, 5000, 25)
alice_loan = LoanApplication(alice, 9000)
alice_loan.Apply_for_loan()
print() 

bob = Customer("Bob", 9374, 3000, 17)
bob_loan = LoanApplication(bob, 4000)
bob_loan.Apply_for_loan()
print()

charlie = Customer("Charlie", 9374, 2000, 30)
charlie_loan = LoanApplication(charlie, 5000)
charlie_loan.Apply_for_loan()
print()

david = Customer("David", 7263, 40, 40)
david_loan = LoanApplication(david, -1000)
david_loan.Apply_for_loan()
