import pandas as pd
import plotly.express as px

def games_per_publisher_developer_heatmap(games, top_n=20):
    data = []

    for game in games:
        if game.publisher and game.developer:
            data.append({
                "Publisher": game.publisher,
                "Developer": game.developer
            })

    df = pd.DataFrame(data)

    df_grouped = df.groupby(["Publisher", "Developer"]).size().reset_index(name="Anzahl Spiele")

    # Top Publisher auswählen
    top_publishers = (
        df_grouped.groupby("Publisher")["Anzahl Spiele"]
        .sum()
        .nlargest(top_n)
        .index
    )

    df_filtered = df_grouped[df_grouped["Publisher"].isin(top_publishers)]

    heatmap_data = df_filtered.pivot(
        index="Publisher",
        columns="Developer",
        values="Anzahl Spiele"
    ).fillna(0)

    fig = px.imshow(
        heatmap_data,
        labels=dict(x="Developer", y="Publisher", color="Anzahl Spiele"),
        title=f"Top {top_n} Publisher vs Developer (Anzahl Spiele)"
    )

    fig.show()

    # games_per_publisher_developer_heatmap(games)