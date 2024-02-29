#Assigment: We are given a code block containing variables' and methods' declarations. Create a class named "PersonBalance" and move declarations to the inside of the class. "name" & "balance" properties values should be set using arguments of the constructor. Make sure to create an object of "PersonBalance" class & call method "display_balance()"
name = "John"
balance = 0

def display_balance():
  print(f'Name: {name}, Balance: {balance}')

display_balance()
#We make sure to declare a constructor inside the class PersonBalance and Constructor should contain three parameter named: "self", "name", "balance".
class PersonBalance:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def display_balance(self):
        print(f'Name: {self.name}, Balance: {self.balance}')

# Initial values
name = "John"
balance = 0

# Creating an object of the PersonBalance class
person = PersonBalance(name, balance)

# Calling the display_balance method
person.display_balance()
#Make class "PersonBalance" properties "name" & "balance" private. Introduce a new public method named "deposit" that takes in 2 arguments: "self" & "amount". If the given "amount" is a positive number then the amount should be added to "balance" and a string displaying the deposited amount and new "balance" returned. If the given "amount" is a negative number or zero then string "Deposit amount should be greater than zero." should be returned.
class PersonBalance:
    def __init__(self, name, balance):
        self.__name = name
        self.__balance = balance

    def display_balance(self):
        print(f'Name: {self.__name}, Balance: {self.__balance}')

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f'Deposited amount: {amount}, New Balance: {self.__balance}'
        else:
            return 'Deposit amount should be greater than zero.'

# Initial values
name = "John"
balance = 0

# Creating an object of the PersonBalance class
person = PersonBalance(name, balance)

# Calling the display_balance method
person.display_balance()

# Depositing some amount
result = person.deposit(500)
print(result)

# Attempting to deposit a non-positive amount
result = person.deposit(-20)
print(result)
#The making-of-a-deposit rules have changed. Each deposit's amount has to go through these rules: Each deposition transaction has a price: 1 and 5% of the deposit's (after transaction price deduction) sum goes to savings account balance
class PersonBalance:
    def __init__(self, name, balance, savings_balance=0):
        self.__name = name  # Private property
        self.__balance = balance  # Private property
        self.__savings_balance = savings_balance  # Private property

    def display_balance(self):
        print(f'Name: {self.__name}, Balance: {self.__balance}, Savings Balance: {self.__savings_balance}')

    def deposit(self, amount):
        if amount > 0:
            transaction_price = 1
            total_amount = amount - transaction_price
            savings_amount = total_amount * 0.05

            self.__balance += total_amount - savings_amount
            self.__savings_balance += savings_amount

            return f'Deposited amount: {amount}, New Balance: {self.__balance}, Savings Balance: {self.__savings_balance}'
        else:
            return 'Deposit amount should be greater than zero.'

# Initial values
name = "John"
balance = 0

# Creating an object of the PersonBalance class
person = PersonBalance(name, balance)

# Calling the display_balance method
person.display_balance()

# Depositing some amount
result = person.deposit(100)
print(result)

# Attempting to deposit a non-positive amount
result = person.deposit(-50)
print(result)

#we are creating a private method "__apply_deposit_transaction_fee" that applies transaction fee on a given amount. we are creating a private method "__apply_savings_account_deduction" that calculates what is 5% of a given amoun. We should make sure to test these methods (call methods and print results) (name mangling)
class PersonBalance:
    def __init__(self, name, balance, savings_balance=0):
        self.__name = name  # Private property
        self.__balance = balance  # Private property
        self.__savings_balance = savings_balance  # Private property

    def display_balance(self):
        print(f'Name: {self.__name}, Balance: {self.__balance}, Savings Balance: {self.__savings_balance}')

    def deposit(self, amount):
        if amount > 0:
            total_amount = self.__apply_deposit_transaction_fee(amount)
            savings_amount = self.__apply_savings_account_deduction(total_amount)

            self.__balance += total_amount - savings_amount
            self.__savings_balance += savings_amount

            return f'Deposited amount: {amount}, New Balance: {self.__balance}, Savings Balance: {self.__savings_balance}'
        else:
            return 'Deposit amount should be greater than zero.'

    def __apply_deposit_transaction_fee(self, amount):
        transaction_fee = 1
        return amount - transaction_fee

    def __apply_savings_account_deduction(self, amount):
        return amount * 0.05

# Initial values
name = "John"
balance = 0

# Creating an object of the PersonBalance class
person = PersonBalance(name, balance)

# Calling the display_balance method
person.display_balance()

# Depositing some amount
result = person.deposit(100)
print(result)

# Testing the private methods
amount_before_fee = 50
fee_applied = person._PersonBalance__apply_deposit_transaction_fee(amount_before_fee)
print(f'Amount before fee: {amount_before_fee}, Amount after fee: {fee_applied}')

amount_before_deduction = 100
deduction_applied = person._PersonBalance__apply_savings_account_deduction(amount_before_deduction)
print(f'Amount before deduction: {amount_before_deduction}, Deduction applied: {deduction_applied}')

#Create a protected property "_sum_of_deposit_transaction_fees" that stores sum of transaction fees. Make sure that this property's value is adjusted when person makes a deposit. Create a private property "__savings_account_balance" that stores sum of savings. Make sure that this property's value is adjusted when person makes a deposit. Apply transaction fee & savings account deduction for each deposit that a person makes.Adjust the "display_balance" method to print also "_sum_of_deposit_transaction_fees" & "__savings_account_balance". Test the updated "deposit" & "display_balance" methods. If person's balance is 0 and he or she makes a deposit of 101, then the result should be:
class PersonBalance:
    def __init__(self, name, balance=0, savings_balance=0, sum_of_deposit_transaction_fees=0):
        self.__name = name  # Private property
        self.__balance = balance  # Private property
        self.__savings_balance = savings_balance  # Private property
        self._sum_of_deposit_transaction_fees = sum_of_deposit_transaction_fees  # Protected property

    def display_balance(self):
        print(f'Name: {self.__name}, Balance: {self.__balance}, Savings Balance: {self.__savings_balance}, '
              f'Sum of Deposit Transaction Fees: {self._sum_of_deposit_transaction_fees}')

    def deposit(self, amount):
        if amount > 0:
            total_amount = self.__apply_deposit_transaction_fee(amount)
            savings_amount = self.__apply_savings_account_deduction(total_amount)

            self.__balance += total_amount - savings_amount
            self.__savings_balance += savings_amount
            self._sum_of_deposit_transaction_fees += 1

            return f'Deposited amount: {amount}, New Balance: {self.__balance}, ' \
                   f'Savings Balance: {self.__savings_balance}, ' \
                   f'Sum of Deposit Transaction Fees: {self._sum_of_deposit_transaction_fees}'
        else:
            return 'Deposit amount should be greater than zero.'

    def __apply_deposit_transaction_fee(self, amount):
        transaction_fee = 1
        return amount - transaction_fee

    def __apply_savings_account_deduction(self, amount):
        return amount * 0.05

# Initial values
name = "John"
balance = 0

# Creating an object of the PersonBalance class
person = PersonBalance(name, balance)

# Testing the deposit and display_balance methods
result = person.deposit(101)
print(result)

# Calling the display_balance method
person.display_balance()

