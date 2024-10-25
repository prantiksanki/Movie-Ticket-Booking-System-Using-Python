###########################   USER   ############################


class login:
    def load_user_pass(self):
     fobj = open ("User_password_save.txt", "a")
     fobj.write("")
     fobj.close()
     user_pass = {}
     with open("User_password_save.txt", "r") as file:
        for i in file :
          lines = i.strip().split(",")
          user_pass[lines[0]] = lines[1]

     return user_pass

     
    def login(self , user_pass):
     print ("\n\n1 : Login ")
     print ("2 : Forgot Password")
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


class signUp:
    def signup(self , user_pass):
     user = input("Username: ")
     password = input("Password: ")
     if user in user_pass:
        print("User ID already exists. Please choose another one")
        
     else :
        with open("User_password_save.txt", "a") as save_userpass:
                  save_userpass.write("\n" + user + "," + password)
                  user_pass[user] = password



class movieAvl:
  def Movie_list(self) :
    import os
    if (os.path.exists("movie_list.txt")):
        fobj = open ("movie_list.txt" , "r")
        s = " HOT MOVIES FOR YOU "
        print (s.center(70 , "*"))
        for i in fobj.readlines() :
          parts= i.split(",")
          showtime = f"{parts[1][0:2]}:{parts[1][2:4]}:{parts[1][4:8]}-{parts[1][12:14]}:{parts[1][14:16]}:{parts[1][16:20]}"
          date = f"{parts[2][0:2]}/{parts[2][3:5]}/{parts[2][6:10]}"
          print ("\n")
          print ("              \t\t Movie    : " , parts[0])
          print ("              \t\t Showtime : " , showtime)
          print ("              \t\t Date     : " , date)
          print ("\n")

        fobj.close ()

    else :
        print ("\n\nNo movie added")




class feedback:
  def Feedback_review(self , username):
    import os
    if (os.path.exists(f"{username}_booking_history.txt")):
       feedback = input ("Feedback : ")
       feedback_save = f"{username}_booking_history.txt"

       with open(feedback_save , "a") as feedback_review :
        feedback_review.write("\n" + "Your Feedback : " + feedback) 


     

