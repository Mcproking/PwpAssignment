#delete
def cancel_delete():
    print("Cancelled")
    print("Back to menu...")

def delete():
    master_delete_list = []
    while True:
        try:
            try:
                delete_code = int(input("Enter the item code to delete or enter '-1' to cancel: "))
                if delete_code == -1:
                    cancel_delete()
                    break
                elif delete_code < 0:
                    print("Please enter a valid code.")
                else:
                    with open("./Database/inventory.txt", "r") as f:
                        f.seek(0)
                        for line in f.readlines():
                            itemDetails = line.strip().split("/")
                            master_delete_list.append(itemDetails)
            except ValueError:
                print("Please enter a valid code.")
        except FileNotFoundError:
            print("File not found.")
        except IOError:
            print("Error occurred.")
        except Exception as e:
            print("Error occurred:", str(e))
delete()                       


#update
def cancel_update():
        print("Cancelled")
        print("Back to menu..") 

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
                return price_up
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

def update():
    master_update_list = []
    
    while True:
        try:
            try:
                item = int(input("Enter the code of the item that you want to update or enter '-1' to cancel: "))
                if item == -1:
                    cancel_update()
                    break
                elif item < 0:
                    print("Please enter a valid code.")
                else:
                    with open("./Database/inventory.txt", "r") as f:
                        f.seek(0)
                        read = f.readlines()
                        for line in read:
                            itemDetails = line.strip().split("/")
                            master_update_list.append(itemDetails)
                        for items in master_update_list:
                            if int(items[0]) == item:
                                print("\nItem details:")
                                print(items, end = "\n")
                                oldItems = f"{items[0]}/{items[1]}/{items[2]}/{items[3]}/{items[4]}/{items[5]}/{items[6]}"
                                updateOption = update_options()
                            
                                if updateOption == -1:
                                    break

                                elif updateOption == 1:
                                    code_up = code_update()
                                    items[0] = code_up
                                    updatedItem = f"{items[0]}/{items[1]}/{items[2]}/{items[3]}/{items[4]}/{items[5]}/{items[6]}"
                                    with open("./Database/inventory.txt", "w") as f:
                                        for line in read:
                                            if line.strip("\n") != oldItems:
                                                f.write(line)
                                        f.write(updatedItem + "\n")
                                    print("Item code updated successfully.")

                                elif updateOption == 2:
                                    description_up = description_update()
                                    items[1] = description_up
                                    updatedItem = f"{items[0]}/{items[1]}/{items[2]}/{items[3]}/{items[4]}/{items[5]}/{items[6]}"
                                    with open("./Database/inventory.txt", "w") as f:
                                        for line in read:
                                            if line.strip("\n") != oldItems:
                                                f.write(line)
                                        f.write(updatedItem + "\n")
                                    print("Item description updated successfully.")

                                elif updateOption == 3:
                                    category_up = category_update()
                                    items[2] = category_up
                                    updatedItem = f"{items[0]}/{items[1]}/{items[2]}/{items[3]}/{items[4]}/{items[5]}/{items[6]}"
                                    with open("./Database/inventory.txt", "w") as f:
                                        for line in read:
                                            if line.strip("\n") != oldItems:
                                                f.write(line)
                                        f.write(updatedItem + "\n")
                                    print("Item category updated successfully.")

                                elif updateOption == 4:
                                    unit_up = unit_update()
                                    items[3] = unit_up
                                    updatedItem = f"{items[0]}/{items[1]}/{items[2]}/{items[3]}/{items[4]}/{items[5]}/{items[6]}"
                                    with open("./Database/inventory.txt", "w") as f:
                                        for line in read:
                                            if line.strip("\n") != oldItems:
                                                f.write(line)
                                        f.write(updatedItem + "\n")
                                    print("Item unit updated successfully.")

                                elif updateOption == 5:
                                    price_up = price_update()
                                    items[4] = price_up
                                    updatedItem = f"{items[0]}/{items[1]}/{items[2]}/{items[3]}/{items[4]}/{items[5]}/{items[6]}"
                                    with open("./Database/inventory.txt", "w") as f:
                                        for line in read:
                                            if line.strip("\n") != oldItems:
                                                f.write(line)
                                        f.write(updatedItem + "\n")
                                    print("Item price updated successfully.")

                                else:
                                    minimum_up = minimum_update()
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
                                break
                        if updateOption == -1:
                            cancel_update()
                            break
            except ValueError:
                print("Please enter a valid code.")
            
            while True:
                choose_up = str(input("Do you still want to update more items? Enter Y for Yes or N for No: "))
                if choose_up.upper() != "Y" and choose_up.upper() != "N":
                    print("Please enter Y or N.")
                else:
                    break
            if choose_up.upper() == "Y":
                update()
            else:
                print("Item(s) have been updated successfully.")
                print("Back to menu...")
            break
        except FileNotFoundError:
            print("File not found.")
        except IOError:
            print("Error occurred.")
        except Exception as e:
            print("Error occurred:", str(e))
                       


#Insert
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


