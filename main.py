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
# IMPORTANT!!! DEFUALT TIMER IS 5 SECOND, NEED FOR LONGER ENTER THE VALUE
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


def login(): # Login Page with user Indentification
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
                print(f"\nPlease confirm with the user details\n\nUsername: {username}\nPassword: {password}\nAsscess Level: {role}")
                finalconfirm = input("\nAre You confirm with the details above? Y/N ")
                
                if finalconfirm.upper() == "Y": # Insert the value into login.txt
                    break
                elif finalconfirm.upper() == "N":
                    reset = input("Reset Input? Y/N ") # Check if user want to reset the input data or not
                    if reset.upper() == "N":
                        print("Cancelled Creation.. Returning to menu")
                        clearConsole(2)
                        LoadMenu()
                    elif reset.upper() == "Y":
                        print("Resting User Creation..")
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

def admin(username): # Admin-Level Consoles
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
            os.sleep(3)
            exit()
            
        if option <= 0 or option >= 9:
            print("Please enter an option between 1 to 8")
            os.sleep(1)
            # After the user input the worng value, it will reprint the menu screen
        else:
            break

    if not V:
        match option:
            case 1:
                print('Inser New item')
            case 8:
                clearConsole(2)
                addUser()  

def startupFirstLogin(): # only use this function once for the program to start
    loginSuccess = (False,-1)
    while not loginSuccess[0]:
        loginSuccess = login()
    if loginSuccess[0]:
        username = loginSuccess[2]
        auth = loginSuccess[1]
    return username,auth

def LoadMenu():
    if not V: # Need to ask lect if we can use match case or not.. 
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
