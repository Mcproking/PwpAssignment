# login in with username and password, then inside the database with the permission value consider 0,1,2. 0 = Admin, 1 = Inverntory checker, 2 = purcherser 
# ADMIN: ALL Tasks. 
# INVENTORY-CHECKER: STOCK TAKING, SEARCH ITEMS. 
# PURCHASER: VIEW REPLENISH LIST, STOCK REPLENISHMENT, and SEARCH ITEMS.  


def logincheck(username,password):
    Users = []
    with open("./Database/login.txt","r") as f:
        for line in f.readlines(): # read the txt line by line
            userDetails = line.strip().split("/") # remove the \n and "/"
            Users.append(userDetails)
    
    for user in Users:
        if user[0] == username and user[1] == password:
           print("Sucess") # prob make another function here
           break
    else:
        print("None of them correct")

# logincheck(username = "Clement",password = "123")

inventory = []

def readInventory():
    with open("./Database/inventory.txt") as f:
        for line in f.readlines(): # read the txt line by line
            # print(line)
            item = line.strip().split("/") # remove the \n and "/"
            inventory.append(item)

def stockTaking(restart = False): # Stock Taking | Auth = Admin/Inventory Checker
    def printitem():
        print(f"<{'-'*7}Item{'-'*7}>")
        print(f"Name: {item[1]}")
        print(f"Unit: {item[3]}")
        print(f"Quantity: {item[5]}")

    if restart:
        # ClearConsole()
        print(f"<{'-'*7}Stock Taking{'-'*7}>")
        print("0.Contiune\n1.Exit To Main Menu")
        while True:
            try:
                userinput = int(input())
                break
            except ValueError:
                print("Enter 0 or 1")
        if userinput == 1:
            return
        elif userinput == 0:
            pass
        
    while True:
        try:
            IdCode = int(input("Enter Item Code:"))
            break
        except ValueError:
            print("Worng Value")
    
    for item in inventory:
        if int(item[0]) == IdCode:
            print("Please Wait..")
            # Clearconsole()
            item = item
            oldItemRaw = f"{item[0]}/{item[1]}/{item[2]}/{item[3]}/{item[4]}/{item[5]}/{item[6]}"
            break
    else:
        print("Item do not exist..")
        stockTaking(restart=True)
            
    while True:
        printitem()
                    
        try:
            userinput = int(input("0. Contiune\n1. Change Quantity"))
            break
        except ValueError:
            print("Worng Value")
            # ClearConsole()
            
        if userinput == 0:
            return
        elif userinput == 1:
            break
        else:
            pass
        
    while True:
        #clearconsole()
        printitem()
        
        try:
            quantity = int(input("Enter the new Quantity:"))
        except ValueError:
            print("Enter Number Only")
        
        print(f"Quantity change from {item[3]} to {quantity}")
        #clearconsole()
        item[5] = quantity
        printitem()
        confirmation = int(input("\n1. Confirm 2. Cancel"))
        if confirmation == 2:
            print("Returning to Menu..")
            return
        if confirmation == 1:
            NewItemRaw = f"{item[0]}/{item[1]}/{item[2]}/{item[3]}/{item[4]}/{item[5]}/{item[6]}\n"
            
            with open("./Database/inventory.txt","r") as f:
                lines = f.readlines()
                
            with open("./Database/inventory.txt","w") as f:
                for line in lines:
                    if line.strip("\n") != oldItemRaw:
                        f.write(line)
                f.write(NewItemRaw)    
            return

# readInventory()
# stockTaking()

# print(inventory)