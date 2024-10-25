def signup(user_pass):
    user = input("Username: ")
    password = input("Password: ")
    if user in user_pass:
        print("User ID already exists. Please choose another one")
        
    else :
        with open("User_password_save.txt", "a") as save_userpass:
                  save_userpass.write("\n" + user + "," + password)
                  user_pass[user] = password

