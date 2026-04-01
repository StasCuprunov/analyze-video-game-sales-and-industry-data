import plotly.express as px

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