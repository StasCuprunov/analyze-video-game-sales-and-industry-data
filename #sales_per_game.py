#sales per game
import pandas as pd
import plotly.express as px
from collections import defaultdict

def sales_diagram(games, top_n=20): # erstellt das Diagramm für die top50 spiele
    #Indezes als Variablen
    INDEX_NA = 0
    INDEX_JP = 1
    INDEX_PAL = 2
    INDEX_OTHER = 3

    #Spaltennamen als Variablen
    COL_GAME = "Spiel"
    COL_NA = "NA"
    COL_JP = "JP"
    COL_PAL = "PAL"
    COL_OTHER = "Other"
    
    sales = defaultdict(lambda: [0, 0, 0, 0])  # [NA, JP, PAL, Other]
    
    for game in games:# geht alle spiele durch und summiert die verkaufszahlen auf
        sales[game.title][INDEX_NA] += game.na_sales
        sales[game.title][INDEX_JP] += game.jp_sales
        sales[game.title][INDEX_PAL] += game.pal_sales
        sales[game.title][INDEX_OTHER] += game.other_sales

    # berechnet den gesamtverkauf eines spiels
    total_sales = {title: sum(region.sales) for title, region.sales in sales.items()}
    top_titles = sorted(total_sales, key=total_sales.get, reverse=True)[:top_n]# wählt die top spiele aus

    df = pd.DataFrame({# erstellt das dataframe fürs plotly
        "Spiel": top_titles,
        "NA": [sales[t][INDEX_NA] for t in top_titles],
        "JP": [sales[t][INDEX_JP] for t in top_titles],
        "PAL": [sales[t][INDEX_PAL] for t in top_titles],
        "Other": [sales[t][INDEX_OTHER] for t in top_titles],
    })

    fig = px.bar(# generiert das balkendiagramm
        df,
        y=COL_GAME,# y-achse sind die spiele
        x=[COL_NA, COL_JP, COL_PAL, COL_OTHER]#x-achse die regionen
        orientation="h",# horizontale ausrichtung der balken
        title=f"Top {top_n} Spiele nach Verkaufszahlen (in Mio.)"
        text_auto=True   # sollte zahlen direkt im balken anzeigen
    )

    fig.update_layout(barmode="stack")# balken sollten gestapelt werden also die regionen damit man einen balken pro spiel hat

    fig.show()#visualisier das diagramm

# command zum csv reinladen games = load_raw_games("dateipfad der csv")
# command zum diagramm generieren sales_diagram(games, top_n=20)
