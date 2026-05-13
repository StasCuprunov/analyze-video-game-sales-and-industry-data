import plotly.graph_objects as go
from collections import defaultdict
from utils import create_empty_console_list, get_index_of_console

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
