class BankAccount:
    def __init__(self,balance=0):
        self.__balance=balance
    def deposit(self,amount):
        self.__balance=self.__balance+amount
        print("deposit:",amount)
    def withdraw(self,amount):
        if self.__balance>0 and self.__balance>=amount:
            self.__balance=self.__balance-amount
            print("withdraw:",amount)
        else:
            return "no sufficient balance"
    def get_balance(self):
        print("current balance",self.__balance)
ba=BankAccount()
ba.deposit(5000)
ba.withdraw(2000)
ba.get_balance()

    
    