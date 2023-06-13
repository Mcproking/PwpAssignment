import os
from time import sleep
from platform import python_version

# This program is only suitable to run on Python 3.10 and above
# This is to check the version of python
# If the Python version is 3.9 and below, then use IF-ELSE instead of MATCH-CASE
def VERSIONCHECKER():
    version = python_version().split(".")
    if int(version[0]) <= 2:
        print("Using Python 2, Please Python 3")
        exit()
    if int(version[1]) <= 9:
        print("Match Case Doesn't Exist. Please use Python 3.10")
        exit()
    else:
        print("Python up-to-date beyond 3.10")
        return False


# This function is to clear the console. Mainly not to overload the entire console.
# IMPORTANT!!! DEFAULT TIMER IS 5 SECONDS, NEED A LONGER TIME TO ENTER THE VALUE
def clearConsole(length = 5):
    def windowsClear():
        os.system('cls')
    def unixClear():
        os.system('clear')
    sleep(length)     
    if os.name == 'nt':
        windowsClear()
    else:
        unixClear()

# Read the inventory.txt and append into list
def readInventory(): 
    inventory.clear()
    with open("./Database/inventory.txt") as f:
        for line in f.readlines(): # read the txt line by line
            item = line.strip().split("/") # remove the "\n" and "/"
            inventory.append(item)

# ---- Below are the Functions used for Insert Item ----            
def cancel_insert():
    print("Cancelled")
    print("Back to Main Menu..")     
        
def code_insert():
    while True:
        try:
            code = int(input("Enter the code of the new item or enter '-1' to cancel: "))
            if code == -1:
                cancel_insert()
                return code
            elif code < 0:
                print("Please enter a valid code.")
            else:
                return code
        except ValueError:
            print("Please enter a valid code.")

def description_insert(code):
    description = str(input(f"Enter the description of item {code} or enter '-1' to cancel: "))
    if description == '-1':
        cancel_insert()
        return description
    else:
        description = description.title()
        return description

def category_insert(description):
    category = str(input(f"Enter the category of {description} or enter '-1' to cancel: "))
    if category == '-1':
        cancel_insert()
        return category
    else:
        category = category.title()
        return category

def unit_insert(description):
    unit = str(input(f"Enter the unit of {description} or enter '-1' to cancel: "))
    if unit == '-1':
        cancel_insert()
        return unit
    else:
        unit = unit.title()
        return unit

def price_insert(description):
    while True:
        try:
            price = float(input(f"Enter the price of {description} or enter '-1' to cancel: "))
            if price == -1:
                cancel_insert()
                return price
            elif price <= 0:
                print("Please enter a valid price.")
            else:
                price = round(price, 2)
                return ("%.2f" % price)
        except ValueError:
            print("Please enter a valid price.")

def quantity_insert(description):
    while True:
        try:
            quantity = int(input(f"Enter the quantity in stock for {description} or enter '-1' to cancel: "))
            if quantity == -1:
                cancel_insert()
                return quantity
            elif quantity < 0:
                print("Please enter a valid quantity.")
            else:
                return quantity
        except ValueError:
            print("Please enter a valid quantity.")

def minimum_insert(description):
    while True:
        try:
            minimum = int(input(f"Enter the minimum threshold allowed for {description} or enter '-1' to cancel: "))
            if minimum == -1:
                cancel_insert()
                return minimum
            elif minimum <= 0:
                print("Please enter a valid minimum threshold.")
            else:
                return minimum
        except ValueError:
            print("Please enter a valid minimum threshold.")

# ---- Below are Functions for Delete Item ----
def cancel_delete():
    print("Cancelled")
    print("Back to menu...")

def delete_confirm():
    while True:
        confirm = str(input("Enter Y to confirm the deletion of the above item or enter N to cancel: "))
        if confirm.upper() != "Y" and confirm.upper() != "N":
            print("Please enter Y or N.")
        else:
            return confirm.upper()


# ---- Below are the Functions for Update Item ----
def cancel_update():
    print("Cancelled")
    print("Back to Main Menu..") 

