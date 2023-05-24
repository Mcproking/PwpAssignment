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
