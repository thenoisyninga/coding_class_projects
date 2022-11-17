# Write a program that inputs the current balance of the customer and
# asks what the customer wants to buy. And then outputs the updated
# account balance

menu = {
    "Chicken": 100,
    "Juice": 50,
    "Dessert": 70,
    "Appetizers" : 40,
    "Donuts" : 20
}

# ChickenCost = 100
# JuiceCost = 50
# DessertCost = 70
finishedBuying = False

accountBalance = float(input("Enter the account balance: "))

while not finishedBuying:
    print("These are your options:")
    for item in menu:
        print(f'{item} : {menu[item]}')
    itemOfChoice = str(input("Enter what you want to buy: "))
    if itemOfChoice in menu:
        cost = menu[itemOfChoice]
        if accountBalance >= cost:
            accountBalance = accountBalance - cost
            print(f"Your {itemOfChoice} is served.")
        else:
            print("Insufficent balance.")

    print(f"Current Balance: {accountBalance}")
    UserChoice = str(input("Would you like yo quit? Enter 'Yes', else leave this blank: "))
    if UserChoice.upper() == 'Yes'.upper():
        finishedBuying = True

print("Thank you for eating with us.")

# if itemOfChoice.upper() == "chicken".upper():
#     if accountBalance >= ChickenCost:
#         accountBalance = accountBalance - ChickenCost
#         print("Your Chicken is served")
#     else:
#         print("Insufficient Balance")
# elif itemOfChoice.upper() == "Juice".upper():
#     if accountBalance >= JuiceCost:
#         accountBalance = accountBalance - JuiceCost
#         print("Your Juice is served")
#     else:
#         print("Insufficient Balance")
# elif itemOfChoice.upper() == "Desert".upper():
#     if accountBalance >= DessertCost:
#         accountBalance = accountBalance - DessertCost
#         print("Your Dessert is served")
#     else:
#         print("Insufficient Balance")
# else:
#     print("This item is not available.")




