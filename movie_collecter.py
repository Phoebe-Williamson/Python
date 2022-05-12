##
# movie_collecter.py
# make a movie collection program
# 
#
#
# Author: Phoebe Williamson
# 9/5/22 - 21/5/22

# Done:
# Funtion for menu 

# To do list:
# Function to add movie (title, director, and length)
# Funtion to edit movie length
# Function to print out the movie time in hours and minutes
# Funtion to print out all the movies


# Funtion for menu 
def getting_movie():
    """
    menu function to allow the user to chose the function to acess
    and returns selected option
    """
    choices = ['A', 'a', 'E', 'e', 'L', 'l', 'P', 'p', 'Q', 'q']
    menu_option = True
    while menu_option:
        try:
            # asks user for an input
            choice = input("\n*** Menu ***"
                           "\n'A': Add movie"
                           "\n'E': Edit movie length"
                           "\n'L': Print out movie length"
                           "\n'P': Print out list of movies"
                           "\n'Q': Quit"
                           "\nEnter option here: ")
            # makes sure it is one of the choices
            if choice in choice:
                print("You have chosen {}.\n".format(choice))
                menu_option = False
            else:
                print("Please enter a valid option, e.g. Q")
        except ValueError:
            print("Please enter a valid option, e.g. Q")
    return choice


# function for getting the movie key
def get_movie_key():
    """
    asks useer for movie key then returns 
    """
    MIN_DICT_SIZE = 0
    getting_key = True
    #
    while getting_key:
        try:
            movie_key = int(input("\nPlease select the key number number for "
                                  "the movie you would like to select: "))
            # Checks if movie key exists
            if movie_key not in dictionary.keys():
                print("Please enter a album key, e.g 2")
            elif movie_key <= len(dictionary):
                return movie_key
            else:
                print("Please enter a album key, e.g 2")
        except ValueError:
            print("Please enter a whole number, e.g 2")

# function to add movie (title, director, and length)
def add_movie(dictionary):
    """
    asks user for inputs and adds them to the dictionary
    """
    movie = input("Please enter the movie title: ")
    director = input("Please enter the directors name: ")

    # sets the highest and lowest time aceptable for the movie length
    HIGHEST_TIME = 299
    LOWEST_TIME = 1

    try:
        time = int(input("Please enter the time of the movie in minutes: "))
        if  time < LOWEST_TIME or time > HIGHEST_TIME:
            print("Please enter the time of a moive less than 299 minutes")

        # converts the dictionary to a list so it can accces last value
        # creates a new movie key
        key = list(dictionary.keys()) [-1] + 1
        dictionary.update({key: {"Title": movie.title(),
                                 "Director": director.title(),
                                 "Time in minutes": time}})

    except ValueError:
        print("Please enter a valing movie time in minutes, e.g 120")
            



# function for editing a movies length
def edit_movie_time(movies):
    pass
    """
    asks user for a new time for selected movie
    """
    

# function for minutes to hours and minutes
def mins_to_hour():
    pass
    """

    """


# function for printing movie time in hours and minutes
def movie_length(dictionary):
    pass
    """

    """


# function for printing out movie list
def print_movies(dictionary):
    """
    prints movies
    """
    for key in dictionary.keys():
        movie_info = dictionary[key]
        movie = movie_info["Title"]
        director = movie_info["Director"]
        time = movie_info["Time in minutes"]

        print("{}\tTitle: {}\tDirector: {}\n\t Time in minutes:{}".format(key, movie, director, time))


# main frame
if __name__ == "__main__":
    # the list of movies
    movies = {1: {"Title": "Minions: the rise of Gru",
                  "Director": "Kyle Balda",
                  "Time in minutes": 91},
              2: {"Title": "Uncharted",
                  "Director": "Ruben Fleischer",
                  "Time in minutes": 116},
              3: {"Title": "The Adam project",
                  "Director": "Shawn Levy",
                  "Time in minutes": 106},
              4: {"Title": "The power of the dog",
                  "Director": "Jane Campion",
                  "Time in minutes": 126},
              5: {"Title": "Rampage",
                  "Director": "Brad Peyton",
                  "Time in minutes": 107}}

    # Will loop so menu will keep runing through until killed
    code_running = True
    while code_running:
        # gets menu option by running function
        menu_option = getting_movie()
        if menu_option == 'A' or menu_option == 'a':
            # goes to add movie function
            add_movie(movies)
            print_movies(movies)
        elif menu_option == 'E':
            # goes to edit movie function
            print_movies(movies)
            edit_movie(movies)
            print_movies(movies)
        elif menu_option == 'L':
            # goes to print moive length function
            movie_length(movies)
        elif menu_option == 'P' or menu_option == 'p':
            # goes to print movies function
            print_movies(movies)
        elif menu_option == 'Q':
            # ends loop
            code_running = False
        else:
            # print error message if valid option not entered
            print("That is not a valid option.")
