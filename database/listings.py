# database/listings.py
import sqlite3
from config import settings

conn = sqlite3.connect(settings.database_path)
cursor = conn.cursor()

def get_user_listings(telegram_id):
    cursor.execute("""
        SELECT listings.id, location, price, rent_type, 
        rooms, photo, description, created_at
        
        FROM listings
        JOIN users ON listings.user_id = users.id
        WHERE users.telegram_id = ?
        ORDER BY created_at DESC
    """, (telegram_id,))
    return cursor.fetchall()


def get_all_listings():
    conn = sqlite3.connect("rentbot.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM listings ORDER BY id DESC")
    rows = cursor.fetchall()
    conn.close()

    return [dict(row) for row in rows]



