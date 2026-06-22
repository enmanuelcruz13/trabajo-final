import requests, json, re, sys
sys.path.insert(0, '.')
from pathlib import Path
from dotenv import load_dotenv
load_dotenv(Path('.env'))
import os

api_key = os.getenv('YOUTUBE_API_KEY', 'AIzaSyA5Xi_1qpDpY_c-GnsZKluXMezn2Nw2piw')

titulos = [
    "Mad Max Fury Road", "John Wick", "Mission Impossible Fallout", "The Equalizer",
    "Whiplash", "The Revenant", "Moonlight", "Parasite", "Oppenheimer",
    "The Grand Budapest Hotel", "Deadpool", "Everything Everywhere All at Once", "Barbie",
    "Interstellar", "The Martian", "Arrival", "Dune",
    "Inside Out", "Coco", "Spider-Man Into the Spider-Verse", "Soul", "Encanto",
    "The Babadook", "Get Out", "Hereditary", "A Quiet Place",
    "The Fault in Our Stars", "La La Land", "Call Me by Your Name", "Past Lives"
]

results = {}
for titulo in titulos:
    query = f"{titulo} trailer oficial español"
    url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={requests.utils.quote(query)}&type=video&maxResults=3&relevanceLanguage=es&videoEmbeddable=true&key={api_key}"
    r = requests.get(url)
    data = r.json()
    items = data.get('items', [])
    if items:
        vid = items[0]['id']['videoId']
        title = items[0]['snippet']['title']
        results[titulo] = (vid, title)
        print(f"OK  {titulo}: {vid} - {title[:60]}")
    else:
        results[titulo] = (None, 'NOT FOUND')
        print(f"FAIL {titulo}: NOT FOUND")

print("\n\nVIDEOS ENCONTRADOS:")
for titulo, (vid, title) in results.items():
    if vid:
        print(f"'{titulo}': 'https://www.youtube.com/watch?v={vid}',")
    else:
        print(f"'{titulo}': 'NO_ENCONTRADO',")