class book(feedback):
  def Book_ticket(self , username):
    import os
    import random
    dictionary = {}

    with open("movie_list.txt", "r") as fobj:
      for line in fobj:
        parts = line.split(",")
        movie_name = parts[0]
        show_time = f"{parts[1][0:2]}:{parts[1][2:4]}:{parts[1][4:8]}-{parts[1][12:14]}:{parts[1][14:16]}:{parts[1][16:20]}"
        date = f"{parts[2][0:2]}/{parts[2][3:5]}/{parts[2][6:10]}"
        

        if movie_name in dictionary:
             dictionary[movie_name].append((date, show_time))
        else:
             dictionary[movie_name] = [(date, show_time)]


    print("Available Movies:")
    for movie_name, date_times in dictionary.items():
      print(f"\n-> {movie_name}:")
      for date, showtime in date_times:
        print(f"   - {date} at {showtime}")

        movie_found = 0
        
    dictionary_price = {}
    selected_movie = input("Enter the name of the movie you want to book: ")
    selected_date = input ("DATE(format-DDMMYYYY): ")
    selected_show_time = input("SHOWTIME(format-HH:MM:SSAM-HH:MM:SSPM): ")
    date = f"{selected_date[0:2]}_{selected_date[2:4]}_{selected_date[4:8]}"
    show_time = f"{selected_show_time[0:2]}{selected_show_time[3:5]}{selected_show_time[6:10]}_to_{selected_show_time[11:13]}{selected_show_time[14:16]}{selected_show_time[17:22]}"

    
    fpath = f"{selected_movie}_{date}_{show_time}_sit_price.txt"
    print(fpath)
    if os.path.exists(fpath):
          print("\n\n:::::::::::::::::::: PRICES ::::::::::::::::::::\n")
          with open(fpath, "r") as file1:
           
             for line in file1:
                parts = line.split(",")
                dictionary_price[parts[0]]= parts[1]
                print(f"{parts[0]} : Rs {parts[1]}")
                movie_found = 1
    else:
          print("\nEnter valid movie name or date or showtime")
          movie_found = 0
        

    
    if (movie_found == 1):
        print ("\n\n1. Front Sit")
        print("2. Middle Sit")
        print ("3. Last sit")
        choose_sit = int (input ("Choose option : "))

        match (choose_sit):

           case 1:
               book_price_per_sit = int(dictionary_price["front"])
            

           case 2:
               book_price_per_sit = int(dictionary_price["middle"])

           case 3:
               book_price_per_sit = int(dictionary_price["last"])

           case _:
               print ("Enter valid option")

       
    if(movie_found == 1):
        no_person = int (input("No of person : "))
        become = 0

        match (choose_sit):

           case 1:
               book_tickets = []
               modified_line = []
               fobj4 = open (f"{selected_movie}_{date}_{show_time}_sit_arrangement_front.txt" , "r")
               line = fobj4.readlines ()
               if not line :
                   print ("Unavlaible sit")
                    
                    
               else :
                   for i in line:
                      seat_nos = i.split (",")
                      for j in seat_nos:
                         modified_line.append(j)

               become = 0
            
               total_available_seats = (len(modified_line)-1)


               if no_person > total_available_seats:
                  print ("\n")
                  print(f"Only {total_available_seats} seats is available.")
                  no_person = total_available_seats
                  become = 1
               else :
                   
                  for k in range(no_person):
                     if modified_line:
                       k = modified_line.pop(0)
                       book_tickets.append(k)

                     with open(f"{selected_movie}_{date}_{show_time}_sit_arrangement_front.txt", "w") as fobj5:
                        fobj5.write(",".join(modified_line)) 
                  
               

           case 2:
               book_tickets = []
               modified_line = []
               fobj4 = open (f"{selected_movie}_{date}_{show_time}_sit_arrangement_middle.txt" , "r")
               line = fobj4.readlines ()
               if not line :
                   print ("Unavlaible sit")
                    
               else :
                   for i in line:
                      seat_nos = i.split (",")
                      for j in seat_nos:
                         modified_line.append(j)

               become = 0

            
               total_available_seats = len(modified_line)

               if no_person > total_available_seats:
                  print(f"Only {(len(modified_line)-1)} sits is available.")
                  become = 1
               else :
                   
                   for k in range(no_person):
                      if modified_line:
                        k = modified_line.pop(0)
                        book_tickets.append(k)

                      with open(f"{selected_movie}_{date}_{show_time}_sit_arrangement_middle.txt", "w") as fobj5:
                         fobj5.write(",".join(modified_line))             

           case 3:
               book_tickets = []
               modified_line = []
               fobj4 = open (f"{selected_movie}_{date}_{show_time}_sit_arrangement_last.txt" , "r")
               line = fobj4.readlines()
               if not line :
                   print ("Unavlaible sit")
                
                   
               else :
                   for i in line:
                      seat_nos = i.split (",")
                      for j in seat_nos:
                         modified_line.append(j)
               become = 0
            
               total_available_seats = len(modified_line)

               if no_person > total_available_seats:
                  print(f"Only {(len(modified_line)-1)} sits is available.")
                  become = 1
               else :  

                   for k in range(no_person):
                      if modified_line:
                         k = modified_line.pop(0)
                         book_tickets.append(k)

                   with open(f"{selected_movie}_{date}_{show_time}_sit_arrangement_last.txt", "w") as fobj5:
                           fobj5.write(",".join(modified_line))

               

           case _:
               print ("Enter valid option")
               

        



    else :
        pass
    found = 1
    if(movie_found == 1):
        book_total_price = (no_person * book_price_per_sit)

        print ("\n\n\n")
        if (become == 0):
           print ("*************** PROCEED TO PAYMENT ***************\n")
           print ("Total bill : " ,book_total_price)
           pay =(input ("Proceed Payment(y/n) ? : "))
           if (pay == "Y" or pay == "y"):
               print ("Payment successfull")
               found = 1

           else :
               print ("Payment faild")
               found = 0 

        else :
           print ("Sorry ! no seat avlaible")
   
        ticket_no = random.randint(10000000 , 20000000)
        if(found == 1 and become == 0):
           print ("\n\n\n\n\n")
           print ("****************************** TICKET ******************************\n")
           welcome = " WELCOME TO WELCOME TO MAJESTIC CINAME"
           welcome1 = "gateway to cinematic briliance"
           print ("\n\n")
           print (welcome.center(65 , " "))
           print (welcome1.center(65 , " "))
           print ("\n")
           print ("                  TICKET NO    : " , ticket_no)
           print ("                  MOVIE        : " , selected_movie)
           print ("                  DATE         : " , selected_date)
           print ("                  TIME         : " ,selected_show_time)
           print ("                  NO OF PERSON : " , no_person)
           print ("                  TOTAL PRICE  :  Rs " , book_total_price)
           print ("                  SEAT NO      : " , book_tickets)
           print ("\n\n                  Thanks for booking . Have a nice show\n\n")
           print ("\n\n\n********************************************************************")

           save_booking_history = f"{username}_booking_history.txt"
           with open(save_booking_history, "a") as file:
                file.write ("\n\n"+"-----------------------------------------------------------------")
                file.write("\n" + "Ticket no : " +str(ticket_no)+ "\n" + "Movie : "+selected_movie + "\n" + "Date : " +selected_date)
                file.write ("\n" + "Time : " + selected_show_time+ "\n" + "No of person : "+ str(no_person) + "\n" + "Total price :Rs " + str(book_total_price) + "\n" + "Seat no : " + str(book_tickets))
                file.write ("\n"+"-----------------------------------------------------------------")
           with open("total_tickets_book.txt", "a") as fobj:
                fobj.write ("\n\n"+"-----------------------------------------------------------------")
                fobj.write("\n" + "Ticket no : " + str(ticket_no) + "\n" + "Movie : " + selected_movie + "\n" + "Date : " + selected_date)
                fobj.write("\n" + "Time : " + selected_show_time + "\n" + "No of person : " + str(no_person) + "\n" + "Total price :Rs " + str(book_total_price) + "\n" + "Seat no : " + str(book_tickets))
                fobj.write ("\n"+"-----------------------------------------------------------------")




   


