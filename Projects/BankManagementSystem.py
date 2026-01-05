import re

class BaseClass:
    def __init__(self, account_number, account_holder, balance=0): 
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance  

    def deposit(self):
        while True:
            try:
                amount = int(input("Enter amount to deposit: "))
                if amount == 0:
                    print("NO zeroes!!")
                else:
                    self.balance += amount
                    break
            except ValueError:
                print("Accepts only Numeric input!!")

    def withdraw(self):
        while True:
            try:
                amount = int(input("Enter amount to withdraw: "))
                if amount == 0 or amount > self.balance:
                    print("Insufficient balance!!")
                else:
                    self.balance -= amount
                    print(f"{amount} has been withdrawn!")
                    break
            except ValueError:
                print("Accepts only Numeric input!!")

    def Info(self):
        print("="*50)
        print("\t\tBank")
        print("="*50)
        print(f"\nAccount holder: {self.account_holder}\nAccount Number: {self.account_number}")
        print("-"*50)
        print(f"Bank Balance: {self.balance}")
        print("-"*50)


class SavingsAccount(BaseClass):
    def __init__(self, account_number, account_holder, balance=0, interest_rate=0.05):
        super().__init__(account_number, account_holder, balance) 
        self.interest_rate = interest_rate

    def add_interest(self):
        interest_calculation = self.balance * self.interest_rate
        self.balance += interest_calculation
        print(f"Interest added: ${interest_calculation:.2f}")

    def show(self):
        print("="*60)
        print("\t\t Savings Account ")
        print("="*60)
        print(f"Account Holder : {self.account_holder}")
        print(f"Account Number : {self.account_number}")
        print(f"Current Balance: ${self.balance:.2f}")
        print(f"Interest Rate  : {self.interest_rate*100:.2f}%")
        print("-"*60)
        print("Thank you for banking with us! 🌟")
        print("="*60)


class PremiumAccount(SavingsAccount):
    def __init__(self, account_number, account_holder, cashback_rate, balance=1000, interest_rate=0.05):  
        super().__init__(account_number, account_holder, balance, interest_rate)  
        self.cashback_rate = cashback_rate

    def apply_cashback(self, amount):
        if amount > self.balance:
            print("Insufficient balance to withdraw!")
            return
        cashback = amount * self.cashback_rate
        self.balance -= (amount - cashback)
        print(f"${amount} withdrawn with ${cashback:.2f} cashback applied.")

    def show(self):  
        print("="*60)
        print("\t\t Premium Account ")
        print("="*60)
        print(f"Account Holder : {self.account_holder}")
        print(f"Account Number : {self.account_number}")
        print(f"Current Balance: ${self.balance:.2f}")
        print(f"Interest Rate  : {self.interest_rate*100:.2f}%")
        print(f"Cashback Rate  : {self.cashback_rate*100:.2f}%")
        print("-"*60)


def acc_verification(name):
    pattern = r'^[A-Z][a-z]{2,25}( [A-Z][a-z]{2,25})+$'
    if re.fullmatch(pattern, name):
        print(f"\nWelcome, {name}! Your account name is valid.\n")
        return True
    else:
        print("\nInvalid name! Make sure:")
        print("- Each words first letter starts with a capital letter")
        print("- Only letters are used")
        print("- First and last name each have 3-26 letters")
        return False


def acc_number_verification(number):
    if re.fullmatch(r'^\d{8}$', number):
        print(f"Account number {number} is valid.")
        return True
    else:
        print("\nInvalid account number! It must be exactly 8 digits.")
        return False


holder_name_input = input("Enter account holder name: ")
account_number_input = input("Enter account number: ")

if acc_verification(holder_name_input) and acc_number_verification(account_number_input):
    acc1 = BaseClass(account_number_input, holder_name_input)
    while True:
        print("\nChoose a function:")
        print("1 - Deposit")
        print("2 - Withdraw")
        print("3 - Add Interest")
        print("4 - Display Balance")
        print("5 - Create a savings acc")
        print("6 - Alice's premium acc")
        print("7 - Exit")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            acc1.deposit()
            acc1.Info()
        elif choice == 2:
            acc1.withdraw()
            acc1.Info()
        elif choice == 3:
            pass
        elif choice == 4:
            acc1.Info()
        elif choice == 5:
            saving = SavingsAccount(account_number_input, holder_name_input)
            saving.show()
        elif choice == 6:
            premium = PremiumAccount(12456789, 'Alice Smith', 0.02) 
            print("\nPremium Account Info:")
            premium.show()
            print("\nApplying interest")
            premium.add_interest()
            print("\nWithdrawing $200 with cashback:")
            premium.apply_cashback(200)
            print("\nFinal Premium Account Info:")
            premium.show()
        elif choice == 7:
            print("Exiting")
            exit()
        else:
            print("Invalid choice! Try again.")
else:
    print("Account creation failed due to invalid input.")