def update_options():
    print("""
1. Code
2. Description
3. Category
4. Unit
5. Price
6. Minimum Threshold Allowed""")

    while True:
        try:
            select = int(input("\nSelect which data to update or enter '-1' to cancel: "))
            if select == -1:
                return select
            elif select < 1 or select > 6:
                print("Please enter between 1 to 6.")
            else:
                return select
        except ValueError:
            print("Please enter between 1 to 6.")

def code_update():
    while True:
        try:
            code_up = int(input("Enter the updated code of the item or enter '-1' to cancel: "))
            if code_up == -1:
                cancel_update()
                return code_up
            elif code_up < 0:
                print("Please enter a valid code.")
            else:
                return code_up
        except ValueError:
            print("Please enter a valid code.")

def description_update():
    description_up = str(input("Enter the updated description of the item or enter '-1' to cancel: "))
    if description_up == "-1":
        cancel_update()
        return description_up
    else:
        description_up = description_up.title()
        return description_up

def category_update():
    category_up = str(input("Enter the updated category of the item or enter '-1' to cancel: "))
    if category_up == "-1":
        cancel_update()
        return category_up
    else:
        category_up = category_up.title()
        return category_up

def unit_update():
    unit_up = str(input("Enter the updated unit of the item or enter '-1' to cancel: "))
    if unit_up == "-1":
        cancel_update()
        return unit_up
    else:
        unit_up = unit_up.title()
        return unit_up

def price_update():
    while True:
        try:
            price_up = float(input("Enter the updated price of the item or enter '-1' to cancel: "))
            if price_up == -1:
                cancel_update()
                return price_up
            elif price_up <= 0:
                print("Please enter a valid price.")
            else:
                price_up = round(price_up, 2)
                return ("%.2f" % price_up)
        except ValueError:
            print("Please enter a valid price.")

def minimum_update():
    while True:
        try:
            minimum_up = int(input("Enter the updated minimum threshold allowed for the item or enter '-1' to cancel: "))
            if minimum_up == -1:
                cancel_update()
                return minimum_up
            elif minimum_up <= 0:
                print("Please enter a valid minimum threshold.")
            else:
                return minimum_up
        except ValueError:
            print("Please enter a valid minimum threshold.")


# ---- Primary functions below ----
def login(): # Login Page with User Identification
    username = str(input("Enter your username: "))
    password = str(input("Enter your password: "))
    Users = []
    with open("./Database/login.txt","r") as f:
        for line in f.readlines(): # read the txt line by line
            userDetails = line.strip().split("/") # remove the "\n" and "/"
            Users.append(userDetails)
    
    for user in Users:
        if user[0] == username and user[1] == password:
            match user[2]:
                case 'Admin':
                    level = 0
                case 'Inventory-Checker':
                    level = 1
                case 'Purchaser':
                    level = 2
            print("\nLogin Successful!")
            print("Loading Menu...")
            return True, level, user[0]
    else:
        print("Username or Password Incorrect")
        return False, -1
    
def addUser(): # Add new user into login.txt | Auth Level = Admin
    chooseauthLevel = f"""
<{'-'*7}Choose Authority Level{'-'*7}>
Enter 0 for Admin
Enter 1 for Inventory-Checker
Enter 2 for Purchaser
"""

    print(f"<{'-'*7}Add New User{'-'*7}>")
    
    username = str(input("Enter the new username: "))
    
    while True:    
        password = str(input("Enter the new password: "))
        confirm = str(input("Confirm your password: "))
        if confirm != password: # if the password is incorrect
            # User only have to re-enter the password and reconfirm the password again
            print("Your password is incorrect")
            print("Please re-enter your password")
            clearConsole(1)
            print(f"<{'-'*7}Add New User{'-'*7}>")
            print(f"Enter the new username: {username}")
        else:
            while True:
                print(chooseauthLevel)
                
                try:
                    authLevel = int(input("Enter the user type: "))
                except ValueError:
                    print("Please Enter Number between 0 to 2")
                    
                if authLevel < 0 or authLevel > 2:
                    print("Please enter an option between 0 to 2")
                else:
                    break
                
            if authLevel == 0:
                role = "Admin"
            elif authLevel == 1:
                role = "Inventory-Checker"
            elif authLevel == 2:
                role = "Purchaser"    
            else:
                role = "User"
                
            while True:
                print(f"\nPlease confirm the user details\n\nUsername: {username}\nPassword: {password}\nAccess Level: {role}")
                finalconfirm = input("\nDo you confirm the above details? Y/N ")
                
                if finalconfirm.upper() == "Y": # Insert the value into login.txt
                    break
                elif finalconfirm.upper() == "N":
                    reset = input("Reset Input? Y/N ") # Check whether the user wants to reset the input data or not
                    if reset.upper() == "N":
                        print("Cancelled Creation.. Returning to menu")
                        clearConsole(2)
                        LoadMenu()
                    elif reset.upper() == "Y":
                        print("Resetting User Creation..")
                        clearConsole(2)
                        addUser()
                    else:
                        print("Enter only Y or N")
                else:
                    print("Enter only Y or N ")
                    
            with open("./Database/login.txt", "a") as f:
                f.write(f"\n{username}/{password}/{role}")
                
            print("New user has been added.")
            clearConsole(2)
            LoadMenu()

