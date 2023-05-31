import os
import time
from platform import python_version

# This is to check the version of python
# If the Python version is 3.9 and below, then utilize the IF-ELSE instead of MATCH-CASE
def VERSIONCHECKER():
    version = python_version().split(".")
    if int(version[0]) <= 2:
        print("Using Python 2, Please Python 3")
        exit()
    if int(version[1]) <= 9:
        print("Match Case Doesnt Exist. Changing to If-Else")
        return True
    else:
        print("Python up-to-date beyond 3.10")
        return False


# This function is to clear the console. Mainly not to overfill the entire console.
# IMPORTANT!!! DEFAULT TIMER IS 5 SECONDS, NEED FOR LONGER ENTER THE VALUE
def clearConsole(length = 5):
    def windowsClear():
        os.system('cls')
    def unixClear():
        os.system('clear')
    time.sleep(length)     
    if os.name == 'nt':
        windowsClear()
    else:
        unixClear()

# Read the inventory.txt and append into list
def readInventory(): 
    inventory.clear()
    with open("./Database/inventory.txt") as f:
        for line in f.readlines(): # read the txt line by line
            item = line.strip().split("/") # remove the \n and "/"
            inventory.append(item)

# ---- Below are Function use for Insert item ----            
def cancel_insert():
        print("Cancelled")
        print("Back to menu..")     
        
def code_insert():
    while True:
        try:
            code = int(input("Enter the code of the item or enter '-1' to cancel: "))
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
                return price
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

# ---- Primary function below ----
def login(): # Login Page with User Identification
    username = str(input("Enter your username: "))
    password = str(input("Enter your password: "))
    Users = []
    with open("./Database/login.txt","r") as f:
        for line in f.readlines(): # read the txt line by line
            userDetails = line.strip().split("/") # remove the \n and "/"
            Users.append(userDetails)
    
    for user in Users:
        if user[0] == username and user[1] == password:
            if not V:
                match user[2]:
                    case 'Admin':
                        level = 0
                    case 'Inventory-Checker':
                        level = 1
                    case 'Purchaser':
                        level = 2
                print("\nLogin Sucessful!")
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
            # User only have to reenter the password and reconfirm the password again
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
                finalconfirm = input("\nDo You confirm the above details? Y/N ")
                
                if finalconfirm.upper() == "Y": # Insert the value into login.txt
                    break
                elif finalconfirm.upper() == "N":
                    reset = input("Reset Input? Y/N ") # Check if user want to reset the input data or not
                    if reset.upper() == "N":
                        print("Cancelled Creation.. Returning to menu")
                        clearConsole(2)
                        LoadMenu()
                    elif reset.upper() == "Y":
                        print("Reseting User Creation..")
                        clearConsole(2)
                        addUser()
                    else:
                        print("Enter only Y or N")
                else:
                    print("Enter only Y or N ")
                    
            with open("./Database/login.txt", "a") as f:
                f.write(f"\n{username}/{password}/{role}")
                
            print("New user has been added")
            clearConsole(2)
            LoadMenu()

def stockTaking(restart = False): # Stock Taking | Auth = Admin/Inventory Checker
    
    item = [None] * 7 # Initalize item with 7 None. To make sure that Item for printitem() function
    
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
        print("Item do not exist..")
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
        print(f"\n<---Quantity change from {item[5]} -> {quantity}--->")
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
            time.sleep(1)
            LoadMenu()

def insert(): # Insert New Item | Auth = Admin
    master_insert_list = []
    while True:
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
        if quantity == -1:
            break
        insert = [code, description, category, unit, price, quantity, minimum]
        master_insert_list.append(insert)

        while True:
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
            for list in master_insert_list:
                print(f"Item Code:{list[0]}")
                print(f"Description:{list[1]}")
                print(f"Category:{list[2]}")
                print(f"Unit:{list[3]}")
                print(f"Price:{list[4]:.2f}")
                print(f"Quanity:{list[5]}")
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
                    
            with open("./Database/inventory.txt", "a") as f:   
                for item in master_insert_list:
                    f.write(f"{item[0]}/{item[1]}/{item[2]}/{item[3]}/{item[4]}/{item[5]}/{item[6]}\n")
                    pass
            print("Item(s) have been inserted successfully.")
            break
    time.sleep(2)
    LoadMenu()

