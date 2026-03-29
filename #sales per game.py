#sales per game
import pandas as pd
import plotly.express as px
from collections import defaultdict

def sales_diagram(games, top_n=50): # erstellt das Diagramm für die top50 spiele
    sales = defaultdict(lambda: [0, 0, 0, 0])  # [NA, JP, PAL, Other]
    
    for game in games:# geht alle spiele durch und summiert die verkaufszahlen auf
        sales[game.title][0] += game.na_sales
        sales[game.title][1] += game.jp_sales
        sales[game.title][2] += game.pal_sales
        sales[game.title][3] += game.other_sales

    # berechnet den gesamtverkauf eines spiels
    total_sales = {t: sum(v) for t, v in sales.items()}
    top_titles = sorted(total_sales, key=total_sales.get, reverse=True)[:top_n]# wählt die top spiele aus

    df = pd.DataFrame({# erstellt das dataframe fürs plotly
        "Spiel": top_titles,
        "NA": [sales[t][0] for t in top_titles],
        "JP": [sales[t][1] for t in top_titles],
        "PAL": [sales[t][2] for t in top_titles],
        "Other": [sales[t][3] for t in top_titles],
    })

    fig = px.bar(# generiert das balkendiagramm
        df,
        y="Spiel",# y-achse sind die spiele
        x=["NA", "JP", "PAL", "Other"],#x-achse die regionen
        orientation="h",# horizontale ausrichtung der balken
        title="Verkäufe pro Spiel (gestapelt nach Regionen)",
        text_auto=True   # sollte zahlen direkt im balken anzeigen
    )

    fig.update_layout(barmode="stack")# balken sollten gestapelt werden also die regionen damit man einen balken pro spiel hat

    fig.show()#visualisier das diagramm