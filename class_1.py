

# name = 'majid'
# num1 = 123
# height = 5.11

# print(name)
# print(num1)
# print(height)

# userName = input('enter your name')
# print('hi' + userName)


# userAge = int(input('enter age'))
# print('your age is' , userAge)

# a = 12
# b = 10

# # print(a + b)
# # print(a != b)
# print(a > b)

# user1 = int(input('enter 1 : '))
# user2 = (input('enter 2 : '))

# result = user1 + user2
# print(result)

# age = int(input('enter age :'))

# if age >= 18:
#     print('adult hai')
# else:
#     print('minor')   


# marks = int(input('enter marks'))
# grade = ''

# if(marks >= 80):
#     grade = 'A'
# elif(marks >= 70):
#     grade = 'B'
# elif (marks >= 60):
#     grade = 'C'
# elif (marks >= 50):
#     grade = 'D'
# else :
#     grade = 'Fail'             

# print(grade)

# num1 = int(input('enter num :'))

# if num1 % 2 == 0 :
#     print('even hai')
# else :
#     print('odd hai')    


# counter = 1

# while counter <= 5:
#     print(counter)
#     counter += 1

# arr1 = [1, 1, 3, 3, 5]

# for i in arr1:
#     print(i)

# num = int(input('enter :'))

# for i in range(1, 11):
#     print(num, 'X', i, '=', num * i )

# def greet(name) :
#   print('Hello', name)

# greet('majid')

# def sum(a, b):
#     return a + b

# result = sum(12, 10)
# print(result)

# def table(num):
#     for i in range(1, 11):
#         print(num, 'X', i, '=', num * i )

# userIn = int(input('enter num :'))
# table(userIn)

# fruits = ['apple', 'mango', 'millon']

# print(fruits)
# firstFr = fruits[0]
# secondFr = fruits[1]

# print(firstFr, secondFr)
# for items in fruits:
#     print(items)

# marks = [45, 67, 89, 32, 76]

# for m in marks:
#     print(m)

# print('total marks :', sum(marks))
# print('max number :', max(marks))
# print('lowest number :', min(marks))

# student = {
#     name: "Majid",
#     age: 20,
#     city: "Karachi"
# }

# print(student)

# class StudentData :
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# std1 = StudentData('majid', 30)
# print(std1.name)        

# class User:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# user1 = User('majid', 20)
# print(user1.name)
# print(user1.age)        

# class Padosi:
#     def __init__(self, naam, harkaten):
#         self.naam = naam
#         self.harkaten = harkaten

#     def greet(self):
#         print('kesa hai bay', self.naam, 'aj tum ny ki hai harkat', self.harkaten)

# s1 = Padosi('kamu', 'boht buri')
# s1.greet()            


class BankAccount:
    def __init__(self, accountHolder, balance):
        self.accountHolder = accountHolder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, withAmount):
        if self.balance >= withAmount:
            self.balance -= withAmount
        else:
            print('insufficient balance bhai')

    def checkAmount(self):
        print('hey', self.accountHolder, 'your amount is', self.balance)        

account = BankAccount('majid', 1000)
account.deposit(1000)
account.withdraw(2500)    
account.checkAmount()            