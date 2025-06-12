# db/user.py
from database.connection import get_connection

def add_user(telegram_id: int, name: str):
    """
    Foydalanuvchini bazaga qo‘shadi. Agar foydalanuvchi
    mavjud bo‘lsa, e'tiborsiz qoldiriladi.
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT OR IGNORE INTO users (telegram_id, name)
        VALUES (?, ?)
    """, (telegram_id, name))

    conn.commit()
    conn.close()


def get_user_by_telegram_id(telegram_id: int):
    """
    Telegram ID orqali foydalanuvchini bazadan oladi.
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM users WHERE telegram_id = ?
    """, (telegram_id,))

    user = cursor.fetchone()
    conn.close()
    return user


def get_user_id(telegram_id: int):
    """
    Telegram ID orqali foydalanuvchining
    ichki `id` (PK) sini oladi.
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id FROM users WHERE telegram_id = ?
    """, (telegram_id,))

    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None




