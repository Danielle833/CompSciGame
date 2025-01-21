import random

menuItems = ["pancakes", "eggs", "bacon", "waffles", "juice", "toast"]

def makeOrder():
    order = []
    orderAmount = random.randint(1, 5)
    for x in range(orderAmount):
        order.append(menuItems[random.randint(0, (len(menuItems)-1))])
    return order

# possiblePancakeToppings = ["blueberries", "strawberries", "banana", "chocolate chips", "whipped cream", "syrup"]
# possibleEggStyles = ["sunny side up", "scrambled", "omelette"]
# possibleWaffleToppings = ["blueberries", "strawberries", "banana", "chocolate chips", "whipped cream", "syrup"]
# possibleJuiceTypes = ["apple juice", "orange juice", "cranberry juice", "lemonade"]
# possibleToastToppings = ["avocado", "butter", "jam", "peanutbutter"]


# def addToppings(order):
#     pancakeToppings = ["blueberries", "strawberries", "banana", "chocolate chips", "whipped cream", "syrup"]
#     eggStyles = ["sunny side up", "scrambled", "omelette"]
#     waffleToppings = ["blueberries", "strawberries", "banana", "chocolate chips", "whipped cream", "syrup"]
#     juiceTypes = ["apple juice", "orange juice", "cranberry juice", "lemonade"]
#     toastToppings = ["avocado", "butter", "jam", "peanutbutter"]
#
#     for item in range(order):
#         if order[item] == "pancakes":
#             b = random.randint(0, len(pancakeToppings))
#             for i in range(b):
#                 currentTopping = random.randint(0, len(pancakeToppings))
#                 menuItems["pancakes"].append(currentTopping)
#
#         if order[item] == "eggs":
#             menuItems["eggs"] = eggStyles[random.randint(0, len(eggStyles))]
#
#         elif order[item] == "waffles":
#             b = random.randint(0, len(waffleToppings))
#             for i in range(b):
#                 currentTopping = random.randint(0, len(waffleToppings))
#                 menuItems["waffles"].append(currentTopping)
#
#         elif order[item] == "juice":
#             menuItems["juice"] = juiceTypes[random.randint(0, len(juiceTypes))]
#
#         elif order[item] == "toast":
#             menuItems["toast"] = toastToppings[random.randint(0, len(toastToppings))]



# Cleaning up the random order for displaying on the screen
# orderOne = CustomerOrder(1)
# orderItems = orderOne.items
#
# orderItemsList = list(orderItems.items())
# print(orderItemsList)
# formList = []
#
# for thing in orderItemsList:
#     ingList = []
#     for x in range(len(thing)):
#         ingList.append(str(thing[x]))
#     ingList.pop(0)
#     if len(ingList) > 0:
#         formList.append(f"{thing[0]}: {",".join(ingList)}")
#     else:
#         formList.append(f"{thing[0]}")
#
# charsToRemove = ["[", "]", "'", '"']
#
# for t in range(len(formList)):
#     for x in range(len(charsToRemove)):
#         formList[t] = formList[t].replace(charsToRemove[x], "")
#     formList[t] = formList[t].replace("-", " ")
#     formList[t] = formList[t].replace("n, ", "n")





# def displayOrder(formList):
#     yPos = 400
#     for f in range(len(formList)):
#         orderSurface = orderFont.render(str(formList[f]), False, (250, 250, 250))
#         orderRect = orderSurface.get_rect(topleft=(300, yPos))
#         display.blit(orderSurface, orderRect)
#         yPos += 25