def stockTaking(restart = False): # Stock Taking | Auth = Admin/Inventory Checker
    
    item = [None] * 7 # Initialize item with 7 None. To make sure that Item for printitem() function
    
    def printitem(): # This Function is created for recalling
        print(f"<{'-'*7}Item{'-'*7}>")
        print(f"Name: {item[1]}")
        print(f"Unit: {item[3]}")
        print(f"Quantity: {item[5]}")

    if restart: # This only runs when recursion happens. When recursion happens, restart value change to True
        clearConsole(2)
        print(f"<{'-'*7}Stock Taking{'-'*7}>")
        print("Restart Stock Taking?")
        print("0.Restart\n1.Exit To Main Menu")
        while True:
            try:
                userinput = int(input())
                break
            except ValueError:
                print("Enter 0 or 1")
        if userinput == 1:
            LoadMenu() 
        elif userinput == 0:
            clearConsole(1)
            pass

    while True: # This is to enter Item Code 
        try:
            print(f"<{'-'*7}Stock Taking{'-'*7}>")
            IdCode = int(input("Enter Item Code:"))
            break
        except ValueError:
            print("Wrong Value")
            clearConsole(1)
    
    for item in inventory: # Check the inventory for the correct code, if not recursion happens with 'restart' set to True
        if int(item[0]) == IdCode:
            print("Please Wait..")
            clearConsole(2)
            item = item
            oldItemRaw = f"{item[0]}/{item[1]}/{item[2]}/{item[3]}/{item[4]}/{item[5]}/{item[6]}"
            break
    else:
        print("Item does not exist..")
        stockTaking(restart=True)
            
    while True: # This is to print out the user's item from their chosen ID.
        printitem()
        
        # By printing the item out and reconfirm whether this is what the user wants
        while True:
            try:
                userinput = int(input("1.Change Quantity\n2.Change Item\n0.Back to Main Menu\n"))
                break
            except ValueError:
                print("Wrong Value")
                clearConsole(2)
        
        # Anything from 0 to 2 will be handled, other than that it will be reset back to this current while loop
        if userinput == 0:
            LoadMenu()
        elif userinput == 1:
            break
        elif userinput == 2:
            stockTaking(restart=True)
        else:
            clearConsole(0.2)
            pass

        
    while True:
        clearConsole(2)
        printitem()
        
        try:
            quantity = int(input("Enter the new Quantity:"))
        except ValueError:
            print("Enter Number Only")
        
        # This section is to make sure that the User input's quantity is correct
        clearConsole(2)
        printitem()        
        print(f"\n<---Quantity changed from {item[5]} -> {quantity}--->")
        item[5] = quantity
        confirmation = int(input("\n1.Confirm\n2.Cancel\n"))
        
        if confirmation == 2:
            print("Returning to Menu..")
            LoadMenu()
        elif confirmation == 1:
            NewItemRaw = f"{item[0]}/{item[1]}/{item[2]}/{item[3]}/{item[4]}/{item[5]}/{item[6]}\n"
            
            with open("./Database/inventory.txt","r") as f:
                lines = f.readlines()
                
            with open("./Database/inventory.txt","w") as f:
                for line in lines:
                    if line.strip("\n") != oldItemRaw:
                        f.write(line)
                f.write(NewItemRaw)
            print("\nUpdated")
            print("Returning to Menu..")
            sleep(1)
            LoadMenu()