def ReplenishList(): # Check Which item to replenish | Auth = Admin/Purchaser
    Replenish_item = []
    for item in inventory:
        if item[5] < item[6]: # if the quanity is less then expected ammount
            Replenish_item.append(item)
            
    print(f"<{'-'*4}Replenish Item List{'-'*4}>\n{'-'*25}")# print out the Replenish_item
    for item in Replenish_item: 
        print(f"ID Code:{item[0]}")
        print(f"Item Name:{item[1]}")
        print(f"Quantity:{item[5]}")
        print(f"Expected Quanity:{item[6]}")
        print(f"{'-'*25}")

def ReplenishItem():
    while True:   
        print(f"<{'-'*4}Replenish Item List Menu{'-'*4}>")
        try:
            userinput = int(input("1.Add Quantity\n0.Return to Main Menu\n"))
            break
        except ValueError:
            print("Please Enter Numbers")
            clearConsole(1.5)
            
    if userinput == None:
        ReplenishItem()         
          
    if userinput == 1:
        clearConsole(0.2)
    elif userinput == 0:
        LoadMenu()
    else:
        print("Enter Value 1 or 0 ")
        clearConsole(1.5)
        ReplenishItem()
    
    while True:
        while True:
            for item in inventory:
                print(f"ID Code:{item[0]}")
                print(f"Item Name:{item[1]}")
                print(f"Quantity:{item[5]}")
                print(f"Expected Quanity:{item[6]}")
                print(f"{'-'*25}")

            try:
                userinput = int(input("\nEnter Code ID:"))
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
        
        while True:
            clearConsole(0.2)
            print(f"<{'-'*4}Item Details{'-'*4}>")
            print(f"ID Code:{item[0]}")
            print(f"Item Name:{item[1]}")
            print(f"Quantity:{item[5]}\n")
            
            try:
                userinput = int(input("1.Add Item\n0.Return to Main Menu\n"))            
                if userinput == 0 or userinput == 1:
                    break
                else:
                    print("Input only allow 1 or 0")
                    time.sleep(0.6)
            except ValueError:
                print("Enter Only Number")
                time.sleep(0.6)
                
        if userinput == 0:
            print("Returning to Main Menu...")
            LoadMenu()
            
        if userinput == 1:
            while True:
                try:
                    addQuantity = int(input("Please state amount to add:"))
                    break
                except ValueError:
                    print("Enter Only Number")
                    
                    
            while True:        
                clearConsole(0.2)
                print(f"<{'-'*4}Item Details{'-'*4}>")
                print(f"ID Code:{item[0]}")
                print(f"Item Name:{item[1]}\n")
                print(f"<{'-'*4}Item Changes{'-'*4}>")
                print(f"Old Quantity:{item[5]}")
                newQuanity = int(item[5]) + addQuantity
                print(f"New Quantity:{newQuanity}")
            
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
                
            if confirm == 1:
                NewItemRaw = f"{item[0]}/{item[1]}/{item[2]}/{item[3]}/{item[4]}/{newQuanity}/{item[6]}\n"
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
                time.sleep(1)
                LoadMenu()
                

def admin(username): # Admin-Level Consoles
    readInventory()
    option = 0
    menu = f"""
Welcome, {username}
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
            option = int(input("Select an option above: "))
        except ValueError:
            print("Enter Number Only")
        
        if option == -1:
            print("Program will be exiting soon..")
            time.sleep(3)
            exit()
            
        if option <= 0 or option >= 9:
            print("Please enter an option between 1 to 8")
            time.sleep(1)
            # After the user input the worng value, it will reprint the menu screen
        else:
            break

    match option:
        case 1:
            clearConsole(2)
            insert()
        case 4:
            clearConsole(2)
            stockTaking()
        case 5:
            clearConsole(2)
            ReplenishList()
        case 6:
            clearConsole(2)
            ReplenishItem()
        case 8:
            clearConsole(2)
            addUser()  
        case _:
            print("Invalid")
            LoadMenu()


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
    match UserDatas[1]:
        case 0:
            admin(username=UserDatas[0])
        case 1:
            print("Invi")
        case 2:
            print("Purc")

"""
VERSIONCHECKER WILL RUN 1ST NO MATTER WHAT!
"""
inventory = []
V = VERSIONCHECKER() # If the version is 3.10 above, will return FALSE    
UserDatas = startupFirstLogin() # Userdata consist of 2 main data, username and auth level
LoadMenu()

# else:
#     if loginSuccess[1] == 0:
#         admin(V=V)
#     elif loginSuccess[1] == 1:
#         pass
#     elif loginSuccess[1] == 2:
#         pass
