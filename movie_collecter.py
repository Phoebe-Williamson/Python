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
    choices = [1, 2, 3, 4, 0]
    menu_option = True
    while menu_option:
        try:
            # asks user for an input
            choice = int(input("\n*** Menu ***"
                           "\n'1': Add movie"
                           "\n'2': Edit movie length"
                           "\n'3': Print out movie length"
                           "\n'4': Print out list of movies"
                           "\n'0': Quit"
                           "\nEnter option here: "))
            # makes sure it is one of the choices
            if choice in choices:
                print("You have chosen {}.\n".format(choice))
                menu_option = False
            else:
                print("Please enter a valid option, e.g. 0")
        except ValueError:
            print("Please enter a valid option, e.g. 0")
    return choice


# function for getting the movie key
def get_movie_key():
    """
    asks user for movie key then returns 
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
            print("Please enter the time of a movie less than 299 minutes")

        # converts the dictionary to a list so it can accces last value
        # creates a new movie key
        key = list(dictionary.keys()) [-1] + 1
        dictionary.update({key: {"Title": movie.title(),
                                 "Director": director.title(),
                                 "Time in minutes": time}})
    except ValueError:
        print("Please enter a valing movie time in minutes, e.g 120")
            

# function for editing a movies length
def edit_movie_time(dictionary):
    """
    asks user for a new time for selected movie
    """  
    movie_time_change = int(input("\nPlease select the key number "
                                  "for the movie you would like to "
                                  "change the rating for: "))
    movie_information = dictionary[movie_time_change]
    movie = movie_information["Title"]
    director = movie_information["Director"]
    time = movie_information["Time in minutes"]
    key = movie_time_change

    get_time = True
    while get_time:
        try:
            new_time = int(input("Please give the movie a new time less than"
                                 " 299 minutes: "))
            if new_time < 0 or new_time > 299:
                # makes sure movie time is within the correct length
                print("Please give the moive a time between 0 and 299 minutes")
            elif new_time == time:
                # makes sure that the time entered isnt what the time alreday is
                print("The movie already has this time, please change it")
            elif new_time != time and new_time >= 0 and new_time <= 299:
                # makes sure the time entered is new and fits the required time
                movie = movie_information["Title"]
                director = movie_information["Director"]
                time = movie_information["Time in minutes"]
                key = movie_time_change
                movie_information = dictionary[movie_time_change]


                dictionary.update({key: {"Title": movie,
                                         "Director": director,
                                         "Time in minutes": new_time}})
                get_time = False
            else:
                print("Please enter a number between 0 and 299")
        except ValueError:
            print("Please  enter a whole number")


# function for minutes to hours and minutes
def mins_to_hour():
    """
    converts the time from minutes to hours and minutes
    """
    print("This feature is currently under development")

# function for printing movie time in hours and minutes
def movie_length(dictionary):
    """
     will print out a specfic movie chosen and its length in hours and minutes
    """
    print("This feature is currently under development")

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
        if menu_option == 1:
            # goes to add movie function
            add_movie(movies)
            print_movies(movies)
        elif menu_option == 2:
            # goes to edit movie function
            print_movies(movies)
            edit_movie_time(movies)
            print_movies(movies)
        elif menu_option == 3:
            # goes to print moive length function
            movie_length(movies)
        elif menu_option == 4:
            # goes to print movies function
            print_movies(movies)
        elif menu_option == 0:
            # ends loop
            code_running = False
        else:
            # print error message if valid option not entered
            print("That is not a valid option.")
