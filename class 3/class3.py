# class FoodItem:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#         self.total = 0
#         self.quanity = 0

# class Pizza(FoodItem):
#     def __init__(self, name, price):
#         super().__init__(name, price)
#         # self.masala = 1000
#         # self.beef = 1200

#         self.orders = [
#             {
#               'masala':1000,
#               'Beef': 1200   
#             }
#         ]

#     def masalaPizza(self):
#         self.quatity += 1

# list methods

# cart = ["Pizza", "Burger"]
# cart.append('Fires')
# print(cart)

        
# cart = ["Pizza", "Burger"]
# new_items = ["Fries", "Drink"]

# cart.extend(new_items)

# print(cart)

# cart = ["Pizza", "Burger"]
# cart.insert(2, 'Leg Tikka')
# print(cart)        
# 

# cart = ["Pizza", "Burger", "Fries"]
# cart.remove('Pizza')
# print(cart)


# cart = ["Pizza", "Burger", "Fries"]
# cart.pop(0)
# print(cart)

# cart = ["Pizza", "Burger"]
# cart.clear()
# print(cart)

# cart = ["Pizza", "Burger", "Fries"]
# print(cart.index('Pizza'))

# cart = []

# cart.append('Pizza')

# cart.insert(0,'Fries')
# print(cart)

# cart.insert(0, 'Tikka')
# print('again insert',cart)

# cart.remove('Fries')
# print('after remove fries',cart)

# cities = ["Atlanta", "Baltimore", "Chicago", "Angeles", "Seattle"]

# print(cities[0])
# cities.append(10)
# print(cities)

# todays_tasks = []
# todays_tasks = todays_tasks + ["Walk dog", "Buygroceries"]
# print(todays_tasks)

# cities = ["Atlanta", "Baltimore", "Chicago", "Angeles", "Seattle"]
# newCities = cities[2:]
# print(newCities)


states_in_order_of_founding = ("Delaware",
"Pennsylvania", "New Jersey", "Georgia")

print(states_in_order_of_founding[1])