def insert(): # Insert New Item | Auth = Admin
    master_insert_list = []
    while True: # if the user enters -1, it will stop this entire insert
        code = code_insert()
        if code == -1:
            break
        description = description_insert(code)
        if description == "-1":
            break
        category = category_insert(description)
        if category == "-1":
            break
        unit = unit_insert(description)
        if unit == "-1":
            break
        price = price_insert(description)
        if price == -1:
            break
        quantity = quantity_insert(description)
        if quantity == -1:
            break
        minimum = minimum_insert(description)
        if minimum == -1:
            break
        insert = [code, description, category, unit, price, quantity, minimum]
        master_insert_list.append(insert)

        while True: # asking the user whether the user wants to insert more items or not
            choose = str(input("Do you still want to insert more items? Enter Y for Yes or N for No: "))
            if choose.upper() != "Y" and choose.upper() != "N":
                print("Please enter Y or N.")
            else:
                break
        if choose.upper() == "Y":
            clearConsole(0.2)
            continue
        else:
            clearConsole(0.5)
            for list in master_insert_list: # double confirming the item that is going to be inserted into the inventory.txt
                print(f"Item Code:{list[0]}")
                print(f"Description:{list[1]}")
                print(f"Category:{list[2]}")
                print(f"Unit:{list[3]}")
                print(f"Price:{list[4]}")
                print(f"Quantity:{list[5]}")
                print(f"Minimum:{list[6]}")
                print(f"{'-'*15}")
            print("Please Make Sure the Insert Values are correct.\nInserted Data can be edited from 2.Update Item")
            while True:
                try:
                    userinput = int(input("1.Continue\n2.Exit to Main menu\n"))
                except ValueError:
                    print("Enter 1 or 2")
                    
                if userinput == 1:
                    break
                elif userinput == 2:
                    LoadMenu()
            # Inserting the item and rewriting the inventory.txt        
            with open("./Database/inventory.txt", "a") as f:   
                for item in master_insert_list:
                    f.write(f"{item[0]}/{item[1]}/{item[2]}/{item[3]}/{item[4]}/{item[5]}/{item[6]}\n")
                    pass
            print("Item(s) have been inserted successfully.")
            break
    sleep(2)
    LoadMenu()

def ReplenishList(): # Check which item to replenish | Auth = Admin/Purchaser
    Replenish_item = []
    for item in inventory:
        if int(item[5]) < int(item[6]): # if the quanity is less than the minimum threshold allowed
            Replenish_item.append(item)
            
    print(f"<{'-'*4}Replenish Item List{'-'*4}>\n{'-'*25}")# prints out the Replenish_item
    for item in Replenish_item: 
        print(f"Item Code:{item[0]}")
        print(f"Item Name:{item[1]}")
        print(f"Quantity:{item[5]}")
        print(f"Expected Quantity:{item[6]}")
        print(f"{'-'*25}")
    input("Press Enter to go Back to Main Menu")
    LoadMenu()

