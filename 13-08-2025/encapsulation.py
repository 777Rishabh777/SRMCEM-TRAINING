# class BankAccount:
#     account_counter = 1001 


#     def __init__(self, account_holder, balance=0):
#         self.account_holder = account_holder
#         self.balance = balance
#         self.account_number = BankAccount.account_counter
#         BankAccount.account_counter += 1 


#     def get_account_info(self):
#         return f"Account Holder: {self.account_holder}, Account Number: {self.account_number}, Balance: ₹{self.balance}"

#     def get_balance(self):
#         return self.balance

#     def deposit_balance(self, amount):
#         if amount > 0:
#             self.balance += amount
#             print(f"₹{amount} deposited successfully!")
#         else:
#             print("Deposit amount must be positive.")

# o1 = BankAccount("Rishabh Singh", 5000)
# o2 = BankAccount("Amit Kumar", 10000)

# print(o1.get_account_info())
# print(o2.get_account_info())


# o1.deposit_balance(2000)
# print(o1.get_account_info())

# print(o1.get_account_info())

class parent:
    def __init__(self):
        self.name = name
        print("parent__init__called")

p1 =parent("kailash")