import os
import hashlib
import getpass

#this text file stores users credentials.
userFile = 'users.txt'                              


#This function converts users passwords into hexdigits. 
def hashPassword(password):
    return hashlib.sha256(password.encode()).hexdigest()

#This function checks if the user exists.
def usersExists(username):
    if not os.path.exists(userFile):
        return False
    with open(userFile,'r') as file:
        return any(line.startswith((f"{username}:"))for line in file)
    
#This function allows users to register.
def register():
    username = input("Please enter your name: ")
    if usersExists(username):
        print("User already exists.")
        return
    
    password = getpass.getpass("enter your password")
    with open(userFile, "a") as f:
        f.write(f"{username}:{hashPassword(password)}\n")
    
    print("You have successfully registered \n","Now you may proceed to login")
    login()

#This function allows users to login.
def login():
    if not os.path.exists(userFile):
        print("Opps we have no user registered under this name.")
        
    username = input("Please enter your name: ")
    password = getpass.getpass("enter your password: ")
    hashed = hashPassword(password)
    
    with open(userFile,'r') as file:
        for line in file:
            if line.strip() == f"{username}:{hashed}":
                print("You have succsessfully logged in.")
                return
            
    return ("Login failed")
       
def main():
    options  = {"1": login, "2": register, "3":exit}
    
    while True:
        print("\n 1.login \n 2.Register \n 3.Exit")
        choice  = input("Please select an option: ")
        action = options.get(choice)
        if action:
            action()
            
        else:
            print("Invalid option please try again.")
            
            
if __name__ == "__main__":
    main()
    