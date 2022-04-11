##
# album_rater.py
# make an album rater program
# an alubm conatins a title, artist, genre, and rating
# you should allow the user to add, edit, delete, and rate, and print out all albums
# when you rate a program, your program should recomend another album
# album of the same genre
# you must make this program modular (funtions)
# you should make version control
# you SHOULD make this program robust
##
# 8/4/22 - ?
# Authors: Phoebe and Janelle



# funtcion for adding album
def adding_album():
    pass
# function for deleting album
def deleting_album():
    pass
# function for editing album
def editing_albums():
    pass
# function for rating album
def rating_album():
    pass
# function for printing album
def printing_album():
    pass
# function for recomending album
def recomdening_album():
    pass
# create nested dictionary (dict inside dict)

# menu #turn into function
def getting_album():
    choices = [1, 2, 3, 4, 5, 6]
    getting_albums = True
    while getting_albums:
        try:
            choice = int(input("\nPlease chose your option\n"
                           "1: add album\n"
                           "2: delete album\n"
                           "3: edit album\n"
                           "4: rate album\n"
                           "5: print albums\n"
                           "6: recomend albums\n"))
            if choice in choices:
                print("you have chosen {}.\n".format(choice))
                getting_albums = False
        except ValueError:
            print("enter a valid number")
        return choice
                


# main routine
if __name__ == "__main__":
    albums = {1:{"Title":"Sour",
                 "Artist":"Olivia Rodrigo",
                 "Genre":"Pop", "Rating":5},
              2:{"Title":"Promises",
                 "Artist":"Sam Shepherd",
                 "Genre":"Jazz", "Rating":2},
              3:{"Title":"Sound Ancestors",
                 "Artist":"Madlib",
                 "Genre":"Hip-Hop", "Rating":0},
              4:{"Title":"Valentine",
                 "Artist":"Snail Mail",
                 "Genre":"Alternative", "Rating":4},
              5:{"Title":"Daddy's Home",
                 "Artist":"St. Vincent",
                 "Genre":"Pop", "Rating":2}}
    menu_option = getting_album()
