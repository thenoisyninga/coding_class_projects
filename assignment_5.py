menu = {
            "Samosa": 20,
            "Kheer": 30,
            "Biryani": 100,
            "Tea": 40,
            "Paratha": 30,
        }

currentBalance = float(input("What is your current balance? "))
isBuying = True

while isBuying:
    for item in menu:
        print(f"{item} costs {menu[item]}")
    itemName = input("What do you want to buy?")
    if itemName in menu:
        cost = menu[itemName]
        updatedCurrentBalance = currentBalance - cost

        # A restaurant program that has a menu with 5 random items.
        # - It initially asks for the customer's current balance.
        # - It asks what the customer would like to buy repeatedly until he/she wants to check out.
        # - After which the program tells the updated balance of the customer

        currentBalance = float(input("Enter current balance: "))
        isBuying = True

        while isBuying:

            # Showing the menu
            for menuItem in menu:
                itemCost = menu[menuItem]
                print(f"{menuItem} : Rs.{itemCost}")

            itemToBuy = str(input("Enter the item you want to buy (if you want to check out, enter 'e'): "))

            # Checking if avaialable
            if item != 'e':
                if itemToBuy in menu:
                    # buying process
                    cost = menu[itemToBuy]
                    updatedBalance = currentBalance - cost

                    # Checking if affordable
                    if updatedBalance >= 0:
                        currentBalance = updatedBalance
                        print(f"Item Succesfully Bought, here is your {itemToBuy}.")
                    else:
                        print("Insufficent Balance in your account")
                    time.sleep(1)

                else:
                    print("Item you want is not available")
            else:
                isBuying = False

                # A restaurant program that has a menu with 5 random items.
                # - It initially asks for the customer's current balance.
                # - It asks what the customer would like to buy repeatedly until he/she wants to check out.
                # - After which the program tells the updated balance of the customer
                import time

                menu = {
                    "Samosa": 20,
                    "Kheer": 30,
                    "Biryani": 100,
                    "Tea": 40,
                    "Paratha": 30,
                }

                currentBalance = float(input("Enter current balance: "))
                isBuying = True

                while isBuying:

                    # Showing the menu
                    for menuItem in menu:
                        itemCost = menu[menuItem]
                        print(f"{menuItem} : Rs.{itemCost}")

                    itemToBuy = str(input("Enter the item you want to buy (if you want to check out, enter 'e'): "))

                    # Checking if avaialable
                    if itemToBuy != 'e':
                        if itemToBuy in menu:
                            # buying process
                            cost = menu[itemToBuy]
                            updatedBalance = currentBalance - cost

                            # Checking if affordable
                            if updatedBalance >= 0:
                                currentBalance = updatedBalance
                                print(f"Item Succesfully Bought, here is your {itemToBuy}.")
                            else:
                                print("Insufficent Balance in your account")

                        else:
                            print("Item you want is not available")
                        print(f"Your account currently has Rs.{currentBalance}")
                        time.sleep(5)

                    else:
                        print("Thank you for eating with us.")
                        isBuying = False
