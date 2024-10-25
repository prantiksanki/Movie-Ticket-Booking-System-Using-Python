def load_user_pass():
    fobj = open ("User_password_save.txt", "a")
    fobj.write("")
    fobj.close()
    user_pass = {}
    with open("User_password_save.txt", "r") as file:
        for i in file :
          lines = i.strip().split(",")
          user_pass[lines[0]] = lines[1]

    return user_pass
     
