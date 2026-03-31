from collections import Counter
from typing import List
import pandas as pd
import plotly.express as px
from get_data_csv import Game

def print_developer_total_as_diagram(games: List[Game], top_n: int) -> None:
    """
    Erstellt ein Kuchendiagramm der Developer-Anteile.
    Zeigt die Top-n Developer einzeln an.
    'Unknown' bleibt separat.
    Alle anderen Developer werden zu 'Andere' zusammengefasst.
    Parameter:
    games: Liste von Game‑Objekten, aus denen die Publisher ausgelesen werden.
    top_n: Anzahl der Developer, die einzeln angezeigt werden. 
           Alle weiteren werden zu 'Andere' zusammengefasst.
    """

    developer_names: List[str] = []

    for game in games:
        developer_name = game.developer.strip() if game.developer else "Unknown"
        if not developer_name:
            developer_name = "Unknown"
        developer_names.append(developer_name)

    developer_counts = Counter(developer_names)

    # Unknown separat behandeln
    unknown_count = developer_counts.get("Unknown", 0)
    if "Unknown" in developer_counts:
        del developer_counts["Unknown"]

    # Top-n Developer bestimmen
    top_n_developers = dict(developer_counts.most_common(top_n))

    # Alle anderen Developer zusammenfassen
    other_count = sum(
        count for developer, count in developer_counts.items()
        if developer not in top_n_developers
    )

    # Labels + Werte für das Diagramm
    developer_labels = []
    developer_values = []

    if unknown_count > 0:
        developer_labels.append("Unknown")
        developer_values.append(unknown_count)

    for developer, count in top_n_developers.items():
        developer_labels.append(developer)
        developer_values.append(count)

    if other_count > 0:
        developer_labels.append("Andere")
        developer_values.append(other_count)

    developer_dataframe = pd.DataFrame({
        "Developer": developer_labels,
        "Anzahl Spiele": developer_values
    })

    developer_figure = px.pie(
        developer_dataframe,
        values="Anzahl Spiele",
        names="Developer",
        width=1000,
        height=700
    )

    developer_figure.update_layout(
        title={
            "text": f"Anteil der Developer ({top_n} + Unknown + Andere)",
            "x": 0.55,          # zentriert
            "xanchor": "center",
            "y": 0.98,         # höher setzen
            "font": dict(size=20)   # <-- Schriftgröße des Titels
        },
        legend=dict(
            orientation="v",
            yanchor="top",
            y=1,
            xanchor="left",
            x=1.05,
            font=dict(size=12),
            itemsizing="constant"
        ),
        margin=dict(r=200)
    )

    developer_figure.show()