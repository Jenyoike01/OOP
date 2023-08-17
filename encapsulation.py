class Bankaccount:
    def __init__(self,balance):
        self.balance=balance
    def deposit(self,amount):
        if amount>0 :
            self.balance+=amount
    def getbalance(self):
        return self.balance
account=Bankaccount(2500)
account.deposit(350)
print("Balance is",account.getbalance())