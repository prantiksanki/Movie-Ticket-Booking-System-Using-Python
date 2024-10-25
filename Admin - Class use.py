######################   ADMIN   ########################


  
class View :
   def view_movies(self):
     try :
      import os
      if (os.path.exists("movie_list.txt")):
        fobj = open ("movie_list.txt" , "r")
        s = "MOVIE LIST"
        print (s.center(60 , "*"))
        for i in fobj.readlines() :
          parts= i.split(",")
          print ("\n")
          print ("Movie : " , parts[0])
          print ("Showtime : " , f"{parts[1][0:2]}:{parts[1][2:4]}:{parts[1][4:8]}-{parts[1][12:14]}:{parts[1][14:16]}:{parts[1][16:20]}")
          print ("Date : " , f"{parts[2][0:2]}/{parts[2][3:5]}/{parts[2][6:10]}")
          print ("\n")

      fobj.close ()

     except :
        print ("No movie available")


   def view_tickit(self):
    try:
     import os
     fpath = "total_tickets_book.txt"
     if os.path.exists(fpath):
        with open(fpath, "r") as fobj:
            for line in fobj:
                print(line.strip())
     else:
        print("No booking yet")

    except :
        print ("Something went wrong")


class viewSitting(View):
    def view_sitting(self):
      import os
      movie_name = input("Enter the name of the movie you want to book: ")
      selected_date = input ("DATE(format-DDMMYYYY): ")
      selected_show_time = input("SHOWTIME(format-HH:MM:SSAM-HH:MM:SSPM): ")
    
      date = f"{selected_date[0:2]}_{selected_date[2:4]}_{selected_date[4:8]}"
      show_time = f"{selected_show_time[0:2]}{selected_show_time[3:5]}{selected_show_time[6:10]}_to_{selected_show_time[11:13]}{selected_show_time[14:16]}{selected_show_time[17:22]}"

      fpath1=  f"{movie_name}_{date}_{show_time}_sit_arrangement_front.txt"
      fpath2 = f"{movie_name}_{date}_{show_time}_sit_arrangement_middle.txt"
      fpath3 = f"{movie_name}_{date}_{show_time}_sit_arrangement_last.txt"
      if os.path.exists(fpath1):

          file_name = f"{movie_name}_{date}_{show_time}_sit_arrangement_front.txt"
          fobj = open (file_name , "r")
          print ("\n::::::::::FRONT ROW ::::::::::::\n")
          print (fobj.readline())
          fobj.close
      else :
        print ("Invalid date or showtime. Please check again.")
        
      if os.path.exists(fpath2):
        
          file_name = f"{movie_name}_{date}_{show_time}_sit_arrangement_middle.txt"
          fobj = open (file_name , "r")
          print ("\n:::::::::: MIDDLE ROW ::::::::::::\n")
          print (fobj.readline())
          fobj.close
      else :
        print ("Invalid date or showtime. Please check again.")
        
      if os.path.exists(fpath3):
        
          file_name = f"{movie_name}_{date}_{show_time}_sit_arrangement_last.txt"
          fobj = open (file_name , "r")
          print ("\n:::::::::: LAST ROW ::::::::::::\n")
          print (fobj.readline())
          fobj.close

      else :
        print ("Invalid date or showtime. Please check again.")


    


