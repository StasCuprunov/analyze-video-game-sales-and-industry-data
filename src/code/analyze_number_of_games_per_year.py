import plotly.express as px
import pandas as pd
from utils import get_distinct_games, find_all_years_of_release_games, find_all_genres

def print_number_of_games_per_year_as_diagram(list_of_games):
    new_list_of_games = get_distinct_games(list_of_games)

    list_of_release_years = find_all_years_of_release_games(new_list_of_games)
    list_of_genres = find_all_genres(new_list_of_games)

    genre_collection_per_year = {}

    for year in list_of_release_years:
        genre_collection_per_year[year] = {}
        for genre in list_of_genres:
            genre_collection_per_year[year][genre] = 0

    for game in new_list_of_games:
        genre_collection_per_year[game.year][game.genre] += 1

    list_of_year = []
    list_of_genre = []
    list_of_number_of_games = []

    for key_year, value_genre_and_number_of_games in genre_collection_per_year.items():
        for key_genre, number_of_games in value_genre_and_number_of_games.items():
            list_of_year.append(key_year)
            list_of_genre.append(key_genre)
            list_of_number_of_games.append(number_of_games)

    text_year = "Jahr"
    text_genre = "Genre"
    text_number_of_games = "Anzahl der Spiele"
    data = {
        text_year: list_of_year,
        text_genre: list_of_genre,
        text_number_of_games: list_of_number_of_games
    }

    data_frame = pd.DataFrame(data)

    figure = px.bar(data_frame, x=text_year, y=text_number_of_games, color=text_genre, text_auto=True)
    figure.show()
