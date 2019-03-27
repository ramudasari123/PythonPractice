class Banking():
    def __init__(self,name):
        self.default=0
        self.customer=name
    def deposit(self,amount,name):
        self.balance=self.default
        if (self.customer.upper()==name.upper()):
            self.balance=self.balance+amount
            print('amount deposited {}'.format(self.balance))
        else:
            print("Invalid Details, Cannot proceed")
        return self.balance
    def withdraw(self,amount,name):
        if(self.customer.upper()==name.upper()):
            if(self.balance>amount):
                print('Congrats, You have sufficient balance to withdraw')
                self.balance=self.balance-amount
                print(f"your current amount after withdraw is {self.balance}")
        else:
            print("Sorry, Please Enter valid Details")

bank=Banking('Ram')
bank.deposit(1000,'Ram')
bank.withdraw(500,'ram')