class addMovie:
    
    def choice_option(self):
     while True :
       print("\n\n1. REMOVE ALL AND ADD FRESHLY")
       print("2. ADD MOVIE IN PREVIOUS LIST")
       print("3. GO TO MAIN OPTIONS")
       add_choice = int(input("Enter choice: "))
       match (add_choice):
           case 1:
               self.fresh_add()
            
           case 2:
               self.previous_add()
            
           case 3:
               break
        
           case _:
               print("Enter a valid choice")

    def remove_movie (self):
     import os
     if (os.path.exists("movie_list.txt")):
        fobj = open ("movie_list.txt" , "w")
        fobj.write ("")
        fobj.close ()
        print ("\nLIST OF MOVIE BECOMES EMPTY. NOW ADD MOVIES\n")
     else :
        print ("File not created")
     

    
    def fresh_add(self):
     import os
     if (os.path.exists("movie_list.txt")):
      self.remove_movie()   
      fobj = open("movie_list.txt", "a")

      n = int(input("NO OF MOVIES: "))
      for i in range(n):
        
        name = input("Movie Name : ")
        selected_date = input ("DATE(format-DDMMYYYY): ")
        selected_show_time = input("SHOWTIME(format-HH:MM:SSAM-HH:MM:SSPM): ")
    
        date = f"{selected_date[0:2]}_{selected_date[2:4]}_{selected_date[4:8]}"
        show_time = f"{selected_show_time[0:2]}{selected_show_time[3:5]}{selected_show_time[6:10]}_to_{selected_show_time[11:13]}{selected_show_time[14:16]}{selected_show_time[17:22]}"

        print("\n")
        fobj.write(name + "," + show_time + "," + date + "\n")
        print ("\n\n::::::::::::::::::::::::: SET PRICE ::::::::::::::::::::::::\n")
        file = open (f"{name}_{date}_{show_time}_sit_price.txt" , "w")
        front_price = input ("FRONT ROW : ")
        middle_price = input ("MIDDLE ROW : ")
        last_price = input ("LAST ROW : ")
        file.write ("front" + "," + front_price +"\n" + "middle" + "," + middle_price +"\n" + "last" + "," + last_price)
        file.close()
        
        while True:
            print("\n\n::::::::::::::::::::::: ALLOCATE SEATS ::::::::::::::::::::\n")
            print("1. FRONT ROW SEAT ADD")
            print("2. MIDDLE ROW SEAT ADD")
            print("3. LAST ROW SEAT ADD")
            print("4. EXIT")
            choose = int(input("Enter choice: "))

            if choose == 1:
                    file_name = f"{name}_{date}_{show_time}_sit_arrangement_front.txt"
                    fileobj = open(file_name, "w")
                    first = int(input("\nFRONT ROW - FIRST SEAT NO: "))
                    last = int(input("FRONT ROW - LAST SEAT NO: "))
                    for i in range(first, last + 1):
                        fileobj.write(str(i) + ",")

                    fileobj.close ()
                    
            elif choose == 2:
                    file_name = f"{name}_{date}_{show_time}_sit_arrangement_middle.txt"
                    fileobj = open(file_name, "w") 
                    first = int(input("\nMIDDLE ROW - FIRST SEAT NO: "))
                    last = int(input("MIDDLE ROW - LAST SEAT NO: "))
                    for i in range(first, last + 1):
                        fileobj.write(str(i) + ",")
                

                    
            elif choose == 3:
                    file_name = f"{name}_{date}_{show_time}_sit_arrangement_last.txt"
                    fileobj = open(file_name, "w") 
                    first = int(input("\nLAST ROW - FIRST SEAT NO: "))
                    last = int(input("LAST ROW - LAST SEAT NO: "))
                    for i in range(first, last + 1):
                         fileobj.write(str(i) + ",")
                    
            elif choose == 4:
                break
            else:
                print("Enter a valid option")

      fobj.close()



    def previous_add(self):
     import os
     if (os.path.exists("movie_list.txt")):
      fobj = open ("movie_list.txt" , "a")
      no = int (input ("NO OF MOVIES : "))
      for i in range (no):
         name = input("Enter the name of the movie you want to book: ")
         selected_date = input ("DATE(format-DDMMYYYY): ")
         selected_show_time = input("SHOWTIME(format-HH:MM:SSAM-HH:MM:SSPM): ")
    
         date = f"{selected_date[0:2]}_{selected_date[2:4]}_{selected_date[4:8]}"
         show_time = f"{selected_show_time[0:2]}{selected_show_time[3:5]}{selected_show_time[6:10]}_to_{selected_show_time[11:13]}{selected_show_time[14:16]}{selected_show_time[17:22]}"

         print ("\n")
         fobj.write (name + "," + show_time + "," + date + "\n")
         print ("\n\n::::::::::::::::::::::::: SET PRICE ::::::::::::::::::::::::\n")
         file = open (f"{name}_{date}_{show_time}_sit_price.txt" , "a")
         front_price = input ("FRONT ROW : ")
         middle_price = input ("MIDDLE ROW : ")
         last_price = input ("LAST ROW : ")
         file.write ("front" + "," + front_price +"\n" + "middle" + "," + middle_price +"\n" + "last" + "," + last_price)
         file.close()
         while True:
            print("\n\n::::::::::::::::::::::: ALLOCATE SEATS ::::::::::::::::::::\n")
            print("1. FRONT ROW SEAT ADD")
            print("2. MIDDLE ROW SEAT ADD")
            print("3. LAST ROW SEAT ADD")
            print("4. Exit")
            choose = int(input("Enter choice: "))

            if choose == 1:
                    file_name = f"{name}_{date}_{show_time}_sit_arrangement_front.txt"
                    fileobj = open(file_name, "w")
                    first = int(input("\nFRONT ROW - FIRST SEAT NO: "))
                    last = int(input("FRONT ROW - LAST SEAT NO: "))
                    for i in range(first, last + 1):
                        fileobj.write(str(i) + ",")

                    fileobj.close ()
               
            elif choose == 2:
                    file_name = f"{name}_{date}_{show_time}_sit_arrangement_middle.txt"
                    fileobj = open(file_name, "w") 
                    first = int(input("\nMIDDLE ROW - FIRST SEAT NO: "))
                    last = int(input("MIDDLE ROW - LAST SEAT NO: "))
                    for i in range(first, last + 1):
                        fileobj.write(str(i) + ",")
                        
            elif choose == 3:
                    file_name = f"{name}_{date}_{show_time}_sit_arrangement_last.txt"
                    fileobj = open(file_name, "w") 
                    first = int(input("\nLAST ROW - FIRST SEAT NO: "))
                    last = int(input("LAST ROW - LAST SEAT NO: "))
                    for i in range(first, last + 1):
                         fileobj.write(str(i) + ",")

            elif choose == 4:
                break
            else:
                print("Enter a valid option")


         fobj.close ()


