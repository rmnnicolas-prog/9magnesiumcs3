class BankAccount:
def__init__(account_number, balance):
    self.__acount_number = account_number
     self.__balance = balance

def set_account_number(self, account_number):
  self._account_number = account_number

@property
def get_account_number(self):
  return self._account_number

def set_balance(self, balance):
    if balance > -1:
        self.__balance = balance
    else:
        print("The balance must not be negative")

@property
def get_balance(self):
  return self.__balance

a1 = BankAccount(45764, 1000)

print("Account 1")
print(f"Account Number: {a1.get_account_number}")
print(f"Balance: {a1.get_balance}")

print("Update balance to -100")
print(f"Account Number: {a1.get_account_number}")
print(f"Balance: {a1.get_balance}")
