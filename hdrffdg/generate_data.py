import json
import os

# Prüfen, ob config.json existiert
if not os.path.exists("config.json"):
    print("❌ Fehler: config.json nicht gefunden!")
    print("Lege zuerst config.json im selben Ordner an.")
    exit(1)

# Konfiguration laden
with open("config.json", "r", encoding="utf-8") as f:
    cfg = json.load(f)

# Werte extrahieren
start = cfg["start_year"]
end = cfg["end_year"]
base = cfg["base_revenue"]
inc = cfg["annual_increase"]

# Validierung
if start > end:
    raise ValueError("Startjahr darf nicht größer als Endjahr sein!")

# Daten berechnen
years = list(range(start, end + 1))
revenue = [base + i * inc for i in range(len(years))]
total = sum(revenue)

# Ausgabedaten vorbereiten (einfache Struktur!)
output = {
    "title": cfg["title"],
    "subtitle": cfg["subtitle"],
    "currency": cfg["currency"],
    "years": years,
    "revenue": revenue,
    "total_revenue": total,
    "average_revenue": total / len(revenue),
    "final_revenue": revenue[-1],
    "year_range": f"{years[0]}–{years[-1]}"
}

# In data.json schreiben
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(output, f, indent=2, ensure_ascii=False)

print("✅ Erfolg! data.json wurde erstellt.")
print(f"   Jahre: {start} – {end}")
print(f"   Bevölkerung: {base} → {revenue[-1]} {cfg['currency']}")