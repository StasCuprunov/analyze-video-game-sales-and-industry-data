from collections import Counter
from typing import List
import pandas as pd
import plotly.express as px
from get_data_csv import Game

UNKNOWN = "Unknown"  
COL_PUBLISHER = "Publisher"
COL_COUNT = "Anzahl Spiele"


def print_publisher_total_as_diagram(games: List[Game], top_n: int) -> None:
    """
    Erstellt ein Kuchendiagramm der Publisher-Anteile.
    Zeigt die Top-n Publisher einzeln an.
    'Unknown' bleibt separat.
    Alle anderen Publisher werden zu 'Andere' zusammengefasst.
    Parameter:
    games: Liste von Game‑Objekten, aus denen die Publisher ausgelesen werden.
    top_n: Anzahl der Publisher, die einzeln angezeigt werden. 
           Alle weiteren werden zu 'Andere' zusammengefasst.
    """

    publisher_names: List[str] = []
    for game in games:
        publisher_name = game.publisher.strip() if game.publisher else UNKNOWN
        if not publisher_name:
            publisher_name = UNKNOWN
        publisher_names.append(publisher_name)

    publisher_counts = Counter(publisher_names)

    unknown_count = publisher_counts.get(UNKNOWN, 0)
    if UNKNOWN in publisher_counts:
        del publisher_counts[UNKNOWN]

    top_n_publishers = dict(publisher_counts.most_common(top_n))

    other_count = sum(
        count for publisher, count in publisher_counts.items()
        if publisher not in top_n_publishers
    )

    publisher_labels = []
    publisher_values = []

    if unknown_count > 0:
        publisher_labels.append(UNKNOWN)
        publisher_values.append(unknown_count)

    for publisher, count in top_n_publishers.items():
        publisher_labels.append(publisher)
        publisher_values.append(count)

    if other_count > 0:
        publisher_labels.append("Andere")
        publisher_values.append(other_count)

    publisher_dataframe = pd.DataFrame({
        COL_PUBLISHER: publisher_labels,
        COL_COUNT: publisher_values
    })

    publisher_figure = px.pie(
        publisher_dataframe,
        values=COL_COUNT,
        names=COL_PUBLISHER,
        width=1000,     # größer
        height=700      # größer
    )

    # Legende rechts, vollständig sichtbar
    publisher_figure.update_layout(
        title={
            "text": f"Anteil der Publisher (Top {top_n} + Unknown + Andere)",
            "x": 0.55,          # zentriert
            "xanchor": "center",
            "y": 0.98,         # höher setzen
            "font": dict(size=20)   # <-- Schriftgröße des Titels
        },
        legend=dict(
            orientation="v",      # vertikal
            yanchor="top",
            y=1,
            xanchor="left",
            x=1.05,               # etwas Abstand rechts
            font=dict(size=12),
            itemsizing="constant"
        ),
        margin=dict(r=200)        # Platz für die Legende schaffen
    )

    publisher_figure.show()
