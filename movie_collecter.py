##
# movie_collecter.py
# make a movie collection program
# 
#
#
# Author: Phoebe Williamson
# 9/5/22 - 21/5/22

# Done:


# To do list:
# Function for adding movie, director and time in minutes
# Funtion to edit a movie length
# Function to print out the movie time in hours and minutes
# Funtion to print out all the movies


# Funtion for menu 
def menu_option():
    """
    menu function to allow the user to chose the function to acess
    """
    choices = ['A', 'E', 'L', 'P', 'Q']
    menu_option = True
    while menu_option:
        try:
            choice = input("Menu\n"
                           "\n'A': Add movie"
                           "\n'E': Edit movie length"
                           "\n'L': Print out movie length"
                           "\n'P': Print out list of movies"
                           "\n'Q': Quit")
            if choice in choice:
                print("You have chosen {}.\n".format(choice))
                menu_option = False
            else:
                print("Please enter a valid option, e.g. Q")
        except ValueError:
            print("Please enter a valid option, e.g. Q")
    return choice


# main frame
if __name__ == "__main__":
    
