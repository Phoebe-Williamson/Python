##
# album_rater.py
# make an album rater program
# an alubm conatins a title, artist, genre, and rating
# you should allow the user to add, edit, delete, and rate, and print out
# all albums
# when you rate a program, your program should recomend another album
# album of the same genre
# you must make this program modular (funtions)
# you should make version control
# you SHOULD make this program robust
##
# 8/4/22 - ?
# Authors: Phoebe and Janelle


# funtcion for adding album - Janelle made this
def add_album(dictionary):
    """
    Asks for user inputs and adds them to dictionary
    """
    adding_albums = True
    while adding_albums:
        album = input("Please enter the title of the album\n"
                      "(or type 'q' to quit)\n"
                      ": ")
        if album == "q":
            adding_albums = False
        else:
            artist = input("Please enter the artist: ")
            genre = input("Please enter the genre: ")
            rating = input("Please give it a rating: ")
            key = len(dictionary) + 1

            dictionary.update({key: {"Title": album,
                                     "Artist": artist,
                                     "Genre": genre,
                                     "Rating": rating}})
            adding_albums = False


# function for deleting album
def deleting_album(dictionary):
    deleting_albums = True
    while deleting_albums:
        try:
            print(dictionary)
            delete = int(input("\nPlease select the album you would like to "
                               "delete, or press 'q' to quit: "))
            if delete == "q":
                deleting_albums = False
            else:
                print("You have chose to delete album {}.".format(delete))
                del dictionary[delete]
                key = len(dictionary) - 1
                dictionary.update()
                deleting_albums = False
        except ValueError:
            print("\nPlease enter a valid alum number, e.g 3\n")


# function for editing album
def editing_albums():
    pass


# function for rating album
def rating_album():
    pass


# function for printing album
def printing_album():
    print(albums)


# function for recomending album
def recomdening_album():
    pass


# menu #turn into function
def getting_album():
    """
    menu function to chose what function of the album rater to do
    """
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
                               "6: recomend albums\n"
                               "0: exit\n"))
            if choice in choices:
                print("you have chosen {}.\n".format(choice))
                getting_albums = False
        except ValueError:
            print("enter a valid number")
    return choice

# main routine
if __name__ == "__main__":  # Janelle made dictionary 
    albums = {1: {"Title": "Sour",
                  "Artist": "Olivia Rodrigo",
                  "Genre": "Pop", "Rating": 5},
              2: {"Title": "Promises",
                  "Artist": "Sam Shepherd",
                  "Genre": "Jazz", "Rating": 2},
              3: {"Title": "Sound Ancestors",
                  "Artist": "Madlib",
                  "Genre": "Hip-Hop", "Rating": 0},
              4: {"Title": "Valentine",
                  "Artist": "Snail Mail",
                  "Genre": "Alternative", "Rating": 4},
              5: {"Title": "Daddy's Home",
                  "Artist": "St. Vincent",
                  "Genre": "Pop", "Rating": 2}}
# loop so menu will keep runing through after chosing an option
    code_running = True
    while code_running:
        menu_option = getting_album()
        if menu_option == 1:
            add_album(albums)
            print(albums)
        elif menu_option == 2:
            deleting_album(albums)
            print(albums)
        elif menu_option == 3:
            deleting_album(albums)
            print(albums)
        elif menu_option == 4:
            deleting_album(albums)
            print(albums)
        elif menu_option == 5:
            printing_albums()
        elif menu_option == 6:
            deleting_album(albums)
            print(albums)
        elif menu_option == 0:
            code_runing = False
        else:
            print("That is not a valid option.")