def ReplenishItem():
    Replenish_item = []
    
    while True: # Displays a menu for the user to go back to the menu if needed
        print(f"<{'-'*4}Replenish Item List Menu{'-'*4}>")
        try:
            userinput = int(input("1.Add Quantity\n2.Show Inventory\n0.Return to Main Menu\n"))
            break
        except ValueError:
            print("Please Enter Numbers")
            clearConsole(1.5)
            
    if userinput == None:
        ReplenishItem()         
          
    if userinput == 1:
        clearConsole(0.2)
    elif userinput == 2:
        clearConsole(0.2)
        print(f"<{'-'*7}Inventory List{'-'*7}>")
        for item in inventory: # this prints the list of inventory to the user
            print(f"Item Code:{item[0]}")
            print(f"Item Name:{item[1]}")
            print(f"Quantity:{item[5]}")
            print(f"Expected Quantity:{item[6]}")
            print(f"{'-'*25}")
        input("Enter to go back to Replenish Item Menu")
        sleep(1)
        clearConsole(0)
        ReplenishItem()
    elif userinput == 0:
        LoadMenu()
    else:
        print("Enter Value 1 or 0 ")
        clearConsole(1.5)
        ReplenishItem()
    
    while True:
        for item in inventory:
                if int(item[5]) < int(item[6]): # if the quanity is less than the minimum threshold allowed
                    Replenish_item.append(item)
                    
        while True:
            print(f"<{'-'*4}Replenish Item List{'-'*4}>\n{'-'*25}")# prints out the Replenish_item
            for item in Replenish_item: 
                print(f"Item Code:{item[0]}")
                print(f"Item Name:{item[1]}")
                print(f"Quantity:{item[5]}")
                print(f"Expected Quantity:{item[6]}")
                print(f"{'-'*25}")
            
            try:
                userinput = int(input("Enter Item Code:"))
                break
            except ValueError:
                print("Please Enter Numbers")
                clearConsole(1.5)
        
        for item in inventory:
            if int(item[0]) == userinput:
                break                    
        else:
            print("Item do not exist... Restarting Replenish Item")
            clearConsole(1)
            ReplenishItem()
        
        while True: # Double confirm with the user whether this item is the correct one or not
            clearConsole(0.2)
            print(f"<{'-'*4}Item Details{'-'*4}>")
            print(f"Item Code:{item[0]}")
            print(f"Item Name:{item[1]}")
            print(f"Quantity:{item[5]}\n")
            
            try:
                userinput = int(input("1.Add Item\n0.Return to Main Menu\n"))            
                if userinput == 0 or userinput == 1:
                    break
                else:
                    print("Input only allows 1 or 0")
                    sleep(0.6)
            except ValueError:
                print("Enter Only Number")
                sleep(0.6)
                
        if userinput == 0:
            print("Returning to Main Menu...")
            LoadMenu()
            
        if userinput == 1:
            while True: # adding the quantity
                try:
                    addQuantity = int(input("Please state the amount to add:"))
                    break
                except ValueError:
                    print("Enter Only Number")
                    
                    
            while True: # Double confirm the quantity added        
                clearConsole(0.2)
                print(f"<{'-'*4}Item Details{'-'*4}>")
                print(f"Item Code:{item[0]}")
                print(f"Item Name:{item[1]}\n")
                print(f"<{'-'*4}Item Changes{'-'*4}>")
                print(f"Old Quantity:{item[5]}")
                newQuantity = int(item[5]) + addQuantity
                print(f"New Quantity:{newQuantity}")
            
                try:
                    confirm = int(input("\n1.Confirm\n2.Cancel\n"))
                    if confirm == 1 or confirm == 2:
                        break
                    else:
                        print("Enter 1 or 0")
                except ValueError:
                    print("Enter Only Number")
                    
            if confirm == 2:
                print("Returning to Menu..")
                LoadMenu()
            
            # Rewriting the inventory.txt file    
            if confirm == 1:
                NewItemRaw = f"{item[0]}/{item[1]}/{item[2]}/{item[3]}/{item[4]}/{newQuantity}/{item[6]}\n"
                oldItemRaw = f"{item[0]}/{item[1]}/{item[2]}/{item[3]}/{item[4]}/{item[5]}/{item[6]}"
                with open("./Database/inventory.txt","r") as f:
                    lines = f.readlines()
                    
                with open("./Database/inventory.txt","w") as f:
                    for line in lines:
                        if line.strip("\n") != oldItemRaw:
                            f.write(line)
                    f.write(NewItemRaw)
                print("\nUpdated")
                print("Returning to Menu..")
                sleep(1)
                LoadMenu()
                
