import os
import time

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

def login():
    username = str(input("Enter your username: "))
    password = str(input("Enter your password: "))
    return username, password

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
        print("Username or Password Incorrect")



def main():
    userInput = login()
    logincheck(userInput[0],userInput[1])


main()