class history:
  def Booking_history(self , username):
    import os
    file_path = f"{username}_booking_history.txt"
    his = " History "
    print (his.center(60 , "*"))

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


class cancel:
  def cancel_ticket(self , username):
    import os 
    selected_movie = input("Enter the name of the movie you want to book: ")
    selected_date = input ("DATE(format-DDMMYYYY): ")
    selected_show_time = input("SHOWTIME(format-HH:MM:SSAM-HH:MM:SSPM): ")
    date = f"{selected_date[0:2]}_{selected_date[2:4]}_{selected_date[4:8]}"
    show_time = f"{selected_show_time[0:2]}{selected_show_time[3:5]}{selected_show_time[6:10]}_to_{selected_show_time[11:13]}{selected_show_time[14:16]}{selected_show_time[17:22]}"
    no_person = int (input ("Enter no of person : "))
    print ("\nSelect the seat position :")
    print ("\n1.Front")
    print ("2.Middle")
    print ("3.Last")
    choose_sit = int(input ("Enter option : "))
    match(choose_sit):
        case 1:
            fname = f"{selected_movie}_{date}_{show_time}_sit_arrangement_front.txt"
            if (os.path.exists(fname)):
              fobj = open (fname , "a")
              for i in range (no_person):
                seat_no = input ("Enter seat no : ")
                fobj.write(seat_no + ",")

              fobj.close()
              print ("\nCancel seccessfull\n")

            else :
                print("No such movie available")


        case 2:
            fname = f"{selected_movie}_{date}_{show_time}_sit_arrangement_middle.txt"
            if (os.path.exists(fname)):
              fobj = open (fname , "a")
              for i in range (no_person):
                seat_no = input ("Enter seat no : ")
                fobj.write(seat_no + ",")

              fobj.close()
              print ("\nCancel seccessfull\n")

            else :
                print ("No such movie available")
                


        case 3:
            fname = f"{selected_movie}_{date}_{show_time}_sit_arrangement_last.txt"
            if (os.path.exists(fname)):
              fobj = open (fname , "a")
              for i in range (no_person):
                seat_no = input ("Enter seat no : ")
                fobj.write(seat_no + ",")

              fobj.close()
              print ("\nCancel seccessfull\n")

            else :
                print ("No such movie available")






l = login()
s = signUp()
m = movieAvl()
b = book()
h = history()
c = cancel()
#f = feedback()


user_pass = l.load_user_pass()
welcome = "WELCOME TO MAJESTIC CINAME"
welcome1 = "gateway to cinematic briliance"
print ("\n\n")
print (welcome.center(70 , " "))
print (welcome1.center(70 , " "))
while True :
    print ("\n\n")
    print ("1 : Sign Up ")
    print ("2 : Login")
    print ("3 : Exit")
    c = int (input ("Enter choice : "))
    print ("\n\n")

    match (c):
        case 1:
            
           s.signup(user_pass)

        case 2:
            username = l.login(user_pass)
            if (username):
              while(True):
                 print ("\n\n")
                 print ("1 : Current Movie List")
                 print ("2 : Book Ticket")
                 print ("3 : Booking History")
                 print ("4 : Feedback and Review")
                 print ("5 : Cancel Ticket")
                 print ("6 : Logout")
                 print ("\n\n")
                 n = int (input ("Enter choice : "))

                 match (n):
                     case 1:
                         m.Movie_list()

                     case 2:
                         b.Book_ticket(username) 

                     case 3 :
                         h.Booking_history(username)

                     case 4 :
                         b.Feedback_review(username)

                     case 5:
                         c.cancel_ticket(username)

                     case 6 :
                          break

                     case _ :
                         print ("Please enter valid option")


        case 3 :
            break

        case _ :
            print ("Choose valid option")
        
            