def update():
    master_update_list = []
    
    while True:
        try:
            try: # to let the user to exit this function
                item = int(input("Enter the code of the item that you want to update or enter '-1' to cancel: "))
                if item == -1:
                    cancel_update()
                    LoadMenu()
                elif item < 0:
                    print("Please enter a valid code.")
                else:
                    with open("./Database/inventory.txt", "r") as f: # read the inventory.txt file again
                        f.seek(0)
                        read = f.readlines()
                        for line in read:
                            itemDetails = line.strip().split("/")
                            master_update_list.append(itemDetails)
                        for items in master_update_list: # enumerate the list and check if the item exist
                            if int(items[0]) == item:
                                print("\nItem details:")
                                print(items, end = "\n")
                                oldItems = f"{items[0]}/{items[1]}/{items[2]}/{items[3]}/{items[4]}/{items[5]}/{items[6]}"
                                updateOption = update_options()
                            
                                if updateOption == -1: # give user to have the choice to exit
                                    break

                                if updateOption == 1: # change the code of the item
                                    code_up = code_update()
                                    if code_up == -1:
                                        LoadMenu()
                                    items[0] = code_up
                                    updatedItem = f"{items[0]}/{items[1]}/{items[2]}/{items[3]}/{items[4]}/{items[5]}/{items[6]}"
                                    with open("./Database/inventory.txt", "w") as f:
                                        for line in read:
                                            if line.strip("\n") != oldItems:
                                                f.write(line)
                                        f.write(updatedItem + "\n")
                                    print("Item code updated successfully.")

                                elif updateOption == 2: # change the item description
                                    description_up = description_update()
                                    if description_up == "-1":
                                        LoadMenu()
                                    items[1] = description_up
                                    updatedItem = f"{items[0]}/{items[1]}/{items[2]}/{items[3]}/{items[4]}/{items[5]}/{items[6]}"
                                    with open("./Database/inventory.txt", "w") as f:
                                        for line in read:
                                            if line.strip("\n") != oldItems:
                                                f.write(line)
                                        f.write(updatedItem + "\n")
                                    print("Item description updated successfully.")

                                elif updateOption == 3: # change the item category
                                    category_up = category_update()
                                    if category_up == "-1":
                                        LoadMenu()
                                    items[2] = category_up
                                    updatedItem = f"{items[0]}/{items[1]}/{items[2]}/{items[3]}/{items[4]}/{items[5]}/{items[6]}"
                                    with open("./Database/inventory.txt", "w") as f:
                                        for line in read:
                                            if line.strip("\n") != oldItems:
                                                f.write(line)
                                        f.write(updatedItem + "\n")
                                    print("Item category updated successfully.")

                                elif updateOption == 4: # change the item's unit
                                    unit_up = unit_update()
                                    if unit_up == "-1":
                                        LoadMenu()
                                    items[3] = unit_up
                                    updatedItem = f"{items[0]}/{items[1]}/{items[2]}/{items[3]}/{items[4]}/{items[5]}/{items[6]}"
                                    with open("./Database/inventory.txt", "w") as f:
                                        for line in read:
                                            if line.strip("\n") != oldItems:
                                                f.write(line)
                                        f.write(updatedItem + "\n")
                                    print("Item unit updated successfully.")

                                elif updateOption == 5: # change the price of the item
                                    price_up = price_update()
                                    if price_up == -1:
                                        LoadMenu()
                                    items[4] = price_up
                                    updatedItem = f"{items[0]}/{items[1]}/{items[2]}/{items[3]}/{items[4]}/{items[5]}/{items[6]}"
                                    with open("./Database/inventory.txt", "w") as f:
                                        for line in read:
                                            if line.strip("\n") != oldItems:
                                                f.write(line)
                                        f.write(updatedItem + "\n")
                                    print("Item price updated successfully.")

                                else: # Change the minimum threshold allowed for the item 
                                    minimum_up = minimum_update()
                                    if minimum_up == -1:
                                        LoadMenu()
                                    items[6] = minimum_up
                                    updatedItem = f"{items[0]}/{items[1]}/{items[2]}/{items[3]}/{items[4]}/{items[5]}/{items[6]}"
                                    with open("./Database/inventory.txt", "w") as f:
                                        for line in read:
                                            if line.strip("\n") != oldItems:
                                                f.write(line)
                                        f.write(updatedItem + "\n")
                                    print("Item minimum threshold updated successfully.")
                                break
                        else:
                            print("Item not found.")
                            clearConsole(1.5)
                            update()
                        if updateOption == -1:
                            cancel_update()
                            LoadMenu()
                        while True: # asking the user whether the user wants to update more items or not
                            choose_up = str(input("Do you still want to update more items? Enter Y for Yes or N for No: "))
                            if choose_up.upper() != "Y" and choose_up.upper() != "N":
                                print("Please enter Y or N.")
                            else:
                                break
                        if choose_up.upper() == "Y":
                            update()
                        else:
                            print("Item(s) have been updated successfully.")
                            print("Back to Main Menu...")
                            LoadMenu()
                        break
            except ValueError:
                print("Please enter a valid code.")

            
        except FileNotFoundError:
            print("File not found.")
        except IOError:
            print("Error occurred.")
        except Exception as e:
            print("Error occurred:", str(e))

