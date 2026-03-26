import csv
from dataclasses import dataclass
from typing import Optional, List
from datetime import datetime

@dataclass
class Game:
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
    release_date: Optional[datetime]
    year: Optional[int]
    last_update: Optional[str] = None

def load_raw_games(csv_path: str) -> List[Game]:  
    """Lädt Spieldaten aus einer CSV-Datei und gibt 
    eine Liste von Game-Objekten zurück."""
    games = [] 

    def convert_to_float(value: str) -> float:
        """Konvertiert einen String in einen Float,
        wobei leere Strings als 0.0 behandelt werden."""
        return float(value) if value.strip() else 0.0
                                         
    def convert_to_date(value: str) -> Optional[datetime]:
        """Konvertiert ein Datum im Format YYYY-MM-DD in ein datetime-Objekt."""
        value = value.strip()
        if not value:
            return None
        try:
            return datetime.strptime(value, "%Y-%m-%d")
        except ValueError:
            return None
    
    with open(csv_path, encoding="utf-8") as file:
        reader = csv.DictReader(file) 
        
        for row in reader:
            # Float-Felder sicher konvertieren
            float_fields = [
                "critic_score", "total_sales", "na_sales",
                "jp_sales", "pal_sales", "other_sales"
            ]

            for field in float_fields:
                row[field] = convert_to_float(row.get(field, ""))
            
            # release_date konvertieren
            release_date = convert_to_date(row.get("release_date", ""))

            # Jahr extrahieren
            year = release_date.year if release_date else None

            # last_update sicher behandeln
            last_update_raw = row.get("last_update", "")
            if not last_update_raw or not last_update_raw.strip():
                last_update = None
            else:
                last_update = last_update_raw.strip()

            # Game-Objekt erzeugen
            games.append(Game(
                img=row.get("img", ""),
                title=row.get("title", ""),
                console=row.get("console", ""),
                genre=row.get("genre", ""),
                publisher=row.get("publisher", ""),
                developer=row.get("developer", ""),
                critic_score=row["critic_score"],
                total_sales=row["total_sales"],
                na_sales=row["na_sales"],
                jp_sales=row["jp_sales"],
                pal_sales=row["pal_sales"],
                other_sales=row["other_sales"],
                release_date=release_date,
                year=year,
                last_update=last_update
            ))

    return games