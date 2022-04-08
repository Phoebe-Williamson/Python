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
    for id, game in dictionary.items():
        print("id: {} Game: {}\tRating: {}".format(id,
                                                   game["name"],
                                                   game["Rating"]))


if __name__ == "__main__":
    videogames = {1:{"name":"Minecraft", "Rating":5},
                  2:{"name":"Call of Duty", "Rating":1},
                  3:{"name":"Angry Birds", "Rating":4},
                  4:{"name":"Splatoon 2", "Rating":5},
                  5:{"name":"Animal Crossing", "Rating":4}}
    print_dictionary(videogames)