def delete():
    master_delete_list = []
    while True:
        try:
            try: # let user to have a choice to exit this function
                delete_code = int(input("Enter the item code to delete or enter '-1' to cancel: "))
                if delete_code == -1:
                    cancel_delete()
                    LoadMenu()
                elif delete_code < 0:
                    print("Please enter a valid code.")
                else:
                    with open("./Database/inventory.txt", "r") as f: # read the file again
                        f.seek(0)
                        read = f.readlines()
                    for line in read:
                        itemDetails = line.strip().split("/")
                        master_delete_list.append(itemDetails)
                    for items in master_delete_list: # enumerate the list
                        if int(items[0]) == delete_code:
                            print("\nItem details:")
                            print(items, end = "\n\n")
                            confirm = delete_confirm()
                            if confirm == "Y": # remove the item
                                master_delete_list.remove(items)
                                with open("./Database/inventory.txt", "w") as new:
                                    for items in master_delete_list:
                                        newDetails = f"{items[0]}/{items[1]}/{items[2]}/{items[3]}/{items[4]}/{items[5]}/{items[6]}"
                                        new.write(newDetails + "\n")
                                print("Item deleted successfully.")
                                print("Returning to Main Menu")
                                LoadMenu()
                            else:
                                print("Back to Main Menu...")
                                LoadMenu()
                    else:
                        print("Item not found.")
                        print("Back to Main Menu...")
                        LoadMenu()
            except ValueError:
                print("Please enter a valid code.")
        except FileNotFoundError:
            print("File not found.")
        except IOError:
            print("Error occurred.")
        except Exception as e:
            print("Error occurred:", str(e))

def search():
    temp_inventory = []
    def searchDescription(): # search by using description
        while True:
            try:
                search = str(input("Enter Description:"))
                break
            except ValueError:
                print("Invalid Value")
             
        for item in inventory:
            if search.title() in item[1]:
                temp_inventory.append(item)
        # print(temp_inventory)           

    def searchCode(): # search by using item code
        while True:
            try:
                minRange = int(input("Enter Range from:"))
                maxRange = int(input("Enter Range to:"))
                break
            except ValueError:
                print("Enter Numbers only")
        for item in inventory:
            if int(item[0]) in range(minRange,maxRange):
                temp_inventory.append(item)
        # print(temp_inventory)
        
    def searchCategory(): # search by using category
        while True:
            try:
                search = str(input("Enter Category:"))
                break
            except ValueError:
                print("Enter correct value.")
        for item in inventory:
            if search.title() in item[2]:
                temp_inventory.append(item)
        # print(temp_inventory)

    def searchPrice(): # search by using price
        while True:
            try:
                minRange = float(input("Enter Range from:")) # 4
                maxRange = float(input("Enter Range to:")) # 10
                break
            except ValueError:
                print("Enter Numbers only")
        for item in inventory:
            if float(item[4]) >= minRange and float(item[4]) <= maxRange:
                temp_inventory.append(item)
        # print(temp_inventory)

    
    while True: 
        try:
            # have a menu to search based on the available choices
            print(f"<{'-'*7}Search By{'-'*7}>") 
            userinput = int(input("1.Search by Description\n2.Search by Code Range\n3.Search by Category\n4.Search by Price Range\n"))
            match userinput: # from the choice of 1 to 4, use case below
                case 1:
                    clearConsole(0.5)
                    searchDescription()
                    break
                case 2:
                    clearConsole(0.5)
                    searchCode()
                    break
                case 3:
                    clearConsole(0.5)
                    searchCategory()
                    break
                case 4:
                    clearConsole(0.5)
                    searchPrice()
                    break
                case _:  
                    print("Enter only Number from 1 to 4")  
        except ValueError:
            print("Enter only Number from 1 to 4")
    
    # prints out the result
    print(f"<{'-'*7}Search Results{'-'*7}>")
    for item in temp_inventory:
        print(f"Item Code: {item[0]}")
        print(f"Item Name: {item[1]}")
        print(f"Category: {item[2]}")
        print(f"Unit: {item[3]}")
        print(f"Price: {item[4]}")
        print(f"Quantity: {item[5]}")
        print(f"Minimum Threshold: {item[6]}")
        print(f"{'-'*25}")
        
    input("Press enter to go Back to Main Menu")
    LoadMenu()


