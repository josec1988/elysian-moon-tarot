# tarot_scraper.py

from dotenv import load_dotenv
import os
import requests
import psycopg2
from bs4 import BeautifulSoup

# ────────────────────────────────────────────────────────────────────────────────
# Load DB connection string from .env
load_dotenv()
DB_CONNECTION = os.getenv("DB_CONNECTION")
if not DB_CONNECTION:
    raise RuntimeError("Missing DB_CONNECTION environment variable")
# ────────────────────────────────────────────────────────────────────────────────

def scrape_tarot():
    # your existing scraping logic…
    # e.g.:
    response = requests.get("https://example.com/tarot-card-list")
    soup = BeautifulSoup(response.text, "html.parser")
    cards = [c.text for c in soup.select(".card-name")]
    
    # connect using the env var
    conn = psycopg2.connect(DB_CONNECTION)
    cur = conn.cursor()
    for card in cards:
        cur.execute("INSERT INTO tarot_cards (name) VALUES (%s)", (card,))
    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    scrape_tarot()
