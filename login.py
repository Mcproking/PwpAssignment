def cancel():
    print("Cancelling...")
    print("Cancelled")

def code():
    while True:
        try:
            code = int(input("Enter the code of the item or enter '-1' to cancel: "))
            if code == -1:
                cancel()
                return code
            else:
                return code
        except ValueError:
            print("Please enter an integer.")

def description():
    description = str(input("Enter the description of item {code} or enter '-1' to cancel: "))
    if description == -1:
        cancel()
        return description
    else:
        description = description.title()
        return description

def category():
    category = str(input("Enter the category of {description} or enter '-1' to cancel: "))
    if category == -1:
        cancel()
        return category
    else:
        category = category.title()
        return category

def unit():
    unit = str(input("Enter the unit of {description} or enter '-1' to cancel: "))
    if unit == -1:
        cancel()
        return unit
    else:
        unit = unit.title()
        return unit

def price():
    while True:
        try:
            price = float(input("Enter the price of {description} or enter '-1' to cancel: "))
            if price == -1:
                cancel()
                return price
            elif price <= 0:
                print("Please enter a valid price.")
            else:
                price = round(price, 2)
                return price
        except ValueError:
            print("Please enter a valid price.")

def quantity():
    while True:
        try:
            quantity = int(input("Enter the quantity in stock for {description} or enter '-1' to cancel: "))
            if quantity == -1:
                cancel()
                return quantity
            elif quantity < 0:
                print("Please enter a valid quantity.")
            else:
                return quantity
        except ValueError:
            print("Please enter a valid quantity.")

def minimum():
    while True:
        try:
            minimum = int(input("Enter the minimum threshold allowed for {description} or enter '-1' to cancel: "))
            if minimum == -1:
                cancel()
                return minimum
            elif minimum <= 0:
                print("Please enter a valid minimum threshold.")
            else:
                return minimum
        except ValueError:
            print("Please enter a valid minimum threshold.")

def insert():
    master_insert_list = []
    while True:
        code = code()
        if code == -1:
            break
        description = description()
        if description == -1:
            break
        category = category()
        if category == -1:
            break
        unit = unit()
        if unit == -1:
            break
        price = price()
        if price == -1:
            break
        quantity = quantity()
        if quantity == -1:
            break
        minimum = minimum()
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
            continue
        else:
            with open("inventory.txt", "a") as f:
                for item in master_insert_list:
                    for detail in item:
                        f.write(f"{detail[0]}/{detail[1]}/{detail[2]}/{detail[3]}/{detail[4]}/{detail[5]}/{detail[6]}")
            print("Item(s) have been inserted successfully.")
            break








def login():
    while True:
        username = str(input("Enter your username: "))
        password = str(input("Enter your password: "))
        
    return username, password

def addUser():
    username = str(input("Enter the new username: "))
    password = str(input("Enter the new password: "))
    while True:
        confirm = str(input("Confirm your password: "))
        if confirm != password:
            print("Your password is incorrect")
            print("Please re-enter your password")
        else:
            while True:
                print("""
Enter 0 for Admin
Enter 1 for Inventory-Checker
Enter 2 for Purchaser""")
                role = str(input("Enter the user type: "))
                if role < 0 or role > 2:
                    print("Please enter an option between 0 to 2")
                else:
                    break
            with open("login.txt", "a") as f:
                f.write(f"{username}/{password}/{role}")
            print("New user has been added")
            break
addUser()
            


def admin():
    while True:
        print("""
1. Insert New Item
2. Update Item
3. Delete Item
4. Stock Taking
5. View Replenish List
6. Stock Replenishment
7. Search Items
8. Add New User""")
        option = int(input("Select an option above: "))
        if option < 0 or option > 8:
            print("Please enter an option between 1 to 8")
        else:
            break
    if option == 1:
