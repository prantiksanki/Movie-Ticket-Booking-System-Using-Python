def Movie_list() :
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
