import sys
class Customer:
    bank_name='Le Lo Bank'
    def __init__(self,name,mobileno,pin,balance=0.0):
        self.name=name
        self.mobileno=mobileno
        self.pin=pin
        self.balance=balance
    def deposit(self,dep_amt):
        self.balance=self.balance + dep_amt
    def withdraw(self,with_amt):
        if with_amt > self.balance:
            print("Insufficent fund!!!")
            sys.exit(0)
        self.balance=self.balance - with_amt
    def check_balance(self):
        print('your current balance is: $',self.balance)
name=input("Enter you name here: ")
mobileno=input('Enter your mobile number here: ')
pin=input('Enter your pin here: ')
c=Customer(name,mobileno,pin)
while True:
    print('d-deposit \nw-withdraw \nb-balance enquiry \ne-exit')
    option=(input("Enter your option here: "))
    if option == 'd' or option=='D':
        dep_amt=int(input("Enter the amount: "))
        c.deposit(dep_amt)
    elif option == 'w' or option=='W':
        with_amt=int(input("Enter the amount to withdraw: "))
        c.withdraw(with_amt)
    elif option == 'b' or option=='B':
        c.check_balance()
    elif option == 'e' or option=='E':
        print('Thanks for banking with {} have a nice day'.format(Customer.bank_name))
        sys.exit(0)
    else:
        print('Incorret option please choose corret opiton from the above list')