class Account:
    def __init__(self,account_number):
        self.account_no=account_number
        self.balance=0.00
    def display(self):
        print(f'Bank Account No: {self.account_no}')
        print(f'Balance: {self.balance}')
    def deposit(self,float):
        self.balance=float
    def withdraw(self,float):
        if self.balance>float:
            self.balance-=float
        else:
            print('Insufficient funds on the account')

acc1 = Account('12 3456 5555 9090 1111 0000 7722')
acc1.display()
acc1.deposit(25.30)
acc1.display()
acc1.withdraw(31.70)
acc1.display()
acc1.withdraw(14)
acc1.display()