# ---- User's Authority Functions ----
def admin(username): # Admin-Level Consoles
    option = 0
    menu = f"""Welcome, {username}.
<------- ADMIN MENU ------->
1. Insert New Item
2. Update Item
3. Delete Item
4. Stock Taking
5. View Replenish List
6. Stock Replenishment
7. Search Items
8. Add New User

-1. Exit Program
"""

    while True:
        clearConsole(1)
        print(menu)
        try:
            option = int(input("Select an option from above: "))
        except ValueError:
            print("Enter an option between 1 to 8.")
        
        if option == -1:
            print("Program will be exiting soon..")
            sleep(3)
            exit()
            
        if option <= 0 or option >= 9:
            print("Please enter an option between 1 to 8")
            sleep(1)
            # After the user input the wrong value, it will reprint the menu screen
        else:
            break

    match option:
        case 1:
            clearConsole(1.5)
            insert()
        case 2:
            clearConsole(1.5)
            update()
        case 3:
            clearConsole(1.5)
            delete()
        case 4:
            clearConsole(1.5)
            stockTaking()
        case 5:
            clearConsole(1.5)
            ReplenishList()
        case 6:
            clearConsole(1.5)
            ReplenishItem()
        case 7:
            clearConsole(1.5)
            search()
        case 8:
            clearConsole(1.5)
            addUser()  
        case _:
            print("Invalid")
            LoadMenu()

def inventory_Checker(username): # Inventory-Checker Consoles
    option = 0
    menu = f"""Welcome, {username}.
<------- INVENTORY-CHECKER MENU ------->
1. Stock Taking
2. Search Items

-1. Exit Program
"""
    while True:
        clearConsole(1)
        print(menu)
        try:
            option = int(input("Select an option from above: "))                
        except ValueError:
            print("Please enter an option between 1 and 2.")
            
        if option == -1:
            print("Program will be exiting soon..")
            sleep(3)
            exit()
        if option < 1 or option > 2:
            print("Please enter an option between 1 and 2.")
            sleep(1)
        else:
            break

    match option:
        case 1:
            clearConsole(1.5)
            stockTaking()
        case 2:
            clearConsole(1.5)
            search()

def purchaser(username): # Purchaser Consoles
    option = 0
    menu = f"""Welcome, {username}.
<------- PURCHASER MENU ------->
1. View Replenish List
2. Stock Replenishment
3. Search Items

-1. Exit Program
"""
    while True:
        clearConsole(1)
        print(menu)
        try:
            option = int(input("Select an option from above: "))
        except ValueError:
            print("Please enter an option between 1 and 3.")

        if option == -1:
            print("Program will be exiting soon..")
            sleep(3)
            exit()
        if option < 1 or option > 3:
            print("Please enter an option between 1 and 3.")
            sleep(1)
        else:
            break
    match option:
        case 1:
            clearConsole(1.5)
            ReplenishList()
        case 2:
            clearConsole(1.5)
            ReplenishItem()
        case 3:
            clearConsole(1.5)
            search()


# ---- Below are start functions -----
def startupFirstLogin(): # only use this function once for the program to start
    loginSuccess = (False,-1)
    while not loginSuccess[0]:
        loginSuccess = login()
    if loginSuccess[0]:
        username = loginSuccess[2]
        auth = loginSuccess[1]
    return username,auth

def LoadMenu():
    readInventory()
    match UserDatas[1]:
        case 0:
            admin(username=UserDatas[0])
        case 1:
            inventory_Checker(username=UserDatas[0])
        case 2:
            purchaser(username=UserDatas[0])


inventory = []
VERSIONCHECKER() # If the version is 3.10 above, will return FALSE. If below, the program would not run    
UserDatas = startupFirstLogin() # User data consists of 2 main data, username and auth level
LoadMenu()

