
class ATM : 
    def __init__(self, accountHolder, balance):
        self.accountHolder = accountHolder
        self.balance = balance

    def checkBalance(self):
        print('your balance is :', self.balance)

    def deposit(self, amount):
        if amount < 0 :
            print('plz enter valid amount')
        else :    
         self.balance += amount
         print('your balance is :', self.balance)


    def withdraw(self, amount): 
        if amount < 0 :
            print('plz enter valid amount')   
        elif self.balance >= amount:
           self.balance -= amount 
           print('your balance is :', self.balance)
        else:
           print('insufficient balance')

atm = ATM('Majid', 1000)

while True:
    print('\n1. Check Balance')
    print('2. Deposit')
    print('3. Withdraw Cash')
    print('4. Exit')

    choice = input('Plz enter number :')

    if choice == '1':
        atm.checkBalance()

    elif choice == '2':
        amt = int(input('enter amount to deposit'))
        atm.deposit(amt)

    elif choice == '3':
         amt = int(input('enter amount to withdraw'))       
         atm.withdraw(amt)

    elif choice == '4':
         print('thank you for using ATM')
         break
    
    else:
        print('invalid number selected')   