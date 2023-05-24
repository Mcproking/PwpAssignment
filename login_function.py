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





logincheck(username = "Clement",password = "123")