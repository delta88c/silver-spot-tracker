import sqlite3
from config import DB_FILE

def init_db():
    with sqlite3.connect(DB_FILE) as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS prices (
                date TEXT PRIMARY KEY,
                price REAL
            )
        ''')

def save_price(date, price):
    with sqlite3.connect(DB_FILE) as conn:
        conn.execute('INSERT OR REPLACE INTO prices (date, price) VALUES (?, ?)', (date, price))

def get_price(date):
    with sqlite3.connect(DB_FILE) as conn:
        cur = conn.execute('SELECT price FROM prices WHERE date = ?', (date,))
        row = cur.fetchone()
        return row[0] if row else None

def get_latest_dates(n=30):
    with sqlite3.connect(DB_FILE) as conn:
        cur = conn.execute('SELECT date FROM prices ORDER BY date DESC LIMIT ?', (n,))
        return [row[0] for row in cur.fetchall()]

def get_prices_for_period(days=30):
    with sqlite3.connect(DB_FILE) as conn:
        cur = conn.execute('SELECT date, price FROM prices ORDER BY date DESC LIMIT ?', (days+1,))
        return cur.fetchall()
