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

def find_all_years_of_release_games(list_of_games):
    list_of_years = []

    for game in list_of_games:
        if game.year not in list_of_years:
            list_of_years.append(game.year)
    return list_of_years

def find_all_genres(list_of_games):
    list_of_genres = []
    for game in list_of_games:
        if game.genre not in list_of_genres:
            list_of_genres.append(game.genre)
    return list_of_genres
def create_empty_console_list(number_of_consoles):
    console_list = []
    for index in range(number_of_consoles):
        console_list.append(None)
    return console_list

def get_index_of_console(list_of_consoles, searched_console):
    for index in range(len(list_of_consoles)):
        if list_of_consoles[index] == searched_console:
            return index
    return -1