##
# movie_collecter.py
# make a movie collection program
# 
# Author: Phoebe Williamson
# 9/5/22 - 21/5/22

# Done:
# Funtion for menu
# Funtion to print out all the movies time in hours and minutes

# To do list:
# Function to add movie (title, director, and length)
# Funtion to edit movie length
# Function to print out a specific movie time in hours and minutes



# Funtion for menu
def getting_movie():
    """
    menu function to allow the user to chose the function to access
    """
    choices = [1, 2, 3, 4, 0]
    # keeps while loop running until a valid 'choice' has been entered
    menu_option = True
    while menu_option:
        try:
            # asks user for an input to go to the function
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
                # prints this out if a 'choice' in 'choices' has not been entered
                print("Please enter a valid option, e.g. 0")
        except ValueError:
            # checks that it is a number
            print("Please enter a valid option, e.g. 0")
    return choice

# function to add movie (title, director, and length)
def add_movie(dictionary):
    """
    asks user for inputs for moive title, director name and time in minutes
    changes time entered in minutes to hours and minutes then
    adds them to the dictionary
    """
    # sets the highest and lowest time aceptable for the movie length
    HIGHEST_TIME = 299
    LOWEST_TIME = 1
    # sets the lowest time acccepted for director and movie name
    MIN_NAME = 3
    MIN_TITLE = 1

    # keeps loop running until a valid moive title has been entered
    get_movie = True
    while get_movie:
        # asks user for a movie title
        movie = input("Please enter the movie title: ")
        if len(movie) > MIN_TITLE:
            # ends loop when a vaild movie name is entered
            get_movie = False
        else:
            # keeps looping until a valid title is entered
            print("Please ennter a valid movie name.\n")

    # keeps loop running util a valid director name has been entered
    get_director = True
    while get_director:
        # asks user for the director name
        director = input("Please enter the directors name: ")
        if len(director) > MIN_NAME:
            # ends loop when a valid director name has been entered
            get_director = False
        else:
            # keeps looping until a valid direcotr name has bean entered
            print("Please enter a valid director name.\n")
    # keeps looping until valid time has been entered
    get_time = True
    while get_time:
        HOUR = 1
        TWO_HOUR = 2
        THREE_HOUR = 3
        FOUR_HOUR = 4
        MIN_IN_HOUR = 60
        MIN_IN_TWO_HOUR = 120
        MIN_IN_THREE_HOUR = 180
        MIN_IN_FOUR_HOUR = 240
        time_in_hours = 0
        try:
            # asks user for a time in minutes
            time = int(input("Please enter the time of the movie in minutes: "))
            if  time < LOWEST_TIME or time > HIGHEST_TIME:
                print("Please enter the time of a movie between 1 and"
                      " 299 minutes")
            elif time < 60:
                time = time
                time_in_hours = time_in_hours
                get_time = False
            elif time >= 60:
                time = time - MIN_IN_HOUR - MIN_IN_HOUR
                time_in_hours = time_in_hours + HOUR + HOUR
                get_time = False
            elif time >= 120:
                time = time - MIN_IN_HOUR - MIN_IN_HOUR
                time_in_hours = time_in_hours + HOUR + HOUR
                get_time = False
            elif time >= 180:
                time = time - MIN_IN_HOUR - MIN_IN_HOUR - MIN_IN_HOUR
                time_in_hours = time_in_hours + HOUR + HOUR + HOUR
                get_time = False
            elif time >= 240:
                time = time - MIN_IN_4HOUR
                time_in_hours = FOUR_HOUR

            else:
                get_time = False
                 
            # converts the dictionary to a list so it can accces last value
            # and creates a new movie key
            key = list(dictionary.keys()) [-1] + 1
            dictionary.update({key: {"Title": movie.title(),
                                     "Director": director.title(),
                                     "Time in hours": time_in_hours,
                                     "Time in minutes": time}})
        except ValueError:
            print("Please enter a valid movie time in minutes, e.g 120")
            

