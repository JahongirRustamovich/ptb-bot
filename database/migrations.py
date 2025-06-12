# database/migrations.py
import sqlite3

def add_photo_path_column():
    conn = sqlite3.connect("rentbot.db")
    cursor = conn.cursor()

    try:
        # photo_path mavjud bo‘lmasa qo‘shadi
        cursor.execute("ALTER TABLE listings "
                       "ADD COLUMN photo_path TEXT")
        print("✅ photo_path ustuni qo‘shildi.")
    except sqlite3.OperationalError as e:
        print(f"ℹ️ Ehtimol ustun allaqachon mavjud: {e}")

    conn.commit()
    conn.close()

if __name__ == "__main__":
    add_photo_path_column()