class sitAdd:
    def add_sits(self) :
     import os
     movie_name = input("Enter the name of the movie you want to book: ")
     selected_date = input ("DATE(format-DDMMYYYY): ")
     selected_show_time = input("SHOWTIME(format-HH:MM:SSAM-HH:MM:SSPM): ")
    
     date = f"{selected_date[0:2]}_{selected_date[2:4]}_{selected_date[4:8]}"
     show_time = f"{selected_show_time[0:2]}{selected_show_time[3:5]}{selected_show_time[6:10]}_to_{selected_show_time[11:13]}{selected_show_time[14:16]}{selected_show_time[17:22]}"

     print ("\n1. FRONT SIT ADD")
     print ("2. MIDDLE SIT ADD")
     print ("3. LAST ROW ADD")
     choose = int (input ("Enter choice : "))
     match (choose):
        case 1:
            if (os.path.exists(f"{movie_name}_{date}_{show_time}_sit_arrangement_front.txt")):
               file_name = f"{movie_name}_{date}_{show_time}_sit_arrangement_front.txt"
               fobj = open (file_name , "a")
               no_sit = int (input ("ENTER NO OF SEATS YOU WANT TO ENTER : "))
               for i in range (no_sit):
                  sit = input ("ENTER SEAT NO : ")
                  fobj.write (sit + ",")

               fobj.close ()

        case 2:
            if (os.path.exists(f"{movie_name}_{date}_{show_time}_sit_arrangement_middle.txt")):
                
               file_name = f"{movie_name}_{date}_{show_time}_sit_arrangement_middle.txt"
               fobj = open (file_name , "a")
               no_sit = int (input ("ENTER NO OF SEATS YOU WANT TO ENTER : "))
               for i in range (no_sit):
                  sit = input ("ENTER SEAT NO : ")
                  fobj.write (sit + ",")

               fobj.close ()

        case 3:
            if (os.path.exists(f"{movie_name}_{date}_{show_time}_sit_arrangement_last.txt")):
                file_name = f"{movie_name}_{date}_{show_time}_sit_arrangement_last.txt"
                fobj = open (file_name , "a")
                no_sit = int (input ("ENTER NO OF SEATS YOU WANT TO ENTER : "))
                for i in range (no_sit):
                  sit = input ("ENTER SEAT NO : ")
                  fobj.write (sit + ",")

                fobj.close ()
           





while (True):
    
    print ("\n\n1. ADD MOVIE")
    print ("2. ADD SOME SEAT")
    print ("3. VIEW MOVIE LIST")
    print ("4. VIEW SITTING ARRANGEMENT")
    print ("5. VIEW TICKETS")
    print ("6. EXIT")
    choose = int (input ("Enter choice : "))
    v = viewSitting()
    a = addMovie()
    s = sitAdd()
    match (choose):
        case 1:
            a.choice_option ()

        case 2:
            s.add_sits()

        case 3:
            v.view_movies ()

        case 4:
            v.view_sitting()

        case 5:
            v.view_tickit()

        case 6:
            break

        case _:
            print ("Enter valid option")
            
