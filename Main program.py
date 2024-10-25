def load_user_pass():
    user_pass = {}
    with open("User_password_save.txt", "r") as file:
        for line in file:
            if "," in line:
                user, password = line.strip().split(",")
                user_pass[user] = password
    return user_pass
     



def signup(user_pass):
    user = input("Username: ")
    password = input("Password: ")
    if user in user_pass:
        print("User ID already exists. Please choose another one")
        return
    else :
        with open("User_password_save.txt", "a") as save_userpass:
                  save_userpass.write("\n" + user + "," + password)


     
     
    

    
def login(user_pass):
    print ("\n\n1 : Login ")
    print ("2 : Forget Password")
    n = int (input ("Enter choice : "))
    
    match (n):
        case 1 :

             
            
            user = input ("Username : ")
            password = input ("Password : ")
            if user in user_pass and user_pass[user] == password:
                
                s = "Login Successfully"
                print ("\n")
                print (s.center(30 , "*"))
                return user
                 

            else :
                print ("\nInvalid User Id and Password")
                return None

                

        case 2 :
            user = input ("Enter User Id : ")

            if user in user_pass :
                print ("Your password is : " , user_pass[user])

            else :
                print ("User not found")
            return None 


def Movie_list() :
    movie1 = "JAWAN"
    movie2 = "TIGER 3"
    movie3 = "12th FAIL"
    movie4 = "HI PAPA"
    movie5 = "GADER 2"

    print ("\n\n***************************** MOVIE LIST *******************************\n\n")
    print (movie1.center(70 , " "))
    print ("\n")
    print (movie2.center(70 , " "))
    print ("\n")
    print (movie3.center(70 , " "))
    print ("\n")
    print (movie4.center(70 , " "))
    print ("\n")
    print (movie5.center(70 , " "))
    print ("\n")
    

