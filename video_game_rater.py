##
# video_game_rater.py
# rates video games
# 8/4/22
# Phoebe

def print_dictionary(dictionary):
    """
    accepts a dictionary, looops through it and prints
    out the game and its rating
    """
    for game, rating in dictionary.items():
        print("Game: {}\tRating: {}".format(game, rating))


if __name__ == "__main__":
    videogames = {"Minecraft":5, "Call of Duty":1, "Angry Birds":4,
                  "Splatoon 2":5, "Animal Crossing":4}
    print_dictionary(videogames)
