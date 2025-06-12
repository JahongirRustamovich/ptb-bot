# db/listing.py
import sqlite3
from typing import List, Tuple, Optional

# Bazaga ulanish
conn = sqlite3.connect("rentbot.db")
cursor = conn.cursor()

# E'lonlar jadvalini yaratish (agar mavjud bo'lmasa)
cursor.execute("""
CREATE TABLE IF NOT EXISTS listings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    location TEXT,
    price INTEGER,
    rent_type TEXT,
    rooms INTEGER,
    photo TEXT,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")
conn.commit()


def add_listing(user_id: int, location: str,
                price: int, rent_type: str,
                rooms: int, photo: str,
                description: str) -> None:
    cursor.execute("""
        INSERT INTO listings (user_id, location, price, 
        rent_type, rooms, photo, description)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (user_id, location, price,
          rent_type, rooms, photo, description))
    conn.commit()


def get_user_listings(telegram_id: int) -> List[Tuple]:
    cursor.execute("""
        SELECT listings.id, listings.location, 
               listings.price, listings.rent_type,
               listings.rooms, listings.photo, 
               listings.description, listings.created_at
        FROM listings
        JOIN users ON listings.user_id = users.id
        WHERE users.telegram_id = ?
    """, (telegram_id,))
    return cursor.fetchall()


def delete_listing(listing_id: int) -> None:
    cursor.execute("DELETE FROM listings "
                   "WHERE id = ?", (listing_id,))
    conn.commit()


