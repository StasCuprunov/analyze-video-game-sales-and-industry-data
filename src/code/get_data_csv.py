import csv                              # zum Einlesen der CSV-Datei
from dataclasses import dataclass       # zum Definieren der RawGame-Dataclass
from typing import Optional, List       # für die optionale last_update-Variable und List-Typen

# Dataclass zur Repräsentation eines Spiels mit den entsprechenden Attributen
@dataclass
class RawGame:
    img: str
    title: str
    console: str
    genre: str
    publisher: str
    developer: str
    critic_score: float
    total_sales: float
    na_sales: float
    jp_sales: float
    pal_sales: float
    other_sales: float
    release_date: str
    last_update: Optional[str] = None

# Funktion zum Laden der Spieldaten aus einer CSV-Datei und Rückgabe einer Liste von RawGame-Objekten
def load_raw_games(csv_path: str) -> List[RawGame]:  # csv_path: Pfad zur CSV-Datei, die die Spieldaten enthält
    games = []                                       # leere Liste, die später mit RawGame-Objekten gefüllt wird
    with open(csv_path, encoding="utf-8") as f:      # Öffnen der CSV-Datei im Lesemodus mit UTF-8-Kodierung
        reader = csv.DictReader(f)                   # Erstellen eines DictReader-Objekts, das die CSV-Daten als Wörterbuch liest (Spaltennamen als Schlüssel)
        for row in reader:                           # Iterieren über jede Zeile in der CSV-Datei, wobei jede Zeile als Wörterbuch (row) dargestellt wird

            # Konvertieren der relevanten Felder von Strings zu den entsprechenden Datentypen (z.B. float für Verkaufszahlen)
            # Hilfsfunktion: leere Strings → 0.0
            def to_float(value: str) -> float:      # Funktion, die einen String-Wert in einen Float konvertiert, wobei leere Strings als 0.0 behandelt werden
                return float(value) if value.strip() != "" else 0.0  # Überprüfen, ob der String nicht leer ist (nach Entfernen von Leerzeichen), und entsprechend konvertieren oder 0.0 zurückgeben
            # Konvertieren der relevanten Felder in die entsprechenden Datentypen
            row["critic_score"] = to_float(row["critic_score"])
            row["total_sales"] = to_float(row["total_sales"])
            row["na_sales"] = to_float(row["na_sales"])
            row["jp_sales"] = to_float(row["jp_sales"])
            row["pal_sales"] = to_float(row["pal_sales"])
            row["other_sales"] = to_float(row["other_sales"])

            # Hilfsfunktion: leere Strings → None
            # last_update: leere Strings → None
            if row["last_update"].strip() == "":  # Überprüfen, ob das last_update-Feld leer ist (nach Entfernen von Leerzeichen)
                row["last_update"] = None         # Wenn das Feld leer ist, wird es auf None gesetzt, andernfalls bleibt der ursprüngliche Wert erhalten
            # Erstellen eines RawGame-Objekts mit den konvertierten Werten und Hinzufügen zur Liste der Spiele
            games.append(RawGame(**row))

    return games    # Rückgabe der Liste von RawGame-Objekten, die aus der CSV-Datei geladen wurden
