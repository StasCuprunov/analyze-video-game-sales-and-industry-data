import pandas as pd 
import plotly.express as px

def games_per_year_diagram(games):
    # Spaltennamen definieren
    COL_YEAR = "Jahr"
    COL_COUNT = "Anzahl Spiele"

    data = []

    # Jahr aus den Game-Objekten sammeln
    for game in games:
        if game.year:  # nur gültige Jahre berücksichtigen
            data.append({COL_YEAR: game.year})

    # DataFrame erstellen
    df = pd.DataFrame(data)

    # Anzahl Spiele pro Jahr zählen
    df_grouped = (
        df.groupby(COL_YEAR)
        .size()
        .reset_index(name=COL_COUNT)
    )

    # nach Jahr sortieren
    df_grouped = df_grouped.sort_values(by=COL_YEAR)

    # Säulendiagramm erstellen
    fig = px.bar(
        df_grouped,
        x=COL_YEAR,
        y=COL_COUNT,
        title="Anzahl der veröffentlichten Spiele pro Jahr",
        text_auto=True,
        width=1200,
        height=600
    )

    # Layout verbessern
    fig.update_layout(
        xaxis_title="Jahr",
        yaxis_title="Anzahl Spiele"
    )

    fig.show()