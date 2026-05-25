import plotly.express as px
import plotly.graph_objects as go
from collections import defaultdict
import pandas as pd
from utils import create_empty_console_list, get_index_of_console

def print_box_plot_for_critic_score(list_of_games):
    list_of_critic_scores = []

    for game in list_of_games:
        critic_score = game.critic_score
        if critic_score is not None and critic_score != 0.0:
            list_of_critic_scores.append(critic_score)

    text_critic_score = "Critic Score"
    data = {
        text_critic_score: list_of_critic_scores
    }

    figure = px.box(data, y=text_critic_score)
    figure.update_layout(title_text="Verteilung der Critic Scores in den Spielen")
    figure.show()

def print_critic_score_from_top_games_as_diagram(games):
    consoles = ["PC", "PS3", "PS4", "NS", "XOne", "X360"]
    top_number = 20

    top_titles = get_top_games_of_all_time(games, top_number)

    length_of_consoles = len(consoles)
    game_dictionary = {}

    for searched_title in top_titles:
        for game in games:
            if game.title != searched_title:
                continue
            if game.title not in game_dictionary.keys():
                empty_list = create_empty_console_list(length_of_consoles)
                game_dictionary.update({game.title: empty_list})
            if game.critic_score is not None and game.critic_score > 0.0:
                index = get_index_of_console(consoles, game.console)
                if index != -1:
                    game_dictionary[game.title][index] = game.critic_score

    data = []

    for value in game_dictionary.values():
        data.append(value)

    title = "Critic Score der besten " + str(top_number) + " Spiele aller Zeiten pro Konsole"

    figure = go.Figure(data=go.Heatmap(
        z=data,
        x=consoles,
        y=list(game_dictionary.keys())
    ))
    figure.update_layout(
        title=dict(
            text=title
        )
    )
    figure.show()

"""
    Es soll herausgefunden werden,
    ob in den Jahren der Critic Score hoeher geworden ist
"""
def print_linear_regression_for_release_year_and_critic_score(list_of_games):
    list_of_release_year = []
    list_of_critic_score = []

    for game in list_of_games:
        if (game.critic_score > 0):
            list_of_release_year.append(game.year)
            list_of_critic_score.append(game.critic_score)

    text_release_year = "Jahr der Veröffentlichung"
    text_critic_score = "Critic Score"

    data = {
        text_release_year: list_of_release_year,
        text_critic_score: list_of_critic_score
    }
    data_frame = pd.DataFrame(data)
    figure = px.scatter(data_frame, x=text_release_year, y=text_critic_score,
                        trendline="ols",
                        title="Verlauf des Critic Scores in den Jahren")
    figure.show()

def get_top_games_of_all_time(games, top_number):
    game_score_dictionary = defaultdict(float)
    for game in games:
        if game.critic_score is None or game.critic_score < 1.0:
            continue
        if game.title not in game_score_dictionary.keys():
            game_score_dictionary[game.title] = game.critic_score
        elif game_score_dictionary[game.title] < game.critic_score:
            game_score_dictionary[game.title] = game.critic_score
    top_titles = sorted(game_score_dictionary, key=game_score_dictionary.get, reverse=True)[:top_number]

    return top_titles