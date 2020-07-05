"""
Imagine you are designing a banking application. What would a
customer look like? What attributes would she have? What methods
would she have?
"""


class Customers:
    def __init__(self, full_name, email_address, contact_number, account_number, account_type, balance,):
        self.full_name = full_name
        self.email_address = email_address
        self.contact_number = contact_number
        self.account_number = account_number
        self.account_type = account_type
        self.balance = balance

    def amount_deposit(self):
        amount = float(input("Enter the amount you want to deposited: "))
        self.balance += amount
        print("\n Deposited Amount:", amount)
        print("\n New Balance=", self.balance)

    def amount_withdraw(self):
        amount = float(input("Enter the amount you want to withdrawn: "))
        if self.balance >= amount:
            self.balance -= amount
            print("\n Withdrew Amount:", amount)
        else:
            print("\n Insufficient balance  ")
        print("\n New Balance=", self.balance)

    def display(self):
        print("\n Account Holder Name =", self.full_name, )
        print("Email Address : ", self.email_address, "\t Contact Number : ", self.contact_number)
        print("\n Account Number=", self.account_number, "\t\t Account Type : ", self.account_type)
        print("\n Net Available Balance=", self.balance)


customer_details = Customers('Bhim Bahadur Rana', 'bhim20@gmail.com', '+977-9805823476', '009823801', 'Saving', 3000)
print("Welcome To ABC Bank!")
print("Please select -\n 1. To Deposit\n 2. To Withdraw \n 3.View Account Details")

select = int(input("Select operations form 1, 2, 3:"))

if select == 1:
    customer_details.amount_deposit()
elif select == 2:
    customer_details.amount_withdraw()
elif select == 3:
    customer_details.display()
else:
    print("Invalid input! Please select valid operation and try again!!")