import pandas as pd
import plotly.express as px

def games_per_publisher_developer_heatmap(games, top_n=20):
    # Spaltennamen als Variablen definieren
    COL_PUBLISHER = "Publisher"
    COL_DEVELOPER = "Developer"
    COL_COUNT = "Anzahl Spiele"

    data = []

    # Daten sammeln
    for game in games:
        if game.publisher and game.developer:
            data.append({
                COL_PUBLISHER: game.publisher,
                COL_DEVELOPER: game.developer
            })

    df = pd.DataFrame(data)

    # Anzahl der Spiele pro Publisher-Developer Kombination zählen
    df_grouped = (
        df.groupby([COL_PUBLISHER, COL_DEVELOPER])# guppiert nach Publisher und Developer
        .size()# zählt die Einträge pro Gruppe
        .reset_index(name=COL_COUNT)# macht es wieder zum dataframe
    )

    # Top Publisher nach Gesamtanzahl bestimmen
    top_publishers = (
        df_grouped.groupby(COL_PUBLISHER)[COL_COUNT]# gruppiert nach publisher
        .sum()# gesamtzahl der spiele
        .nlargest(top_n)# wählt die top_n
        .index# gibt die namen der publisher zurück
    )

    # nur diese Publisher im dataframe behalten
    df_filtered = df_grouped[
        df_grouped[COL_PUBLISHER].isin(top_publishers)
    ]

    # Top Developer auswählen (für bessere Übersicht)
    top_developers = (
        df_filtered.groupby(COL_DEVELOPER)[COL_COUNT]# gruppiert nach developer
        .sum() #gesamtzahl der spiele
        .nlargest(20)# top 20 developer gewählt zur übersicht
        .index# nur namen zurückgeben
    )

    # nur diese Developer ins dataframe aufnehmen
    df_filtered = df_filtered[
        df_filtered[COL_DEVELOPER].isin(top_developers)
    ]

    # Daten in Matrixform bringen
    heatmap_data = df_filtered.pivot(
        index=COL_PUBLISHER,# publisher in zeilen
        columns=COL_DEVELOPER,# developer in säulen
        values=COL_COUNT# anzahl der spiele als matrixwerte
    ).fillna(0)

    # Heatmap erstellen
    fig = px.imshow(
        heatmap_data,# matrix als basisform
        labels=dict(
            x=COL_DEVELOPER,#x-achse
            y=COL_PUBLISHER,#y-achse
            color=COL_COUNT# farbenskala abhängig von spielanzahl
        ),
        title=f"Top {top_n} Publisher vs Developer ({COL_COUNT})",
        text_auto=True# soll zahlen in den feldern anzeigen
    )

    # Anmerkungen hinzufügen
    fig.add_annotation(
        text="Rechts äußere Säule: Developer unbekannt (Unknown)",
        xref="paper",
        yref="paper",
        x=1.12,
        y=1.05,
        showarrow=False
    )

    fig.add_annotation(
        text="Unterste Reihe: Publisher unbekannt (Unknown)",
        xref="paper",
        yref="paper",
        x=-0.08,
        y=-0.1,
        showarrow=False
    )
    
    fig.show()
    # games_per_publisher_developer_heatmap(games)