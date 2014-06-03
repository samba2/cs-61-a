# Question 4
# 
# Predict the result of evaluating the following calls in the interpreter. Then try them out yourself!
# 
# >>> class Account(object):
# ...     interest = 0.02
# ...     def __init__(self, account_holder):
# ...         self.balance = 0
# ...         self.holder = account_holder
# ...     def deposit(self, amount):
# ...         self.balance = self.balance + amount
# ...         print("Yes!")
# ...
# >>> a = Account("Billy")
# >>> a.account_holder
# _____Error, no attribute_

# >>> a.holder
# ___"Billy"___

# >>> class CheckingAccount(Account):
# ...     def __init__(self, account_holder):
# ...         Account.__init__(self, account_holder)
# ...     def deposit(self, amount):
# ...         Account.deposit(self, amount)
# ...         print("Have a nice day!")
# ...
# >>> c = CheckingAccount("Eric")
# >>> a.deposit(30)
# _'Yes'_____

# >>> c.deposit(30)
# __'Have...'____ 
  
#class Person(object):
#    """Person class.
#
#    >>> steven = Person('Steven')
#    >>> steven.repeat()       # starts at whatever value you'd like
#    'I squirreled it away before it could catch on fire.'
#    >>> steven.say('Hello')
#    'Hello'
#    >>> steven.repeat()
#    'Hello'
#    >>> steven.greet()
#    'Hello, my name is Steven'
#    >>> steven.repeat()
#    'Hello, my name is Steven'
#    >>> steven.ask('preserve abstraction barriers')
#    'Would you please preserve abstraction barriers'
#    >>> steven.repeat()
#    'Would you please preserve abstraction barriers'
#    """
#    def __init__(self, name):
#        self.name = name
#        self.spoken = 'I squirreled it away before it could catch on fire.'
#
#    def say(self, stuff):
#        self.spoken = stuff
#        return stuff
#
#    def ask(self, stuff):
#        return self.say("Would you please " + stuff)
#
#    def greet(self):
#        return self.say("Hello, my name is " + self.name)
#
#    def repeat(self):
#        return self.say(self.spoken)


class Account(object):
    """A bank account that allows deposits and withdrawals.

    >>> eric_account = Account("Eric")
    >>> eric_account.deposit(1000000)   # depositing my paycheck for the week
    1000000
    >>> eric_account.transactions
    [('deposit', 1000000)]
    >>> eric_account.withdraw(100)      # buying dinner
    999900
    >>> eric_account.transactions
    [('deposit', 1000000), ('withdraw', 100)]
    """

    interest = 0.02

    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder
        self.transactions = []

    def deposit(self, amount):
        """Increase the account balance by amount and return the
        new balance."""
        self.balance = self.balance + amount
        self.add_transaction( 'deposit', amount )
        return self.balance

    def withdraw(self, amount):
        """Decrease the account balance by amount and return the
        new balance."""
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance = self.balance - amount
        self.add_transaction( 'withdraw', amount )
        return self.balance

    def add_transaction(self, name, amount):
        self.transactions.append( (name, amount)  )


class CheckingAccount(Account):
    """A bank account that charges for withdrawals.
    >>> check = Check("Steven", 42)  # 42 dollars, payable to Steven
    >>> steven_account = CheckingAccount("Steven")
    >>> eric_account = CheckingAccount("Eric")
    >>> eric_account.deposit_check(check)  # trying to steal steven’s money
    'The police have been notified.'
    >>> eric_account.balance
    0
    >>> check.deposited
    False
    >>> steven_account.balance
    0
    >>> steven_account.deposit_check(check)
    42
    >>> check.deposited
    True
    >>> steven_account.deposit_check(check)  # can't cash check twice
    'The police have been notified.'
    """

    withdraw_fee = 1
    interest = 0.01

    def withdraw(self, amount):
        return Account.withdraw(self, amount + self.withdraw_fee)

    def deposit_check(self, check):

        if self.holder != check.payable_to or check.deposited == True:
            return 'The police have been notified.'
        else:
            check.deposited = True
            return self.deposit( check.amount )


# Don't forget to modify CheckingAccount above!
 
class Check(object):
    "*** YOUR CODE HERE ***"

    def __init__(self, payable_to, amount ):
        self.payable_to = payable_to
        self.amount = amount
        self.deposited = False