def Book_ticket(username):
    import random 

    print ("\n\n")
    date = input ("Enter date : ")
    print ("\n\n")
    theater_name = input ("Enter theater name : ")

    print ("\n\n\n")
    print ("*************** MOVIE CHOICE ***************\n")
    print ("1 : JAWAN")
    print ("2 : TIGER 3")
    print ("3 : 12th FAIL")
    print ("4 : HI PAPA")
    print ("5 : GADER 2")
    movie_choice = int (input ("Enter choice : "))

    if (movie_choice == 1):
        book_movie ="JAWAN"

    elif (movie_choice == 2):
        book_movie = "TIGER 3"

    elif (movie_choice == 3):
        book_movie = "12th FAIL"

    elif (movie_choice == 4):
        book_movie = "HI PAPA"

    elif (movie_choice == 5):
        book_movie ="GADER 2"

    else :
        print ("Enter valid choice")

    print ("\n\n\n")
    no_person = int (input("No of person : "))

    
    print ("\n\n\n")
    print ("*************** TIME **************\n")
    time1 = "1 : 10:00 AM - 12:00 PM"
    time2 = "2 : 2:00 PM - 4:00 PM"
    time3 = "3 : 6:00 PM - 8:00 PM"
    time4 = "4 : 9:00 PM - 11:00 PM"
    print (time1.center(35 , " "))
    print (time2.center(35 , " "))
    print (time3.center(35 , " "))
    print (time4.center(35 , " "))
    time = int (input ("Enter choice : "))
    if (time == 1):
        book_time = "10:00 AM - 12:00 PM"
    elif (time == 2):
        book_time = "2:00 PM - 4:00 PM"
    elif (time == 3):
        book_time = "6:00 PM - 8:00 PM"
    elif(time == 4):
        book_time = "9:00 PM - 11:00 PM"
    else :
        print ("Enter valid option")

    print ("\n\n\n")

    print ("*************** SEAT POSITION ***************\n")
    pos1 = "1 : Front row - middle view : $10 "
    pos2 = "2 : Front row - side view : $9"
    pos3 = "3 : Middle row - middle view : $8"
    pos4 = "4 : Middle row - side view : $7"
    pos5 = "5 : Last row - middle view : $6"
    pos6 = "6 : Last row - side view : $5"
    print (pos1.center(50 , " "))
    print (pos2.center(50 , " "))
    print (pos3.center(50 , " "))
    print (pos4.center(50 , " "))
    print (pos5.center(50 , " "))
    print (pos6.center(50 , " "))
    sit = int (input ("Enter choice : "))
    if (sit == 1):
        book_sit = "Front row - middle view"

    elif (sit == 2):
        book_sit = "Front row - side view "

    elif (sit == 3):
        book_sit = "Middle row - middle view"
        
    elif (sit == 4):
        book_sit = "Middle row - side view"
        
    elif (sit == 5):
        book_sit = "Last row - middle view"
        
    elif (sit == 6):
        book_sit = "Last row - side view"

    else :
        print ("Enter valid option")

     

    print ("\n\n\n")

    print ("*************** PROCEED TO PAYMENT ***************\n")
    found = 0
    if (book_sit == "Front row - middle view"):
        
        amt = no_person*10
        print ("Total Ammount : $" , amt)
        pay =(input ("Proceed Payment(y/n) ? : "))
        if (pay == "Y" or pay == "y"):
            print ("Payment successfull")
            seat_nos = random.sample(range(15,30) ,no_person)
            found = 1

        else :
            print ("Payment faild")
            found = 0

    elif ( book_sit == "Front row - side view"):
        amt = no_person * 9
        print ("Total Ammount : $" ,amt)
        pay =(input ("Proceed Payment(y/n) ? : "))
        if (pay == "Y" or pay == "y"):
            print ("Payment successfull")
            seat_nos = random.sample(range(1,15) ,no_person)
            found = 1 

        else :
            print ("Payment faild")
            found = 0

        
    elif ( book_sit == "Middle row - middle view"):
        amt = no_person * 8
        print ("Total Ammount : $" ,amt)
        pay =(input ("Proceed Payment(y/n) ? : "))
        if (pay == "Y" or pay == "y"):
            print ("Payment successfull")
            seat_nos = random.sample(range(30,45) ,no_person)
            found =1 

        else :
            print ("Payment faild")
            found = 0

            
    elif ( book_sit == "Middle row - side view"):
        amt = no_person * 7
        print ("Total Ammount : $" ,amt)
        pay =(input ("Proceed Payment(y/n) ? : "))
        if (pay == "Y" or pay == "y"):
            print ("Payment successfull")
            seat_nos = random.sample(range(45,60) ,no_person)
            found = 1 

        else :
            print ("Payment faild")
            found = 0

    elif ( book_sit == "Last row - middle view"):
        amt = no_person * 6
        print ("Total Ammount : $" ,amt)
        pay =(input ("Proceed Payment(y/n) ? : "))
        if (pay == "Y" or pay == "y"):
            print ("Payment successfull")
            seat_nos = random.sample(range(60,75) ,no_person)
            found = 1 

        else :
            print ("Payment faild")
            found = 0

    elif ( book_sit == "Last row - side view"):
        amt = no_person * 5
        print ("Total Ammount : $" ,amt)
        pay =(input ("Proceed Payment(y/n) ? : "))
        if (pay == "Y" or pay == "y"):
            print ("Payment successfull")
            seat_nos = random.sample(range(75,90) ,no_person)
            found = 1 

        else :
            print ("Payment faild")
            found = 0


    ticket_no = random.randint(10000000 , 20000000)
    if(found == 1):
        print ("\n\n\n\n\n")
        print ("****************************** TICKET ******************************\n")

        print ("                  TICKET NO    : " , ticket_no)
        print ("                  THEATER      : " ,theater_name)
        print ("                  MOVIE        : " , book_movie)
        print ("                  DATE         : " , date)
        print ("                  TIME         : " ,book_time)
        print ("                  NO OF PERSON : " , no_person)
        print ("                  TOTAL PRICE  : " , amt)
        print ("                  SEAT NO      : " , seat_nos)
        print ("\n\n                  Thanks for booking . Have a nice show\n\n")
        print ("\n\n\n********************************************************************")

        save_booking_history = f"{username}_booking_history.txt"
        with open(save_booking_history, "a") as file:
             file.write("\n\n" + "Ticket no : " +str(ticket_no) +"\n" + "Theater : " + theater_name + "\n" + "Movie : "+book_movie + "\n" + "Date : " + date)
             file.write ("\n" + "Time : " + book_time + "\n" + "No of person : "+ str(no_person) + "\n" + "Total price :$" + str(amt) + "\n" + "Seat no : " + str(seat_nos))


    else :
        print ("\n\nFirst do payment\n\n")



    
            
def Booking_history(username):
    import os
    file_path = f"{username}_booking_history.txt"

    if os.path.exists(file_path):
        with open(file_path, 'r') as booking:
            lines = booking.readlines()
            if lines:
                for line in lines:
                    print(line)
            else:
                print("Empty Booking History")
    else:
        print("Empty Booking History")



def Feedback_review(username):

    feedback = input ("Feedback : ")
    feedback_save = f"{username}_booking_history.txt"

    with open(feedback_save , "a") as feedback_review :
        feedback_review.write("\n" + "Your Feedback : " + feedback) 
    


    
        

user_pass = load_user_pass()       
while True :
    print ("\n\n")
    print ("1 : Sign Up ")
    print ("2 : Login")
    print ("3 : Exit")
    c = int (input ("Enter choice : "))
    print ("\n\n")

    match (c):
        case 1:
            
            signup(user_pass)

        case 2:
            username = login(user_pass)
            if (username):
              while(True):
                 print ("\n\n")
                 print ("1 : Current Movie List")
                 print ("2 : Book Ticket")
                 print ("3 : Booking History")
                 print ("4 : Feedback and Review")
                 print ("5 : Logout")
                 print ("\n\n")
                 n = int (input ("Enter choice : "))

                 match (n):
                     case 1:
                         Movie_list()

                     case 2:
                         Book_ticket(username)

                     case 3 :
                         Booking_history(username)

                     case 4 :
                         Feedback_review(username)

                     case 5 :
                          break

                     case _ :
                         print ("Please enter valid option")


        case 3 :
            break

        case _ :
            print ("Choose valid option")
        
            
