import plotly.graph_objects as go
from utils import get_all_consoles, create_empty_console_list, get_index_of_console

def print_critic_score_as_diagram(list_of_games):
    list_of_consoles = get_all_consoles(list_of_games)
    length_of_list_of_consoles = len(list_of_consoles)
    game_dictionary = {}
    for game in list_of_games:
        if game.title not in game_dictionary.keys():
            empty_list = create_empty_console_list(length_of_list_of_consoles)
            game_dictionary.update({game.title: empty_list})
        index = get_index_of_console(list_of_consoles, game.console)
        if game.critic_score != None:
            game_dictionary[game.title].insert(index, game.critic_score)

    data = []

    for value in game_dictionary.values():
        data.append(value)

    figure = go.Figure(data=go.Heatmap(
                       z=data,
                       x=list_of_consoles,
                       y=list(game_dictionary.keys())
                        ))
    figure.update_layout(
        title=dict(
            text="Critic-Score pro Spiel je Konsole"
        )
    )
    figure.show()
