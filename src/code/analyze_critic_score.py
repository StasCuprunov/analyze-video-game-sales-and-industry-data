import plotly.express as px
import pandas as pd

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