# function for editing a movies length
def edit_movie_time(dictionary):
    """
    asks user for a new time for selected movie
    """
    for key in dictionary.keys():
                    movie_information = dictionary[key]
                    movie = movie_information["Title"]
                    director = movie_information["Director"]
                    new_time = movie_information["Time in minutes"]
                    time_in_hours = movie_information["Time in hours"]
    get_key = True
    while get_key:
        try:
            movie_time_change = int(input("\nPlease select the key number "
                                          "for the movie you would like to "
                                          "change the time for: "))
            if movie_time_change not in dictionary.keys():
                print("Please enter a valid movie key, e.g. 2")
            elif movie_time_change <= len(dictionary):
                get_key = False
            else:
                print("Please enter a valid movie key, e.g. 2")
        except ValueError:
            print("Please enter a whole number, e.g 2")

    MIN_TIME = 0
    MAX_TIME = 299
    HOUR = 1
    MIN_IN_HOUR = 60
    time_in_hours = 0

    get_time = True
    while get_time:
        try:
            new_time = int(input("Please give the movie a new time less than"
                                  " 299 minutes: "))
            if new_time < MIN_TIME or new_time > MAX_TIME:
                # makes sure movie time is within the correct length
                print("Please give the movie a time between 0 and 299 minutes")
            elif new_time != time_in_hours and new_time > MIN_TIME and new_time <= MAX_TIME:
                # makes sure the time entered is new and fits the required time
                for key in dictionary.keys():
                    movie_information = dictionary[key]
                    movie = movie_information["Title"]
                    director = movie_information["Director"]
                    new_time = movie_information["Time in minutes"]
                    time_in_hours = movie_information["Time in hours"]

                    mins_to_hours = True
                    time_in_hours = 0
                    MIN_IN_HOUR = 60
                    HOUR = 1
                    while mins_to_hours:
                        if new_time < 60:
                            new_time = new_time
                            hours = time_in_hours
                            mins_to_hours = False
                        elif new_time >= 60 and new_time < 120:
                            new_time = new_time - MIN_IN_HOUR - MIN_IN_HOUR
                            hours = time_in_hours + HOUR + HOUR
                            mins_to_hours = False
                        elif new_time >= 120 and new_time < 180:
                            new_time = new_time - MIN_IN_HOUR - MIN_IN_HOUR
                            hours = time_in_hours + HOUR + HOUR
                            mins_to_hours = False
                        elif new_time >= 180 and new_time < 240:
                            new_time = new_time - MIN_IN_HOUR - MIN_IN_HOUR - MIN_IN_HOUR
                            hours = time_in_hours + HOUR + HOUR + HOUR
                            mins_to_hours = False
                        elif new_time > 240:
                            new_time = new_time - MIN_IN_HOUR - MIN_IN_HOUR - MIN_IN_HOUR - MIN_IN_HOUR
                            hours = HOUR + HOUR + HOUR + HOUR
                        else:
                            mins_to_hours = False
                    dictionary.update({key: {"Title": movie,
                                             "Director": director,
                                             "Time in hours": hours,
                                             "Time in minutes": new_time}})
                get_time = False
            else:
                print("Please enter a number between 0 and 299")
        except ValueError:
            print("Please  enter a whole number")


# function for printing movie time in hours and minutes
def movie_length(dictionary):
    """
    will print out a specfic movie chosen and its length in hours and minutes
    """
    for key in dictionary.keys():
        movie_info = dictionary[key]
        movie = movie_info["Title"]
        director = movie_info["Director"]
        hours = movie_info["Time in hours"]
        minutes = movie_info["Time in minutes"]

        print("{}\tTitle: {}\n\tDirector: {}".format(key, movie, director,))

    get_movie_key = True
    while get_movie_key:
        movie_length_print = int(input("\nPlease select the key number "
                                       "for the movie you would like to "
                                       "print the time for: "))
        if movie_length_print not in dictionary.keys():
            print("Please enter a valid movie key, e.g. 2")
    


# function for printing out movie list
def print_movies(dictionary):
    """
    prints movies
    """
    for key in dictionary.keys():
        movie_info = dictionary[key]
        movie = movie_info["Title"]
        director = movie_info["Director"]
        hours = movie_info["Time in hours"]
        minutes = movie_info["Time in minutes"]

        print("{}\tTitle: {}\tDirector: {}\n\tTime in hours: {}"
              "\tTime in minutes: {}".format(key, movie, director, hours, minutes))


# main frame
if __name__ == "__main__":
    # the list of movies
    movies = {1: {"Title": "Minions: the rise of Gru",
                  "Director": "Kyle Balda",
                  "Time in hours": 1, "Time in minutes": 31},
              2: {"Title": "Uncharted",
                  "Director": "Ruben Fleischer",
                  "Time in hours": 1, "Time in minutes": 56},
              3: {"Title": "The Adam project",
                  "Director": "Shawn Levy",
                  "Time in hours": 1, "Time in minutes": 46},
              4: {"Title": "The power of the dog",
                  "Director": "Jane Campion",
                  "Time in hours": 2, "Time in minutes": 6},
              5: {"Title": "Rampage",
                  "Director": "Brad Peyton",
                  "Time in hours": 1, "Time in minutes": 47}}

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
            # goes to print movie length function
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
