import csv
from dataclasses import dataclass
from typing import Optional, List

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
    release_date: Optional[str]
    year: Optional[int]
    last_update: Optional[str] = None

def load_raw_games(csv_path: str) -> List[Game]:  
    """Lädt Spieldaten aus einer CSV-Datei und gibt 
    eine Liste von Game-Objekten zurück."""
    games = [] 

    def convert_to_float(value: str) -> float:
        """Konvertiert einen String sicher in einen Float.
        Fängt zusätzlich ValueError und AttributeError ab."""
        try:
            return float(value.strip())
        except (ValueError, AttributeError):
            return 0.0
                                            
    with open(csv_path, encoding="utf-8") as file:
        reader = csv.DictReader(file) 
        
        for row in reader:
            # Falls CSV ein year-Feld enthält → entfernen, wir setzen es selbst
            row.pop("year", None)

            # Float-Felder sicher konvertieren
            float_fields = [
                "critic_score", "total_sales", "na_sales",
                "jp_sales", "pal_sales", "other_sales"
            ]

            for field in float_fields:
                row[field] = convert_to_float(row.get(field, ""))
            
            # release_date als String holen
            release_date = row.get("release_date", "").strip()

            # Jahr extrahieren (Format dd-mm-yyyy)
            if release_date:
                try:
                    year = int(release_date[-4:])
                except ValueError:
                    year = None
            else:
                year = None

            # last_update sicher behandeln
            if not row.get("last_update", "").strip():
                row["last_update"] = None
                
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
                last_update=row.get("last_update")
            ))

    return games