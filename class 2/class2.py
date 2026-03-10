
# class ATM : 
#     def __init__(self, accountHolder, balance):
#         self.accountHolder = accountHolder
#         self.__balance = balance

#     def checkBalance(self):
#         print('your balance is :', self.__balance)

#     def deposit(self, amount):
#         if amount < 0 :
#             print('plz enter valid amount')
#         else :    
#          self.__balance += amount
#          print('your balance is :', self.__balance)


#     def withdraw(self, amount): 
#         if amount < 0 :
#             print('plz enter valid amount')   
#         elif self.__balance >= amount:
#            self.__balance -= amount 
#            print('your balance is :', self.__balance)
#         else:
#            print('insufficient balance')

#     @property
#     def balance(self):
#             return self.__balance
    
#     @balance.setter
#     def balance(self, value):
#         if value <= 0:
#             print('invalid input')
#         else:
#             self.__balance = value    

#     def __str__(self):
#         return f"Account Holder : {self.accountHolder} \n Balance : {self.__balance}"       

# # atm = ATM('Majid', 1000)
# # print(atm.balance) 
# # atm.balance = -5
# # print(atm.balance)

# class SavingAccount(ATM):
#     def addInterest(self):
#         interset = self.balance * 0.05
#         self.balance += interset 
#         print('interest added new balance is :', self.balance)

# class CurrentAccount(ATM):
#     pass

# save = SavingAccount('Majid', 1000)
# save.deposit(500)
# save.checkBalance()
# save.addInterest()
# save.checkBalance()

# curr = CurrentAccount('Hussain', 20000)
# curr.deposit(2000)
# curr.checkBalance()
# curr.withdraw(1000)
# curr.checkBalance()    
    

# atm.__balance = 100000
# print(atm)
# print(atm.__balance)
# while True:
#     print('\n1. Check Balance')
#     print('2. Deposit')
#     print('3. Withdraw Cash')
#     print('4. Exit')

#     choice = input('Plz enter number :')

#     if choice == '1':
#         atm.checkBalance()

#     elif choice == '2':
#         amt = int(input('enter amount to deposit'))
#         atm.deposit(amt)

#     elif choice == '3':
#          amt = int(input('enter amount to withdraw'))       
#          atm.withdraw(amt)

#     elif choice == '4':
#          print('thank you for using ATM')
#          break
    
#     else:
#         print('invalid number selected')   


# program for employee

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     def showInfo(self):
#         print('Employee :', self.name)
#         print('Salary :', self.salary)

#     def work(self):
#         print(self.name, ' is working')

# class Developer(Employee):
#     def code(self):
#         print(self.name, ' is writing code')

# class Designer(Employee):
#     def design(self):
#         print(self.name, ' is designing')

# dev = Developer('Majid', 50000)
# des = Designer('Hussain', 20000)

# dev.showInfo()
# dev.work()
# dev.code()

# des.showInfo()
# des.work()
# des.design()


# Food 

class FoodItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.total = 0
        self.quantity = 0     

class Pizza(FoodItem):
    def __init__(self, name, price):
        super().__init__(name, price)

        self.orders = {
          'BBQ':0,
          'Afghan':0,
          'Masala':0,
          'Cream':0
        }

    def BBQ(self):
        self.price = 1000
        # self.quantity += 1
        self.orders['BBQ'] += 1
        self.total += self.price
        print('BBQ Pizza Ready price :', self.price)
        print('total bill :', self.total)

    def afghan(self):
        self.price = 1200
        # self.quantity += 1
        self.orders['Afghan'] += 1
        self.total += self.price
        print('Aghan Pizza Ready price :', self.price)
        print('total bill :', self.total)
    
    def masala(self):
        self.price = 1400
        # self.quantity += 1
        self.orders['Masala'] += 1
        self.total += self.price
        print('Masala Pizza Ready price :', self.price)
        print('total bill :', self.total)

    def cream(self):
        self.price = 800
        # self.quantity += 1
        self.orders['Cream'] += 1
        self.total += self.price
        print('Cream Pizza Ready price :', self.price) 
        print('total bill :', self.total)

class Burger(FoodItem):
    def __init__(self, name, price):
        super().__init__(name, price)

        self.orders = {
            'Chicken':0,
            'Chicken Cheese':0,
            'Beef':0,
            'Beef Cheese':0
        }

    def chiken(self):
        self.price = 400
        # self.quantity += 1
        self.orders['Chicken'] += 1
        self.total += self.price
        print('Chicken Burger Ready price :', self.price)
        print('total bill :', self.total)

    def chickenCheese(self):
        self.price = 500
        self.total += self.price
        # self.quantity += 1
        self.orders['Chicken Cheese'] += 1
        print('Chicken Cheese Burger Ready price :', self.price)
        print('total bill :', self.total)

    def beef(self):
        self.price = 500
        self.total += self.price
        # self.quantity += 1
        self.orders['Beef'] += 1
        print('Beef Burger Ready price :', self.price)
        print('total bill :', self.total)

    def beefCheese(self):
        self.price = 600
        self.total += self.price
        # self.quantity += 1
        self.orders['Beef Cheese'] += 1
        print('Beef Cheese Burger Ready price :', self.price)
        print('total bill :', self.total)

piz = Pizza('Pizza', 0)
burg = Burger('Burger', 0)

while True:
        print('\n -- Main Menu --')
        print('1. Pizza')
        print('2. Burger')
        print('3. Both')
        print('4. Exit')

        mainChoice = input('Select options :')

        if mainChoice == '1':
                
         while True:
          print('\n1. BBQ Pizza')
          print('2. Afghan Pizza')
          print('3. Masala Pizza')
          print('4. Cream Pizza') 
          print('5. Go back to main menu') 
  
          pizzaChoice = input('select menu')
  
          if pizzaChoice == '1':
              piz.BBQ()
          elif pizzaChoice == '2':
              piz.afghan()
          elif pizzaChoice == '3':
              piz.masala()
          elif pizzaChoice == '4':
              piz.cream()           
          elif pizzaChoice == '5':
              print('thank you')
              break
          else:
              print('invalid selection')

        elif mainChoice == '2':      

         while True:
          print('\n1. Chicken Burger')
          print('2. Chicken Cheese Burger')
          print('3. Beef Burger')
          print('4. Beef Cheese Burger')
          print('5. Go back to main menu') 
      
          burgerChoice = input('please select menu')
      
          if burgerChoice == '1':
              burg.chiken()
          elif burgerChoice == '2':
              burg.chickenCheese() 
          elif burgerChoice == '3':
              burg.beef()
          elif burgerChoice == '4':
              burg.beefCheese()
          elif burgerChoice == '5':
              print('Thank you')
              break   
          else:
              print('invalid selection')   

        elif mainChoice == '4':
            print('\n ------ Pizza order details ------')

            prices = {
                'BBQ':1000,
                "Afghan":1200,
                "Masala":1400,
                "Cream":800
            }

            for pizza, qty in piz.orders.items():
                if qty > 0:
                    print(pizza, 'Pizza :', 'Price :', qty * prices[pizza])

            print('Pizza total bill', piz.total)

            pricesB = {
                'Chicken':400,
                'Chicken Cheese':500,
                'Beef':500,
                'Beef Cheese':600
            }   

            for burger, qty in burg.orders.items():
                if qty > 0:
                    print( 'Burger :',burger, 'Price :', qty * pricesB[burger])

            print('Burger total bill', burg.total)             

        else:
            print('wrong selection')                     