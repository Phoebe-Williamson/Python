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
# Function for adding movie, director and time in minutes
# Funtion to edit a movie length
# Function to print out the movie time in hours and minutes
# Funtion to print out all the movies


# Funtion for menu 
def getting_movie():
    """
    menu function to allow the user to chose the function to acess
    """
    choices = ['A', 'E', 'L', 'P', 'Q']
    menu_option = True
    while menu_option:
        try:
            choice = input("*** Menu ***"
                           "\n'A': Add movie"
                           "\n'E': Edit movie length"
                           "\n'L': Print out movie length"
                           "\n'P': Print out list of movies"
                           "\n'Q': Quit"
                           "\nEnter option here: ")
            if choice in choice:
                print("You have chosen {}.\n".format(choice))
                menu_option = False
            else:
                print("Please enter a valid option, e.g. Q")
        except ValueError:
            print("Please enter a valid option, e.g. Q")
    return choice


# function for adding movies
def add_movie(dictionary):
    pass
    """

    """


# function for editing a movies length
def edit_movie(dictionary):
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
    pass
    """

    """





# main frame
if __name__ == "__main__":
    
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
                  "Time": 126, " minutes"
                  "Time in hours": 2, "Time in minutes": 6},
              5: {"Title": "Rampage",
                  "Director": "Kyle Balda",
                  "Time in hours": 1, "Time in minutes": 31}}

# Will loop so menu will keep runing through until killed
    code_running = True
    while code_running:
        menu_option = getting_movie()
        if menu_option == 'A':
            add_movie(movies)
            print_movies(movies)
        elif menu_option == 'E':
            print_movies(movies)
            edit_movie(movies)
            print_movies(movies)
        elif menu_option == 'L':
            movie_length(movies)
        elif menu_option == 'P':
            print_movies(movies)
        elif menu_option == 'Q':
            code_running = False
        else:
            print("That is not a valid option.")
