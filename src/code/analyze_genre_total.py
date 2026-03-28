from collections import defaultdict
import pandas as pd
import plotly.express as px

"""
Einige Spiele haben mehrere Kategorien. 
Daher wird ein beliebige Kategorie pro Spiel ausgewaehlt.
Wenn es moeglich ist, wird kein "Misc"-Kategorie ausgewaehlt.
"""
def get_distinct_games(list_of_games):
    new_list_of_games = []
    for game in list_of_games:
        has_found_game = False
        for index in range(len(new_list_of_games)):
            searched_game = new_list_of_games[index]
            if (searched_game.title == game.title):
                has_found_game = True
                if (searched_game.genre == "Misc"):
                    new_list_of_games[index] = game
                break
        if not has_found_game:
            new_list_of_games.append(game)
    return new_list_of_games

def print_genre_total_as_diagram(list_of_games):
    genre_dictionary = defaultdict(int)
    new_list_of_games = get_distinct_games(list_of_games)
    for game in new_list_of_games:
        genre_dictionary[game.genre] += 1

    genre_list = []
    number_of_games_list = []

    for key, value in genre_dictionary.items():
        genre_list.append(key)
        number_of_games_list.append(value)

    text_genre = "Genre"
    text_number_of_games = "Anzahl an Spielen"

    data = {
        text_genre: genre_list,
        text_number_of_games: number_of_games_list
    }

    data_frame = pd.DataFrame(data)

    figure = px.pie(data_frame, values=text_number_of_games, names=text_genre)
    figure.show()
